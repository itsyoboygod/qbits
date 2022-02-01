import cirq 

lenght = 3

qubits = [cirq.GridQubit(i, j) for i in range(lenght) for j in range(lenght)]

print(qubits)
