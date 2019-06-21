"""
Unit test for the calculator library
"""
import calculator


class test_calculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 4 == calculator.multiply(2, 2)

    def test_division(self):
        assert 4 == calculator.divide(8, 2)
