def scalar_multiply_matrix(A, B):
    return [[element * B for element in row] for row in A]
rows = int(input("Enter the number of rows in matrix A: "))
cols = int(input("Enter the number of columns in matrix A: "))

A = []
print("Enter the elements of matrix A (separated by spaces):")
for i in range(rows):
    row_input = input().split()
    row = [int(element) for element in row_input]
    A.append(row)
B = int(input("Enter the scalar B: "))
result = scalar_multiply_matrix(A, B)
print("Result of scalar multiplication:")
for row in result:
    print(row)
