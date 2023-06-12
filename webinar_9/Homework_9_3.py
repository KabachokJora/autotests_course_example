# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path

path_to_folder = Path('test_file')

with open(path_to_folder / 'task_3.txt', mode='r', encoding='utf-8') as file:
    purchase_list = []
    purchase = 0

    for item in file:
        if item != '\n':
            purchase += int(item)
        else:
            purchase_list.append(purchase)
            purchase = 0

    three_most_expensive_purchases = sum(sorted(purchase_list)[-3:])

assert three_most_expensive_purchases == 202346
print('Все ок')
