import telebot
from product_line import ProductLine
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('5399787412:AAGasF5jdC21g2N-FpvFCVgE7dpyZI_7nls')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
  #  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  #  item1 = types.KeyboardButton('')  # USDT
  #  item2 = types.KeyboardButton('')  # RUB
  #  item3 = types.KeyboardButton('')  # MHS
  #  markup.add(item1)
  #  markup.add(item2)
  #  markup.add(item3)
    bot.send_message(m.chat.id, 'Я на связи. Я умею преобразовывать прайс')
    bot.send_message(m.chat.id, 'Для того, что бы всё получилось как нужно:\n'
                                '1. Каждая позиция должна быть на отдельной строке\n'
                                '2. Цена должна быть в юанях и быть в конце строки\n'
                                '3. Мегахеш указывается для карт без LHR,\n'
                                '4. Добавь слово "LHR" что бы изменить настройки ')
                 #    reply_markup=markup)


# Получение сообщений от юзера и обратный ответ
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Принято')
    bot.send_message(message.chat.id, transformation(message.text))


# Преобразование входящих строк, выполнение основной программы
def transformation(lines):
    """
    Ф берет на вход все строки с бота,
    Выполняет основную программу с каждой из них по очереди
    Склеиваем строку воедино, для того, что бы ответ был в одном сообщении
    :param lines: На вход принимаем Строки разделенные символом '\n'
    :return: Одна длинная строка разделенная '\n'
    """
    LHR = False  # переключатель lhr
    my_strings = ''  # здесь будет вся строка
    for line in lines.split('\n'):  # итерируем входящие строки
        if line:  # пустые пропускам
            try:
                my_strings += str(ProductLine(line, LHR)) + '\n'  # выполняем основную программу
            except ValueError:  # отлов невалидных строк
                if 'lhr' in line.lower():  # переключаем lhr
                    LHR = True
                my_strings += str(line) + '\n'  # если невалидная оставляем как было
    return my_strings


# Запускаем бота
bot.polling(none_stop=True, interval=0)
