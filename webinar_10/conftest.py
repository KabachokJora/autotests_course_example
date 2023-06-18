import pytest
import datetime


@pytest.fixture(scope='class')
def class_time():
    start_time = datetime.datetime.now()
    print(f'Время старта тестового комплекта: {start_time}')
    yield start_time
    end_time = datetime.datetime.now()
    print(f'\n Окончание прохождения тестового комплекта: {end_time}')


@pytest.fixture()
def function_time():
    start_time = datetime.datetime.now()
    yield start_time
    end_time = datetime.datetime.now()
    print(f'\n Время прохождения теста: {end_time-start_time}')
