import pytest
from app.calc import Calculator


class TestOperation:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_subtracting_success(self):
        assert self.calc.subtracting(3, 1) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown_method(self):
        print("Выполнение метода Teardown")
