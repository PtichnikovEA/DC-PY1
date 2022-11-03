import string
from random import sample


def get_random_password(n=8) -> str:
    sec_dict = string.ascii_letters + string.digits  # Создание алфавита
    return ''.join(
        sample(sec_dict, n))  # Выборка из алфавита n случайных значений
                                # и преобразование возвращаемого списка в строку
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
