class DictGpu:
    """
    Принимает на вход имя видеокарты, возвращает количество мегахеш, выдаваемое этой картой
    """

    def __init__(self, key: str):
        self.key = key

    def gpu_mhs(self):
        no_lhr_dict = {'3080': 102,
                       '3090ti': 132,
                       '3080ti': 118,
                       '3070ti': 82,
                       '3070': 65,
                       '3060ti': 62,
                       '3060': 50,
                       '3090': 121,
                       '2060s': 44,
                       '2060': 33,
                       '1660s': 33,
                       '1660ti': 29,
                       '598': 30,
                       '30hx': 30,
                       '6900xt': 65,
                       '6800xt': 62,
                       '6800': 63,
                       '6700xt': 47,
                       '6600xt': 33,
                       '6600': 30,
                       '3050': 20,
                       }
        try:
            no_lhr_dict[str(self.key)]
        except KeyError:
            return 0
        return no_lhr_dict[str(self.key)]
