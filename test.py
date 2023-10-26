import pytest
import lib


class Test_Calc:

    @pytest.fixture()
    def plus(self):
        return 21, 21, '+'

    @pytest.fixture()
    def minus(self):
        return 62, 20, '-'

    @pytest.fixture()
    def div(self):
        return 84, 2, '/'

    @pytest.fixture()
    def mult(self):
        return 6, 7, '*'

    def test_1(self, plus):
        assert lib.Calc(*plus) == 42

    def test_2(self, minus):
        assert lib.Calc(*minus) == 42

    def test_3(self, div):
        assert lib.Calc(*div) == 42

    def test_4(self, mult):
        assert lib.Calc(*mult) == 42