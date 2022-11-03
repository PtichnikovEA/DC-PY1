import random


def get_unique_list_numbers() -> list[int]:
    rand_list = [random.randint(-10, 10) for i in range(0, 15)]  # Создание списка со случайными значениями
    while len(rand_list) != len(set(rand_list)):  # Цикл проверки значечний списка на уникальность
        rand_list = list(set(rand_list))  # Удаление неуникальных значений
        while len(rand_list) < 15:  # Цикл добавления новых значений в список
            rand_list.append(random.randint(-10, 10))
    return rand_list
    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
