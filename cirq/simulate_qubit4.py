import cirq

circuit  = cirq.Circuit()
(a, b, c, d, e) = cirq.LineQubit .range(5)

circuit.append([cirq.H(a), cirq.CNOT(a, c), cirq.CNOT(c, e)])
circuit.append([cirq.measure(a), cirq.measure(b), cirq.measure(c), cirq.measure(d), cirq.measure(e)])
circuit.append([cirq.H(a), cirq.CNOT(a, c), cirq.CNOT(c, e)])
print(circuit)

