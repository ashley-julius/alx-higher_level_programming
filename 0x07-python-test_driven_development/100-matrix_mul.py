#!/usr/bin/python3
""" This project multiplies two matrices using for loop """


def matrix_mul(m_a, m_b):
    """ This function multiplies two matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if m_a == [] or m_a == [[]] and len(row) == 0:
            raise ValueError("m_a can't be empty")
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError("m_a should contain only integers\
 or floats")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if m_b == [] or m_b == [[]] and len(row) == 0:
            raise ValueError("m_b can't be empty")
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError("m_b should contain only integers\
 or floats")
    first_row_length_a = len(m_a[0])
    first_row_length_b = len(m_b[0])
    for i in m_b:
        if len(i) != first_row_length_b or not row:
            raise TypeError("each row of m_b must be of the \
same size")
    for i in m_a:
        if len(i) != first_row_length_a or not row:
            raise TypeError("each row of m_a must be of the \
same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_a[0])):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result.append(row)
    return result
