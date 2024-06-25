# Matrix Calculator

## Author
CyberGhoul (cyb3rgh0u1)

## Description
This script allows you to perform operations on a square matrix, including calculating minors, cofactors, and the determinant. It was initially a test project and is free to use and modify. If you use this code, please give credit to the author, cyb3rgh0u1.

## Features
- Input a square matrix of any size.
- Calculate the minor and cofactor of any element in the matrix.
- Compute the determinant of the matrix.

## Usage
1. **Download the Script**: Save the script to your local machine.
2. **Run the Script**: Execute the script using Python.
3. **Follow the Prompts**: Enter the size of the matrix and values for each element as prompted.
4. **Input Parameters**:
    - Row and column positions for minor and cofactor calculation.

### Example
```bash
python3 matrix.py
```
When prompted, enter the size of the matrix and values for each element. Then, specify the row and column positions for which you want to calculate the minor and cofactor.
```plaintext
Enter the size of your matrix: 3
Enter value for element [1][1]: 1
Enter value for element [1][2]: 2
Enter value for element [1][3]: 3
Enter value for element [2][1]: 4
Enter value for element [2][2]: 5
Enter value for element [2][3]: 6
Enter value for element [3][1]: 7
Enter value for element [3][2]: 8
Enter value for element [3][3]: 9
Matrix:
1.0 2.0 3.0
4.0 5.0 6.0
7.0 8.0 9.0
Enter the row position (1 to 3) of the element: 2
Enter the column position (1 to 3) of the element: 2
Minor of the element in position [2][2] is: -3.0
Cofactor of the element in position [2][2] is: -3.0
Determinant of the matrix is: 0.0
```



