import math


#Calculus: Taylor Series for Sin(x)
def taylor_sin(x, terms: int):
    """Approximate sin(x) using the first terms of its Taylor series."""
    approximation = 0
    for k in range(terms):
        approximation = approximation + (-1) ** k * x ** (2 * k + 1) / math.factorial(2 * k + 1)
    return approximation