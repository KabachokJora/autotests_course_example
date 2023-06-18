import random


def generate_random_name():
    """
    Генерирует две случайных последовательности букв на латинице длиной до 15 символов в нижнем регистре
    """

    def generate_word():
        """
        Создает случайный набор букв на латинице длиной до 15 символов
        :return: строка длиной до 15 символов
        """
        word_length = random.randint(1, 15)
        word = ''.join(chr(random.randint(ord('a'), ord('z'))) for _ in range(word_length))
        return word

    while True:
        yield f'{generate_word()} {generate_word()}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
