
import numpy as np

# Read matrix dimensions MxN
M = int(input("Enter the number of rows (M): "))
N = int(input("Enter the number of columns (N): "))

# Initialize matrices
matrix1 = []
matrix2 = []

# Read matrix elements
print("Enter elements of matrix 1:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(float(input(f"Enter element at position ({i+1},{j+1}): ")))
    matrix1.append(row)

print("Enter elements of matrix 2:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(float(input(f"Enter element at position ({i+1},{j+1}): ")))
    matrix2.append(row)

# Addition of two matrices
result_addition = np.add(matrix1, matrix2)

# Product of two matrices
result_product = np.dot(matrix1, matrix2)

print("Matrix 1:")
print(np.array(matrix1))
print("Matrix 2:")
print(np.array(matrix2))
print("Matrix Addition:")
print(result_addition)
print("Matrix Product:")
print(result_product)