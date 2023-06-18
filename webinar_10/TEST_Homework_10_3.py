# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args, result',
                         [
                             pytest.param([1, 2], 0.5, marks=pytest.mark.smoke()),
                             pytest.param([0, 2, 5], 0, marks=pytest.mark.smoke()),
                             pytest.param([10, 5, 0.25], 8, marks=pytest.mark.acceptance()),
                             pytest.param([1], 1, marks=pytest.mark.skip('Скипаем тест по заданию')),
                             pytest.param([1, 0], ZeroDivisionError, marks=pytest.mark.negative())

                         ], ids=['test_1', 'test_2', 'test_3', 'test_4', 'test_division_by_zero']
                         )
def test_all_division(args, result):
    try:
        assert all_division(*args) == result
    except Exception as error:
        assert isinstance(error, result)
