
import numpy as np

def matrix(m,n):
    M = []
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        M.append(row)
    return M

def matrix_add(A,B):
    sum = []
    for i in range(len(A)): #Number of rows
        row = []
        for j in range(len(A[0])): #number of columns
            row.append(A[i][j] + B[i][j])
        sum.append(row)
    return sum

def matrix_product(A,B):
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            Product = 0
            for k in range(len(A[0])):
                Product = Product + A[i][k] * B[k][j]
            row.append(Product)
        C.append(row)
    return C
    
def matrix_formt(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end = " ")
        print()

m = int(input("Enter the number of rows (m):"))
n = int(input("Enter the number of columns (n):"))

print("Enter elements of matrix A:")
A = matrix(m,n)
matrix_formt(A)

print("Enter elements of matrix 2:")
B = matrix(m,n)
matrix_formt(B)

print("The addition of matrix is : ")
add = matrix_add(A,B)
matrix_formt(add)

print("The Product of matrix is : ")
result = matrix_product(A,B)
matrix_formt(result)

