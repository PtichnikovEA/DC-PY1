# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint


def get_num_list(total=0):
    return [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(0, total)]


pprint(get_num_list(16))
