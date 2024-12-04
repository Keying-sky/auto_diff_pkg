import pytest
from dual_autodiff_x.dual import Dual
import math

def test_dual_initialization():
    x = Dual(2, 4)
    assert x.real == 2
    assert x.dual == 4

def test_dual_addition():
    x = Dual(1, 2)
    y = Dual(2, 4)
    z = x + y
    assert z.real == 3
    assert z.dual == 6

# ---------------- Tests for subtraction ----------------- #
def test_dual_sub_dual():
    x = Dual(1, 2)
    y = Dual(2, 4)
    result = x - y
    assert result.real == -1
    assert result.dual == -2

def test_dual_sub_scalar():
    x = Dual(1, 2)
    result = x - 3
    assert result.real == -2
    assert result.dual == 2

def test_scalar_sub_dual():
    x = Dual(1, 2)
    result = 10 - x
    assert result.real == 9
    assert result.dual == -2


# ---------------- Tests for multiplication ----------------- #
def test_dual_mul_dual():
    x = Dual(3, 2)
    y = Dual(4, 1)
    result = x * y
    assert result.real == 12
    assert result.dual == 11

def test_dual_mul_scalar():
    x = Dual(3, 2)
    result = x * 5
    assert result.real == 15
    assert result.dual == 10

def test_scalar_mul_dual():
    x = Dual(3, 2)
    result = 5 * x
    assert result.real == 15
    assert result.dual == 10

# ---------------- Tests for division ----------------- #
def test_dual_div_dual():
    x = Dual(6, 4)
    y = Dual(3, 2)
    result = x / y
    assert result.real == 2
    assert result.dual == 0

def test_dual_div_scalar():
    x = Dual(6, 4)
    result = x / 2
    assert result.real == 3
    assert result.dual == 2

def test_scalar_div_dual():
    x = Dual(3, 2)
    result = 6 / x
    assert result.real == 2
    assert result.dual == -4 / 3

def test_dual_div_zero_dual():
    x = Dual(0, 2)
    with pytest.raises(ZeroDivisionError, match="Division by a Dual with real part zero"):
        Dual(3, 1) / x

def test_scalar_div_zero_dual():
    x = Dual(0, 2)
    with pytest.raises(ZeroDivisionError, match="Division by a Dual with real part zero"):
        10 / x

def test_dual_div_zero_scalar():
    x = Dual(3, 2)
    with pytest.raises(ZeroDivisionError, match="Division by zero"):
        x / 0


# ---------------- Tests for exponential operation ----------------- #
def test_exp_dual():
    x = Dual(2, 4)
    y = x.exp()
    assert y.real == pytest.approx(math.exp(2), rel=1e-5)
    assert y.dual == pytest.approx(4*math.exp(2), rel=1e-5)

# ---------------- Tests for logarithmic operation ----------------- #
def test_log_dual():
    x = Dual(2, 2)
    y = x.log()
    assert y.real == pytest.approx(math.log(2), rel=1e-5)
    assert y.dual == pytest.approx(1, rel=1e-5)         

# ---------------- Tests for power operation ----------------- #
def test_scalar_power():
    x = Dual(2, 1)
    power = 3
    y = x ** power
    assert y.real == 8
    assert y.dual == 12

def test_dual_power():
    x = Dual(2, 1) 
    y = Dual(3, 0.5) 
    z = x ** y
    assert z.real == pytest.approx(8, rel=1e-5)
    assert z.dual == pytest.approx(8 * (0.5 * math.log(2) + 1.5) , rel=1e-5)


# ---------------- Tests for trigonometric operation ----------------- #
def test_dual_sine():
    x = Dual(math.pi/2, 2) 
    y = x.sin()
    assert y.real == pytest.approx(1, rel=1e-5)  
    assert y.dual == pytest.approx(0, rel=1e-5) 

def test_dual_cosine():
    x = Dual(math.pi/2, 2)  
    y = x.cos()
    assert y.real == pytest.approx(0, rel=1e-5)  
    assert y.dual == pytest.approx(-2, rel=1e-5) 

def test_dual_tangent():
    x1 = Dual(math.pi/2, 2)
    x2 = Dual(math.pi/4, 2)
    with pytest.raises(ValueError, match="Tangent only defined for the value whose .cos != 0"):
        y1 = x1.tan()

    y2 = x2.tan()
    assert y2.real == pytest.approx(1, rel=1e-5)
    assert y2.dual == pytest.approx(4, rel=1e-5)
