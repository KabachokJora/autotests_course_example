# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_1():
    assert all_division(1, 2) == 0.5


@pytest.mark.smoke
def test_2():
    assert all_division(0, 2, 5) == 0


@pytest.mark.acceptance
def test_3():
    assert all_division(10, 5, 0.25) == 8


@pytest.mark.acceptance
def test_4():
    assert all_division(1) == 1


@pytest.mark.negative
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(1, 0, 3)
