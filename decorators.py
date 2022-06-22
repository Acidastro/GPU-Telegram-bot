def name_cut_price(func):
    """
    Отрезаем от имени лишние значения (цена, количество, состояние и тп)
    """

    def wrapper(line):
        name_cut = ' '.join(line.split()[:2])
        tmp = line[line.find(name_cut) + len(name_cut):]
        for i in tmp:
            if i.isdigit():
                return func(name_cut)
            name_cut += i
        return func(name_cut)

    return wrapper


def name_fix_point(func):
    """
    Убираем точку внутри модели
    """

    def wrapper(line):
        if '.' in line:  # если точка есть в строке
            x = line.find('.')  # положение точки
            if line[x + 2].isdigit():  # если 4 цифры
                line = line[:x] + line[x + 1:]  # просто уберем
            else:
                line = line[:x] + line[x + 1] + '0' + line[x + 2:]  # иначе уберем и добавим в конец ноль
        return func(line)

    return wrapper


def name_fix_tuf(func):
    """
    Ставит пробел после либо перед "TUF"
    """

    def wrapper(line: str):
        if 'tuf' in line.lower():
            x = line.lower().find('tuf')
            if line[x + 3] != ' ':  # если после tuf нет пробела
                line = line[:x + 3] + ' ' + line[x + 3:]
            if line[x - 1] != ' ':  # если перед tuf нет пробела
                line = line[:x] + ' ' + line[x:]
        return func(line)

    return wrapper


def name_space_after_model(func):
    """
    Поставить пробел перед пометкой "adoc" / utwoc / oc если такая есть в названии
    """

    def wrapper(line: str):
        if 'adoc' in line.lower():
            x = line.lower().find('adoc')
            line = line[:x] + ' ' + line[x + 4:]
        if 'utwoc' in line.lower():
            x = line.lower().find('utwoc')
            line = line[:x] + ' ' + line[x + 5:]
        if 'oc' in line.lower():
            x = line.lower().find('oc')
            line = line[:x] + ' ' + line[x:]
        return func(line)

    return wrapper


def price_cut(func):
    def wrapper(line):
        """
        Найти и вернуть цену из строки
        :param line: необработанная строка
        :return: необработанная цена
        """
        cut_price = int(''.join([x for x in line.split()[-1] if x.isdigit()]))
        return func(cut_price)

    return wrapper


def price_change(func):
    def wrapper(price, value=10):
        """
        Изменяет цену на value %
        :param price: начальная цена
        :param value: сколько процентов нужно прибавить
        :return: вернуть новую цену c округлением в большую сторону последних двух знаков
        """
        new_price = int(price + (price / 100) * value)
        new_price = round(new_price, -2)
        return func(new_price)

    return wrapper
