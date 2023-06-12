# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path

path_to_folder = Path('test_file')

with open(path_to_folder / 'task1_data.txt', encoding='utf-8') as file:
    file_strings = file.readlines()
    for line in file_strings:
        magic_string = ''.join([symbol for symbol in line if not symbol.isdigit()])
        with open(path_to_folder / 'task1_answer.txt', mode='a', encoding='utf-8') as answer_file:
            answer_file.write(magic_string)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
