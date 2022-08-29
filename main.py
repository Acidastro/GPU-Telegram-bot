import preprocessing
from product_line import ProductLine
from preprocessing import string_with_slash_for_main
"""
Берет данные с блокнота, выполняет основную программу, печатает результат в консоль.
"""


# получение файла из блокнота
def received_data():
    """
    Получает текстовый файл, разбивает его на строки
    :return: возвращает список строк
    """
    with open('data.txt', 'r', encoding='utf-8') as data:
        return data.readlines()


# создание списка из множества строк
def give_line(data: str):
    lines = [str(x).strip() for x in data]
    return string_with_slash_for_main(lines)


# печать в консоль всей программы
def print_in_console(data):
    """
    Выводит строковое представление в консоль
    Если ловит ошибку, печатает изначальную строку
    Пустые строки не печатает
    Переключатель LHR дает понять с какого словаря брать значение для DictGpu
    """
    for i in data:
        if i:
            try:
                print(ProductLine(i))
            except ValueError:
                print(i)


if __name__ == '__main__':
    a = give_line(received_data())
    print_in_console(a)
