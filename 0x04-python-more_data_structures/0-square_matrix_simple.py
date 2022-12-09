#!/usr/bin/python3
# _ _ _ _ _ THIS PROJECT SQUARED THE ITEMS IN A NESTED LIST _ _ _ _ _ _
def square_matrix_simple(matrix=[]):
    #  _ _ _ _ _ _ COPY OF THE LIST _ _ _ _ _ _ _
    square = []
    # _ _ FOR LOOP _ _
    for row in matrix:
        square.append([num ** 2 for num in row])
    return square
