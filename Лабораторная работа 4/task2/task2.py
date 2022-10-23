def get_count_char(str_):
    dictionary = {}  # TODO посчитать количество каждой буквы в строке в аргументе str_
    for char in str_:
        c = char.lower()  # Приводим символ к нижнему регистру
        if c.isalpha():
            if c in dictionary:
                dictionary[c] += 1  # Если в словаре уже есть такой ключ, то увеличиваем значение на единицу
            else:
                dictionary[c] = 1  # Если в словаре нет такого ключа, то заносим его со значением 1
    return dictionary

def get_percents(dict_):
    dictionary = {}  # TODO посчитать количество каждой буквы в строке в аргументе str_
    sum_ = 0
    for char in dict_:
        sum_ += dict_[char]  # Считаем сумму всех значений в словаре
    for char in dict_:
        dictionary[char] = round(dict_[char]/sum_ * 10000)/100  # Пересчитываем каждое значение с округлением до сотых процента
    return dictionary

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_percents(get_count_char(main_str)))
