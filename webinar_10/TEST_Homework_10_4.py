# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('class_time')
class TestMy:

    def test_1(self, function_time):
        time.sleep(3)
        assert all_division(1, 2) == 0.5

    def test_2(self, function_time):
        time.sleep(2)
        assert all_division(0, 2, 5) == 0

    def test_3(self):
        assert all_division(10, 5, 0.25) == 8

    def test_4(self):
        assert all_division(1) == 1

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            assert all_division(1, 0, 3)
