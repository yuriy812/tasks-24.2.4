import pytest
from app.calc import Calculator


class TestOperation:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtracting_success(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def tearown(self):
        print("Выполнение метода Teardown")
