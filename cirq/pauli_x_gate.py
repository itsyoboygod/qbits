#------------Pauli's X Gate--------------#

import cirq

length = 3

qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]

circuit  = cirq.Circuit()

#---NOT Gate (if input == 1 then output == 0. And vice versa)---#
circuit.append(cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1)

print(circuit)


#------------Hadamard's Gate--------------#
#length = 3
#qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]
#circuit  = cirq.Circuit()
#---ON/OFF Gate (50% chance of being on or off)---#
#circuit.append(cirq.H(q) for q in qubits if (q.row + q.col) % 2 == 0)
#print(circuit)
