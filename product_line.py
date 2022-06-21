class ProductLine:
    USDT_EXCHANGE_RATE = 6.3  # курс доллара к юаню
    RUB_EXCHANGE_RATE = 12.6  # курс юаня к рублю

    def __init__(self, line: str, lhr=False):
        self.line = line  # принятая строка
        self.__name = ''  # имя видеокарты
        self.__price = ''  # конечная стоимость видеокарты
        self.__price_USDT = ''  # Цена в USDT
        self.__price_RUB = ''  # Цена в RUB
        self.__name_model_number = ''  # Номер модели видеокарты
        self.lhr = lhr  # определяет с какого словаря брать информацию о количестве mh

    def __str__(self):
        from dictGpu import DictGpu
        if self.line:
            try:
                if self.lhr:
                    return f'{self.name}, {self.price}, {DictGpu(self.name_model_number.lower()).gpu_mhs_lhr()}'
                return f'{self.name}, {self.price}, {DictGpu(self.name_model_number.lower()).gpu_mhs()}'
            except(ValueError, TypeError):  # отлов невалидных строк
                if 'lhr' in self.line:  # переключаем lhr
                    self.lhr = True
        return self.line

    @property
    def name(self):
        """
        Задать конечное имя для видеокарты
        :return: чистое без ошибок имя
        """
        tmp_name = self.name_fix_point(self.line)
        tmp_name = self.name_cut_price(tmp_name)
        tmp_name = self.name_fix_tuf(tmp_name)
        tmp_name = name_space_after_model(tmp_name)
        return tmp_name

    @staticmethod
    def name_fix_tuf(line: str):
        """
        Ставит пробел после "TUF"
        """
        if 'tuf' in line.lower():
            x = line.lower().find('tuf')
            line = line[:x + 3] + ' ' + line[x + 3:]
        return line

    @staticmethod
    def name_fix_point(line):
        """
        Цель функции:
        Убрать точку из имени видеокарты, добавить ноль четвертой цифрой
        Проверить, если точка находится в середине 4х цифр, то просто убрать её
        Если точка находится между 3х цифр, то добавить четвертой цифрой "0"
        :return:
        """
        if '.' in line:  # если точка есть в строке
            x = line.find('.')  # положение точки
            if line[x + 2].isdigit():  # если 4 цифры
                line = line[:x] + line[x + 1:]  # просто уберем
            else:
                line = line[:x] + line[x + 1] + '0' + line[x + 2:]  # иначе уберем и добавим в конец ноль
        return line

    @staticmethod
    def name_cut_price(line):
        """
        Отрезаем от имени лишние значения (цена, количество, состояние и тп)
        """
        name_cut = ' '.join(line.split()[:2])
        for i in line[line.find(name_cut) + len(name_cut):]:
            if i.isdigit():
                return name_cut
            name_cut += i

    @property
    def name_model_number(self):
        """
        Номер модели должен:
        Состоять из более чем 2 символов,
        Начинаться с цифры
        :return: номер модели видеокарты (прим. 3070ti)
        """
        min_len = 2
        while True:
            name_num = [str(x) for x in self.name if x.isdigit()][0]  # определить первую цифру модели
            for i in self.name[self.name.find(name_num) + 1:] + ' ':  # определить остальные символы до пробела
                if i == ' ':  # если наткнулись на пробел
                    if len(name_num) > min_len:  # имя больше min_len символов
                        return str(name_num)
                    name_num = ''  # не более 3х символов, стереть имя
                    continue  # начать цикл заново
                name_num += i  # добавить символ в имя

    @property
    def price(self):
        price_cut = ProductLine.price_cut(self.line)  # парсим цену
        price_change = ProductLine.price_change(price_cut)  # меняем цену
        return price_change

    @staticmethod
    def price_cut(line):
        """
        Найти и вернуть цену из строки
        :param line: необработанная строка
        :return: необработанная цена
        """
        cut_price = int(''.join([x for x in line.split()[-1] if x.isdigit()]))
        return cut_price

    @staticmethod
    def price_change(price, value=10):
        """
        Изменяет цену на value %
        :param price: начальная цена
        :param value: сколько процентов нужно прибавить
        :return: вернуть новую цену c округлением в большую сторону последних двух знаков
        """
        new_price = int(price + (price / 100) * value)
        new_price = round(new_price, -2)
        return new_price

    @property
    def price_USDT(self):
        """
        Конвертируем Цену в USDT
        :return: usdt price
        """
        return int(self.price / self.USDT_EXCHANGE_RATE)

    @property
    def price_RUB(self):
        """
        Конвертируем Цену в USDT
        :return: usdt price
        """
        return int(self.price * self.RUB_EXCHANGE_RATE)

    @staticmethod
    def is_lhr(line: str):
        """
        Показывает содержит ли строка информацию о наличии LHR
        Если содержит, то эту строку обрабатывать не нужно
        :param line: необработанная строка
        :return: True если есть "LHR"
        """
        if 'lhr' in line.lower():
            return True
        return False


def name_space_after_model(name: str):
    """
    поставить пробел перед пометкой "adoc" если такая есть в названии
    :param name: принимает имя карты
    :return: возвращает имя с пробелом
    """
    if 'adoc' in name.lower():
        name = name[:name.lower().find('adoc')] + ' ' + name[name.lower().find('adoc') + 4:]
    if 'utwoc' in name.lower():
        x = name.lower().find('utwoc')
        name = name[:x] + ' ' + name[x + 5:]
    if 'oc' in name.lower():
        x = name.lower().find('oc')
        name = name[:x] + ' ' + name[x + 2:]
    return name


if __name__ == '__main__':
    a = ''
    while a != 0:
        a = input()
        print(ProductLine(a))
