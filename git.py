# i. Using Python Lists

# Define matrices
A = [[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]]
B = [[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]]
C = [[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]]

# Function to add two matrices
def add_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Function to subtract two matrices
def subtract_matrices(mat1, mat2):
    return [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Function to multiply two matrices
def multiply_matrices(mat1, mat2):
    return [[sum(a*b for a,b in zip(row, col)) for col in zip(*mat2)] for row in mat1]

# Perform operations
sum_AB = add_matrices(A, B)
diff_AC = subtract_matrices(A, C)
prod_BC = multiply_matrices(B, C)

print("Using Python Lists:")
print("Sum of A and B:", sum_AB)
print("Difference of A and C:", diff_AC)
print("Product of B and C:", prod_BC)

# ii. Using NumPy

import numpy as np

# Define matrices
A_np = np.array(A)
B_np = np.array(B)
C_np = np.array(C)

# Perform operations
sum_AB_np = A_np + B_np
diff_AC_np = A_np - C_np
prod_BC_np = np.dot(B_np, C_np)

print("\nUsing NumPy:")
print("Sum of A and B:", sum_AB_np)
print("Difference of A and C:", diff_AC_np)
print("Product of B and C:", prod_BC_np)