"""
Все строки должны пройти через предобработку перед выполнением основной программы.
Китайцы записывают одинаковые модели с разными названиями через слэш, нам нужно каждое наименование записать отдельно.
"""
from product_line import ProductLine


def string_with_slash_for_main(lines: list):
    """
    Берет строку, в которой есть слэш, и преобразует её в несколько строк.
    Находит имя и ставит его в начало
    Пересоздает список строк и возвращает его
    """
    new_lines = []
    for line in lines:
        if '/' in line:
            name = ProductLine(line).name  # Найти имя
            if 'tuf' in name.lower():  # Обрезать имя
                name = ' '.join(name.split()[:3])
            else:
                name = ' '.join(name.split()[:2])
            flag = True  # Флаг, который не даст имя первой строке, т.к там оно уже есть
            while '/' in line:  # Пока слэш есть в строке
                if flag:  # Первую добавляем как есть, отрезая от слэшей
                    new_lines.append(line[:line.find('/')])
                    line = line[line.find('/'):]
                    flag = False
                else:  # К остальным добавим в начало имя
                    line = line[1:]
                    if '/' in line:  # Если не последнее, склеить до слэша
                        new_lines.append(name + ' ' + line[:line.find('/')])
                        line = line[line.find('/'):]
                    else:  # Если последнее, склеить до конца
                        new_lines.append(name + ' ' + line)
        else:
            new_lines.append(line)  # Если нет слэша, добавить как есть
    return new_lines
