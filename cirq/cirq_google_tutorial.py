#At the base of this construction is the notion of a qubit. In Cirq, qubits and other quantum objects are identified by instances of subclasses of the  Qidbase class. Different subclasses of Qid can be used for different purposes. For example, the qubits that Google’s Xmon devices use are often arranged on the vertices of a square grid. For this, the class GridQubit subclasses Qid. For example, we can create a 3 by 3 grid of qubits using

import cirq
qubits = [cirq.GridQubit(x, y) for x in range(3) for y in range(3)]

print('-------------RESULT-------------')

print(qubits[0])

#------RESULT---------

#      (0, 0)


# The next level up is the notion of a Gate. A Gate represents a physical process that occurs on a Qubit. The important property of a Gate is that it can be applied to one or more qubits. This can be done via the Gate.on method itself or via (), and doing this turns the Gate into a GateOperation.

# This is an Pauli X gate. It is an object instance.
x_gate = cirq.X
# Applying it to the qubit at location (0, 0) (defined above)
# turns it into an operation.
x_op = x_gate(qubits[0])

print('-------------RESULT-------------')

print(x_op)

#------RESULT---------

#    X((0, 0))



#A Moment is simply a collection of operations, each of which operates on a different set of qubits, and which conceptually represents these operations as occurring during this abstract time slice. The Moment structure itself is not required to be related to the actual scheduling of the operations on a quantum computer, or via a simulator, though it can be. For example, here is a Moment in which Pauli X and a CZ gate operate on three qubits:


cz = cirq.CZ(qubits[0], qubits[1])
x = cirq.X(qubits[2])
moment = cirq.Moment([x, cz])

print('-------------RESULT-------------')

print(moment)

#------RESULT---------

#    X((0, 2)) and CZ((0, 0), (0, 1))



#The above is not the only way one can construct moments, nor even the typical method, but illustrates that a Moment is just a collection of operations on disjoint sets of qubits.
#Finally, at the top level a Circuit is an ordered series of Moment objects. The first Moment in this series contains the first Operations that will be applied. Here, for example, is a simple circuit made up of two moments:

cz01 = cirq.CZ(qubits[0], qubits[1])
x2 = cirq.X(qubits[2])
cz12 = cirq.CZ(qubits[1], qubits[2])
moment0 = cirq.Moment([cz01, x2])
moment1 = cirq.Moment([cz12])
circuit = cirq.Circuit((moment0, moment1))

print('-------------RESULT-------------')

print(circuit)


#------RESULT---------

#   (0, 0): ───@───────
#              │
#   (0, 1): ───@───@───
#                  │
#   (0, 2): ───X───@───

#Constructing circuits
#Constructing Circuits as a series of Moment objects, with each Moment being hand-crafted, is tedious. Instead, we provide a variety of different ways to create a Circuit.
#One of the most useful ways to construct a Circuit is by appending onto the Circuit with the Circuit.append method.

from cirq.ops import CZ, H
q0, q1, q2 = [cirq.GridQubit(i, 0) for i in range(3)]
circuit = cirq.Circuit()
circuit.append([CZ(q0, q1), H(q2)])

print('-------------RESULT-------------')

print(circuit)


#------RESULT---------

#(0, 0): ───@───
#           │
#(1, 0): ───@───
#
#(2, 0): ───H───


#This appended a new moment to the qubit, which we can continue to do:

circuit.append([H(q0), CZ(q1, q2)])

print('-------------RESULT-------------')

print(circuit)


#------RESULT---------

#(0, 0): ───@───H───
#           │
#(1, 0): ───@───@───
#               │
#(2, 0): ───H───@───

#We see that here we have again created two Moment objects. How did Circuit know how to do this? Circuit's Circuit.append method (and its cousin, Circuit.insert) both take an argument called the InsertStrategy. By default, InsertStrategy is InsertStrategy.NEW_THEN_INLINE.

#InsertStrategies
#InsertStrategy defines how Operations are placed in a Circuit when requested to be inserted at a given location. Here, a location is identified by the index of the Moment (in the Circuit) where the insertion is requested to be placed at (in the case of Circuit.append, this means inserting at the Moment, at an index one greater than the maximum moment index in the Circuit).

#There are four such strategies: InsertStrategy.EARLIEST, InsertStrategy.NEW, InsertStrategy.INLINE and InsertStrategy.NEW_THEN_INLINE.

#InsertStrategy.EARLIEST, which is the default, is defined as:

#Scans backward from the insert location until a moment with operations touching qubits affected by the operation to insert is found. The operation is added to the moment just after that location.

#For example, if we first create an Operation in a single moment, and then use InsertStrategy.EARLIEST, Operation can slide back to this first Moment if there is space:

from cirq.circuits import InsertStrategy

circuit = cirq.Circuit()
circuit.append([CZ(q0, q1)])
circuit.append([H(q0), H(q2)], strategy=InsertStrategy.EARLIEST)

print('-------------RESULT-------------')

print(circuit)


#------RESULT---------

#(0, 0): ───@───H───
#           │
#(1, 0): ───@───────
#
#(2, 0): ───H───────


#After creating the first moment with a CZ gate, the second append uses the InsertStrategy.EARLIEST strategy. The H on q0 cannot slide back, while the H on q2 can and so ends up in the first Moment.

#Contrast this with InsertStrategy.NEW that is defined as:

#Every operation that is inserted is created in a new moment.

circuit = cirq.Circuit()
circuit.append([H(q0), H(q1), H(q2)], strategy=InsertStrategy.NEW)

print('-------------RESULT-------------')

print(circuit)


#(0, 0): ───H───────────
#
#(1, 0): ───────H───────
#
#(2, 0): ───────────H───



#Here every operator processed by the append ends up in a new moment. InsertStrategy.NEW is most useful when you are inserting a single operation and do not want it to interfere with other Moments.

#Another strategy is InsertStrategy.INLINE:

#Attempts to add the operation to insert into the moment just before the desired insert location. But, if there’s already an existing operation affecting any of the qubits touched by the operation to insert, a new moment is created instead.


circuit = cirq.Circuit()
circuit.append([CZ(q1, q2)])
circuit.append([CZ(q1, q2)])
circuit.append([H(q0), H(q1), H(q2)], strategy=InsertStrategy.INLINE)

print('-------------RESULT-------------')

print(circuit)


#------RESULT---------

#(0, 0): ───────H───────
#
#(1, 0): ───@───@───H───
#           │   │
#(2, 0): ───@───@───H───








