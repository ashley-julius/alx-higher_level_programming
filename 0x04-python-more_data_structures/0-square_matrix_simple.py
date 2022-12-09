#!/usr/bin/python3
# _ _ _ _ _ THIS PROJECT SQUARED THE ITEMS IN A NESTED LIST _ _ _ _ _ _ 
def square_matrix_simple(matrix=[]):
    #  _ _ _ _ _ _ COPY OF THE LIST _ _ _ _ _ _ _
    square = []
    # _ _ FOR LOOP _ _ 
    for i in range(3):
        item = []
        for j in range(3):
            item.append(matrix[i][j] ** 2)
        square.append(item)
    return square

