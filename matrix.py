
"""
# Matrix Operations Script
# Author: CyberGhoul(cyb3rgh0u1)
# This script is property of cyb3rgh0u1. It was a test project of
# mine, so you can use or modify it.
# For those who are going to use this code as it is free:
# Please give credit to cyb3rgh0u1.
# ---------------------------------------------------------------
"""

def input_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = float(input(f"Enter value for element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def input_minor(matrix, i, j):
    minor_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
    return minor_matrix


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant([row[:c] + row[c+1:] for row in matrix[1:]])
    return det



def output_cofactor(matrix, i, j):
    minor_matrix = input_minor(matrix, i, j)
    minor = determinant(minor_matrix)
    cofactor = ((-1) ** (i + j)) * minor
    return minor, cofactor



def main():
    n = int(input("Enter the size of your matrix: "))
    matrix = input_matrix(n)
    print("Matrix:")
    print_matrix(matrix)

    # Determinant of the matrix
    det = determinant(matrix)
    print(f"Determinant of the matrix is: {det}")

    i = int(input(f"Enter the row position (1 to {n}) of the element: ")) - 1
    j = int(input(f"Enter the column position (1 to {n}) of the element: ")) - 1

    # Minor & Cofactor of the matrix
    minor, cofactor = output_cofactor(matrix, i, j)
    print(f"Minor of the element in position [{i+1}][{j+1}] is: {minor}")
    print(f"Cofactor of the element in position [{i+1}][{j+1}] is: {cofactor}")



if __name__ == "__main__":
    main()
