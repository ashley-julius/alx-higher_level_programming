#!/usr/bin/python3
""" This project multiply two matrices with numpy """
import numpy as np
""" importing the numpy module """


def lazy_matrix_mul(m_a, m_b):
    """ This function multiply matrices using numpy"""
    result = (np.dot(m_a, m_b))
    return result
