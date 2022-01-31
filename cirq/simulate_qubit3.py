import cirq

circuit  = cirq.Circuit()
(q0, q1, q2, q3, q4) = cirq.LineQubit .range(5)

circuit.append([cirq.H(q0), cirq.CNOT(q0, q2), cirq.CNOT(q2, q4)])
circuit.append([cirq.measure(q0), cirq.measure(q1), cirq.measure(q2), cirq.measure(q3), cirq.measure(q4)])

print(circuit)

