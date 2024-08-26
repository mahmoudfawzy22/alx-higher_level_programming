#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = []
        for column in row:
            squared_row.append(column**2)  
        result.append(squared_row)
    return result
