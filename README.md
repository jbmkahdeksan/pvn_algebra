[Pura Vida Neutrosophic Algebra](https://arxiv.org/pdf/2312.02169) is a initiative lead byRanulfo Paiva Barbosa and Florentin Smarandache.
This project aims to implement these ideas into a Python module which can be utilized for other several applications.

### Content
A simple neutrosophic number is a number of the form "X = a + bI".
Where "a" is a real or complex coefficient and "b" is a real or complex number binded to indeterminacy (I).
    
Operations for Simple Neutrosophic Number stated in Pura Vida Neutrosophic Algebra are:
- Addition using Max-Plus algebra.
    Having two simple neutrosophic numbers X = a + bI and Y = c + dI.
    > Their addition is X @ Y = max(a, c) + max(b, d)I.
- Addition using Min-Plus (Tropical) algebra.
    Having two simple neutrosophic numbers X = a + bI and Y = c + dI. 
    > Their addition is X + Y = min(a, c) + min(b, d)I.
- Multiplication.
    Having two simple neutrosophic numbers X = a + bI and Y = c + dI.
    > Their multiplication is X * Y = (a + c) + (b + d)I.

### Limitations
Current features missing:
* Support for complex numbers
* Support for matrix operations

### How to use
Adding this project to PyPI is intended for a better adoption
Right now you can copy and paste the code to your project.

Here is a simple example of the current features:
![alt text](/src/image.png)