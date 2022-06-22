import decorators


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

    def __str__(self):
        from dictGpu import DictGpu
        if self.line:
            try:
                return f'{self.name}, {self.price}, {DictGpu(self.name_model_number.lower()).gpu_mhs()}'
            except(ValueError, TypeError):  # отлов невалидных строк
                return self.line
        return self.line

    @property
    def name(self):
        """
        Задать конечное имя для видеокарты.
        :return: чистое без ошибок имя
        """

        @decorators.name_cut_price
        @decorators.name_fix_tuf
        @decorators.name_space_after_model
        @decorators.name_fix_point
        def new_name(name):
            return name

        return new_name(self.line)

    @property
    def name_model_number(self):
        """
        Номер модели должен:
        Состоять из более чем 2 символов.
        Начинаться с цифры.
        :return: номер модели видеокарты (прим. 3070ti)
        """
        min_len = 2
        while True:
            name_num = [str(x) for x in self.name if x.isdigit()][0]  # определить первую цифру модели
            for i in self.name[self.name.find(name_num) + 1:] + ' ':  # определить остальные символы до пробела
                if i == ' ':  # если наткнулись на пробел
                    if len(name_num) > min_len:  # имя больше min_len символов
                        return str(name_num)
                    name_num = ''  # не более 3-х символов, стереть имя
                    continue  # начать цикл заново
                name_num += i  # добавить символ в имя

    @property
    def price(self):

        @decorators.price_cut
        @decorators.price_change
        def new_price(price):
            return price

        return new_price(self.line)

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


if __name__ == '__main__':
    a = ''
    while a != 0:
        a = input()
        print(ProductLine(a))
