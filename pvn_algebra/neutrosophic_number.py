"""
This module contains the implementation of a neutrosophic number
and its operations based on the paper: Pura Vida Neutrosophic Algebra.
"""

from dataclasses import dataclass


@dataclass
class Indeterminacy:
    """Represents the indeterminacy part of a neutrosophic number."""
    coefficient: float


class NeutrosophicNumber:
    """
    A neutrosophic number is a number of the form "X = a + bI".
    Where "a" is a real or complex coefficient and
    "b" is a real or complex number binded to indeterminacy (I).

    Having two neutrosophic numbers `X = a + bI` and `Y = c + dI`
    Operations for them stated in Pura Vida Neutrosophic Algebra are:
    - Addition using Max-Plus algebra.
        > X + Y = max(a, c) + max(b, d)I.
    - Addition using Min-Plus (Tropical) algebra.
        > X - Y = min(a, c) + min(b, d)I.
    - Multiplication.
        > X * Y = (a + c) + (b + d)I.
    """

    def __init__(self, a: float = 0, indet: float = 0):
        self.coefficient = a
        self.indet = Indeterminacy(indet)

    def __add__(self, other: 'NeutrosophicNumber') -> 'NeutrosophicNumber':
        return NeutrosophicNumber(
            self.coefficient + other.coefficient,
            self.indet.coefficient + other.indet.coefficient
        )

    def __sub__(self, other: 'NeutrosophicNumber') -> 'NeutrosophicNumber':
        return NeutrosophicNumber(
            self.coefficient - other.coefficient,
            self.indet.coefficient - other.indet.coefficient
        )

    def add_max(self, other: "NeutrosophicNumber") -> "NeutrosophicNumber":
        """Addition using Max-Plus algebra."""
        return NeutrosophicNumber(
            max(self.coefficient, other.coefficient),
            max(self.indet.coefficient, other.indet.coefficient),
        )

    def add_min(self, other: "NeutrosophicNumber") -> "NeutrosophicNumber":
        """Addition using Min-Plus (Tropical) algebra."""
        return NeutrosophicNumber(
            min(self.coefficient, other.coefficient),
            min(self.indet.coefficient, other.indet.coefficient),
        )

    def multiply(self, other: "NeutrosophicNumber") -> "NeutrosophicNumber":
        """Multiplication"""
        return NeutrosophicNumber(
            self.coefficient + other.coefficient, 
            self.indet.coefficient + other.indet.coefficient
        )

    def __repr__(self):
        sign = "+" if self.indet.coefficient >= 0 else "-"
        return f"({self.coefficient}{sign}{self.indet.coefficient.__abs__()}I)"


def add_min(number1: "NeutrosophicNumber", number2: "NeutrosophicNumber"):
    return number1.add_min(number2)


def add_max(number1: "NeutrosophicNumber", number2: "NeutrosophicNumber"):
    return number1.add_max(number2)


def multiply(number1: "NeutrosophicNumber", number2: "NeutrosophicNumber"):
    return number1.multiply(number2)


x = NeutrosophicNumber(5, 6)
y = NeutrosophicNumber(-1, 14)

print(f"x = {x}")
print(f"y = {y}")

print(f"number.add_max(x, y) = {x.add_max(y)}")
print(f"number.add_min(x, y) = {x.add_min(y)}")
print(f"number.multiply(x, y) = {x.multiply(y)}")


print(NeutrosophicNumber(1))
print(NeutrosophicNumber(indet=9))
print(NeutrosophicNumber())
