#from calculator import Calculator
#
#import pytest
#
#@pytest.fixture
#def calculator():
#    return Calculator()
#
#def test_sum_pos_muns(calculator):
#    assert calculator.sum(1, 6) == 7
#
#@pytest.mark.skip(reason='тест отключен')
#def test_sum_neg_muns(calculator):
#    assert calculator.sum(-1, -2) == -3
#
#def test_div_by_zero(calculator):
#    with pytest.raises(ArithmeticError, match="На ноль делить нельзя"):
#        calculator.div(10,0)
#
#def test_mul_pos_muns(calculator):
#    assert calculator.mul(2, 2) == 4
#@pytest.mark.skipif(condition='sys.version_info < (3, 8)', reason="Требуется Python 3.8")
#


###################
### modificat ##


from calculator import Calculator

import pytest

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize('num1, num2, result', [(4, 5, 9), (2, 8, 10), (11, 0, 11)])
def test_sum_nums(calculator, num1, num2, result):
    res = calculator.sum(num1, num2)
    assert res == result

@pytest.mark.skip(reason='тест отключен')
def test_sum_neg_muns(calculator):
    assert calculator.sum(-1, -2) == -3

@pytest.mark.skipif(condition='sys.version_info < (3, 8)', reason="Требуется Python 3.8")
def test_div_by_zero(calculator):
    with pytest.raises(ArithmeticError, match="На ноль делить нельзя"):
        calculator.div(10,0)

def test_mul_pos_muns(calculator):
    assert calculator.mul(2, 2) == 4






















#from calculator import Calculator
#
#import pytest
#
#@pytest.fixture
#def  calculator():
#    return Calculator()
#
#def test_sum_pas_muns(calculator):
#    assert calculator.sum(1, 2) == 3
#
#def test_sum_neg_muns(calculator):
#    assert calculator.sum(-1, -2) == -3


    ##########################################

 #   from calculator import Calculator
#
 #   import pytest
#
 #   @pytest.fixture
 #   def calculator():
 #       return Calculator()
#
 #   def test_sum_pos_muns(calculator):
 #       assert calculator.sum(1, 2) == 3
#
 #   def test_sum_neg_muns(calculator):
 #       assert calculator.sum(-1, -2) == -3
#







