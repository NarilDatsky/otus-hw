"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_of_nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    output = []

    if filter_type == "odd":
        return [num for num in list_of_nums if num % 2 != 0]
    elif filter_type == "even":
        return [num for num in list_of_nums if num % 2 == 0]
    elif filter_type == "prime":
        for num in list_of_nums:
            abbreviated_list = [2] + list(range(3, abs(num), 2))
            for i in abbreviated_list:
                if num % i == 0:
                    break
            else:
                if num != 0:
                    output.append(num)
    else:
        return f"filter_type has no value '{filter_type}'"

    return output
