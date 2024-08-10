'''
This module contains the implementation of simple neutrosophic number and its operations.
based on the Pura Vida Neutrosophic Algebra.
'''
from dataclasses import dataclass
import numpy as np

@dataclass
class Indeterminacy:
    '''Represents the indeterminacy part of a simple neutrosophic number.'''
    coefficient: float

class SimpleNeutrosophicNumber:
    '''
    A simple neutrosophic number is a number of the form "X = a + bI".
    Where "a" is a real or complex coefficient and 
    "b" is a real or complex number binded to indeterminacy (I).
    
    Operations for Simple Neutrosophic Number are:
    - Addition using Max-Plus algebra.
        Having two simple neutrosophic numbers X = a + bI and Y = c + dI.
        Their addition is X @ Y = max(a, c) + max(b, d)I.
    - Addition using Min-Plus (Tropical) algebra.
        Having two simple neutrosophic numbers X = a + bI and Y = c + dI. 
        Their addition is X + Y = min(a, c) + min(b, d)I.
    - Multiplication.
        Having two simple neutrosophic numbers X = a + bI and Y = c + dI.
        Their multiplication is X * Y = (a + c) + (b + d)I.
    '''
    def __init__(self, a, b):
        self.coefficient = a
        self.indeterminacy = Indeterminacy(b)

    def __matmul__(self, other: 'SimpleNeutrosophicNumber') -> 'SimpleNeutrosophicNumber':
        '''Addition using Max-Plus algebra.'''
        return SimpleNeutrosophicNumber(
            max(self.coefficient, other.coefficient),
            max(self.indeterminacy.coefficient, other.indeterminacy.coefficient))

    def __add__(self, other: 'SimpleNeutrosophicNumber') -> 'SimpleNeutrosophicNumber':
        '''Addition using Min-Plus (Tropical) algebra.'''
        return SimpleNeutrosophicNumber(
            min(self.coefficient, other.coefficient),
            min(self.indeterminacy.coefficient, other.indeterminacy.coefficient))

    def __mul__(self, other: 'SimpleNeutrosophicNumber') -> 'SimpleNeutrosophicNumber':
        '''Multiplication'''
        return SimpleNeutrosophicNumber(
            self.coefficient + other.coefficient,
            self.indeterminacy.coefficient + other.indeterminacy.coefficient)

    def __str__(self):
        '''String representation of the simple neutrosophic number.'''
        sign = "+" if self.indeterminacy.coefficient >= 0 else "-"
        return f"{self.coefficient} {sign} {self.indeterminacy.coefficient}I"
    
    def __repr__(self):
        return self.__str__()