import cirq

print('-------------CODE--------------')

print('')

print('circuit = cirq.Circuit()')
print('(a0, b1, c2, d3, e4) = cirq.LineQubit .range(5)')
print('circuit.append([cirq.H(a0), cirq.CNOT(a0, c2), cirq.CNOT(c2, e4)])')
print('circuit.append([cirq.measure(a0), cirq.measure(b1), cirq.measure(c2), cirq.measure(d3), cirq.measure(e4)])')
#print('circuit.append([cirq.H(a0), cirq.CNOT(a0, c2), cirq.CNOT(c2, e4)])')

print('')

circuit  = cirq.Circuit()
(a0, b1, c2, d3, e4) = cirq.LineQubit .range(5)

circuit.append([cirq.H(a0), cirq.CNOT(a0, c2), cirq.CNOT(c2, e4)])
circuit.append([cirq.measure(a0), cirq.measure(b1), cirq.measure(c2), cirq.measure(d3), cirq.measure(e4)])
#circuit.append([cirq.H(a0), cirq.CNOT(a0, c2), cirq.CNOT(c2, e4)])
print('------------RESULT-------------')

print('')

print(circuit)

print('')
#a0: ───H───@───M───H───@───────
#           │           │
#b1: ───M───┼───────────┼───────
#           │           │
#c2: ───────X───@───M───X───@───
#               │           │
#d3: ───M───────┼───────────┼───
#               │           │
#e4: ───────────X───M───────X───
