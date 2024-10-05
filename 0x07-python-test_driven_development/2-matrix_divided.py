def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(item, (int, float)) for row in matrix for item in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])

    if not all(len(row) == row_length for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (float, int)):
         raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    matrix_2 = matrix

    return [[round(item / div, 2) for item in row] for row in matrix_2]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")