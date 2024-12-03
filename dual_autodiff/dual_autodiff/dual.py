import math

class Dual:
    """
    A class to compute various operations on Dual type number.

    Attributes:
        real (float): The input real part of a Dual.
        dual (float): The input dual part of a Dual.
    """
    def __init__(self, real, dual=0):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        '''Addition'''
        if isinstance(other, Dual):
            # Dual + Dual
            return Dual(self.real + other.real, self.dual + other.dual)
        else:
            # Dual + scalar
            return Dual(self.real + other, self.dual)


    def __sub__(self, other):
        '''Substractive with self on the left'''
        if isinstance(other, Dual):
            # Dual - Dual
            return Dual(self.real - other.real, self.dual - other.dual)
        else:
            # Dual - scalar
            return Dual(self.real - other, self.dual)
    
    def __rsub__(self, other):
        '''Substractive with self on the right'''
        if isinstance(other, Dual):
            # Dual - Dual
            return Dual(other.real - self.real, other.dual - self.dual)
        else:
            # scalar - Dual
            return Dual(other - self.real, -self.dual)


    def __mul__(self, other):
        '''Multiplication with self on the left'''
        if isinstance(other, Dual):
            # Dual * Dual
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
        else:
            # Dual * scalar
            return Dual(self.real * other, self.dual * other)

    def __rmul__(self, other):
        '''Multiplication with self on the right'''
        if isinstance(other, Dual):
            # Dual * Dual
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
        else:
            # Dual * scalar
            return Dual(self.real * other, self.dual * other)


    def __truediv__(self, other):
        '''Division with self on the left'''
        if isinstance(other, Dual):
            # Dual / Dual
            if other.real == 0:
                raise ZeroDivisionError("Division by a Dual with real part zero")
            return Dual(
                self.real / other.real,
                (self.dual * other.real - self.real * other.dual) / (other.real ** 2)
            )
        else:
            # Dual / scalar
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return Dual(self.real / other, self.dual / other)

    def __rtruediv__(self, other):
        '''Division with self on the right'''
        if self.real == 0:
            raise ZeroDivisionError("Division by a Dual with real part zero")
        if isinstance(other, Dual):
            # Dual / Dual
            return Dual(
                other.real / self.real,
                (other.dual * self.real - other.real * self.dual) / (self.real ** 2)
            )
        else:
            # scalar / Dual
            return Dual(other / self.real, -other * self.dual / (self.real ** 2))

    def exp(self):
        '''Exponential operation'''
        exp_real = math.exp(self.real)
        return Dual(exp_real, self.dual * exp_real)

    def log(self):
        '''Logarithmic operation'''
        if self.real <= 0:
            raise ValueError("Logarithm defined only for positive real numbers!")
        return Dual(math.log(self.real), self.dual / self.real)
    
    def __pow__(self, power):
        '''Power operation'''
        if isinstance(power, Dual):
            # Dual ^ Dual
            preal = self.real ** power.real
            pdual = (
                preal
                * (power.dual * math.log(self.real) + power.real * self.dual / self.real)
            )
            return Dual(preal, pdual)
        else:
            # Dual ^ float/int
            preal = self.real ** power
            pdual = power * (self.real ** (power - 1)) * self.dual
            return Dual(preal, pdual)

    def sin(self):
        '''Sine operation'''
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))

    def cos(self):
        '''Cosine operation'''
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))
    
    def tan(self):
        '''Tangent operation'''
        if math.isclose(math.cos(self.real), 0, abs_tol=1e-9):   # have Used Chatgpt to debug, previously it was: if math.cos(self.real) == 0:
            raise ValueError("Tangent only defined for the value whose .cos != 0")
        return Dual(math.tan(self.real), self.dual * (1 + math.tan(self.real)**2 ) )


    def __repr__(self):
        '''Generate a string representation of the object'''
        return f"Dual(real={self.real}, dual={self.dual})"

