import pytest
from dual_autodiff_cy import Dual
import math

def forward_mode_diff(func, x):
    '''
    A forward mode automatic differentiation method
    
    func:   Objective function, should be constructed by the mathematical operations in class 'Dual'
    x:      A scalar, indicating where you need to differentiate
    return: func derivative value at x
    '''
    x_dual = Dual(x, 1) 
    result = func(x_dual)  
    return result.get_dual()


def test_general_func_diff():
    # ------------ Inclusds: + - * ** / ----------- #
    x = 3
    f1 = lambda x: 2*x*x 
    result1 = forward_mode_diff(f1, x)
    assert result1 == pytest.approx(12, rel=1e-5)

    f2 = lambda x: 2*x.pow(2) 
    result2 = forward_mode_diff(f2, x)
    assert result2 == pytest.approx(12, rel=1e-5)

    f3 = lambda x: x.pow(3) + x*2 
    result3 = forward_mode_diff(f3, x)
    assert result3 == pytest.approx(29, rel=1e-5)

    f4 = lambda x: x.pow(3) - x*2  #
    result4 = forward_mode_diff(f4, x)
    assert result4 == pytest.approx(25, rel=1e-5)
    
    f5 = lambda x: x.pow(3) / (2*x)  #
    result5 = forward_mode_diff(f5, x)
    assert result5 == pytest.approx(3, rel=1e-5)


# ------------ Inclusds: sin, cos, tan ----------- #    
def test_trigo_diff():
    x = math.pi/2
    f = lambda x: x.sin() + x.cos() - (x - math.pi/2).tan()
    result = forward_mode_diff(f, x)
    assert result == pytest.approx(-2, rel=1e-5)

# ------------ Inclusds: exp, log ----------- #    
def test_e_diff():
    x = 1
    f = lambda x: x.exp() + x.log()
    result = forward_mode_diff(f, x)
    assert result == pytest.approx(math.e + 1, rel=1e-5)