from libc.math cimport exp, log, sin, cos, tan, pow

cdef inline bint isclose(double a, double b, double bias):  # no isclose() func in C 
    """
    A function to judge whether the gap between number a and number b is smaller than the set max bias, if so, return True, otherwise False.

    Attributes:
        a (double): The input real part of a Dual.
        b (double): The input dual part of a Dual.
        bias (double): The input bias that sets the max gap between a and b
    """
    return abs(a - b) <= bias

cdef class Dual:
    """
    A class to compute various operations on Dual type number.

    Attributes:
        real (double): The input real part of a Dual.
        dual (double): The input dual part of a Dual.
    """
    cdef double real
    cdef double dual

    def __cinit__(self, double real, double dual=0):
        self.real = real
        self.dual = dual

    cpdef double get_real(self):
        return self.real

    cpdef void set_real(self, double value):
        self.real = value

    cpdef double get_dual(self):
        return self.dual

    cpdef void set_dual(self, double value):
        self.dual = value
    
    def __repr__(self):
        return f"Dual(real={self.real}, dual={self.dual})"

# ------------------ add ---------------------------#
    cdef inline Dual _add(self, Dual other):
        return Dual(self.real + other.real, self.dual + other.dual)

    def __add__(self, other):
        cdef double scalar         # pre-declare variables, otherwise meet error
        if isinstance(other, Dual):
            return self._add(other)
        else:
            scalar = <double>other 
            return Dual(self.real + scalar, self.dual)

# ------------------ sub ---------------------------#
    cdef inline Dual _sub_dual(self, Dual other):
        cdef double result_real = self.real - other.real
        cdef double result_dual = self.dual - other.dual
        return Dual(result_real, result_dual)

    cdef inline Dual _sub_scalar(self, double scalar):
        return Dual(self.real - scalar, self.dual)

    def __sub__(self, other):
        cdef double scalar
        if isinstance(other, Dual):
            return self._sub_dual(other)
        else:
            scalar = <double>other
            return self._sub_scalar(scalar)

# ------------------ rsub ---------------------------#
    cdef inline Dual _rsub_dual(self, Dual other):
        cdef double result_real = other.real - self.real
        cdef double result_dual = other.dual - self.dual
        return Dual(result_real, result_dual)

    cdef inline Dual _rsub_scalar(self, double scalar):
        cdef double result_real = scalar - self.real
        cdef double result_dual = -self.dual
        return Dual(result_real, result_dual)

    def __rsub__(self, other):
        cdef double scalar
        if isinstance(other, Dual): 
            return self._rsub_dual(other)
        else: 
            scalar = <double>other
            return self._rsub_scalar(scalar)

# ------------------ mul ---------------------------#
    cdef inline Dual _mul(self, Dual other):
        return Dual(
            self.real * other.real,
            self.real * other.dual + self.dual * other.real
        )

    def __mul__(self, other):
        cdef double scalar
        if isinstance(other, Dual):
            return self._mul(other)
        else:
            scalar = <double>other
            return Dual(self.real * scalar, self.dual * scalar)
# ------------------ rmul ---------------------------#
    def __rmul__(self, other):
        return self.__mul__(other)


# ------------------ truediv ---------------------------#
    cdef Dual _truediv_dual(self, Dual other):
        if other.real == 0.0:
            raise ZeroDivisionError("Division by a Dual with real part zero")
        cdef double denom = pow(other.real, 2)
        return Dual(
            self.real / other.real,
            (self.dual * other.real - self.real * other.dual) / denom
        )

    cdef Dual _truediv_scalar(self, double scalar):
        if scalar == 0.0:
            raise ZeroDivisionError("Division by zero")
        return Dual(self.real / scalar, self.dual / scalar)

    def __truediv__(self, other):
        cdef double scalar
        if isinstance(other, Dual):
            return self._truediv_dual(other)
        else:
            scalar = <double>other
            return self._truediv_scalar(scalar)

# ------------------ rtruediv ---------------------------#
    cdef inline Dual _rtruediv_dual(self, Dual other):
        cdef double denom = self.real * self.real
        return Dual(
            other.real / self.real,
            (other.dual * self.real - other.real * self.dual) / denom
        )

    def __rtruediv__(self, other):
        cdef double scalar
        cdef double denom = self.real * self.real
        if self.real == 0.0:
            raise ZeroDivisionError("Division by a Dual with real part zero")
        if isinstance(other, Dual):
            return self._rtruediv_dual(other)
        else:
            scalar = <double>other
            return Dual(
                scalar / self.real,
                -scalar * self.dual / denom
            )

# ------------------ exp ---------------------------#
    def exp(self):
        cdef double exp_real = exp(self.real)
        return Dual(exp_real, self.dual * exp_real)

# ------------------ log ---------------------------#
    cdef inline Dual _log(self):
        if self.real <= 0.0:
            raise ValueError("Logarithm defined only for positive real numbers")
        cdef double result_real = log(self.real)
        cdef double result_dual = self.dual / self.real
        return Dual(result_real, result_dual)

    cpdef Dual log(self):
        return self._log()
        
# ------------------ pow ---------------------------#
    cdef inline Dual _pow_dual(self, Dual power):
        cdef double preal = pow(self.real, power.real)
        cdef double pdual = (
            preal
            * (power.dual * log(self.real) + power.real * self.dual / self.real)
        )
        return Dual(preal, pdual)

    cdef inline Dual _pow_scalar(self, double scalar):
        cdef double preal = pow(self.real, scalar)
        cdef double pdual = scalar * pow(self.real, scalar - 1) * self.dual
        return Dual(preal, pdual)

    cpdef Dual pow(self, power):
        cdef double scalar
        if isinstance(power, Dual):
            return self._pow_dual(power)
        else:
            scalar = <double>power
            return self._pow_scalar(scalar)

# ------------------ sin cos tan ---------------------------#
    cdef inline Dual _sin_inline(self):
        cdef double sin_real = sin(self.real)
        cdef double cos_real = cos(self.real)
        return Dual(sin_real, self.dual * cos_real)

    cdef inline Dual _cos_inline(self):
        cdef double sin_real = sin(self.real)
        cdef double cos_real = cos(self.real)
        return Dual(cos_real, -self.dual * sin_real)

    
    cdef inline Dual _tan_inline(self):
        if isclose(cos(self.real), 0.0, bias=1e-5):
            raise ValueError("Tangent only defined for the value whose .cos != 0")

        cdef double real_part = tan(self.real)  
        cdef double sec_squared = 1.0 + tan(self.real)**2
        cdef double dual_part = self.dual * sec_squared
        return Dual(real_part, dual_part) 

    cpdef Dual sin(self):
        return self._sin_inline()

    cpdef Dual cos(self):
        return self._cos_inline()

    cpdef Dual tan(self):
        return self._tan_inline()


## the 'cpdef's used above exposing methods to the Python layer, also combined with Cython's optimisation to improve performance