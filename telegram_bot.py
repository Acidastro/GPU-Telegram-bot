# pip install pyTelegramBotAPI
import telebot
from product_line import ProductLine
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('xxx')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):

    bot.send_message(m.chat.id, 'Я на связи. Я умею преобразовывать прайс')
    bot.send_message(m.chat.id, 'Для того, что бы всё получилось как нужно:\n'
                                '1. Каждая позиция должна быть на отдельной строке\n'
                                '2. Цена должна быть в юанях и быть в конце строки\n'
                                '3. Мегахеш указывается для карт без LHR,\n'
                                '4. Добавь слово "LHR" что бы изменить настройки ')


# Получение сообщений от юзера и обратный ответ
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Принято')
    bot.send_message(message.chat.id, transformation(message.text))


# Преобразование входящих строк, выполнение основной программы
def transformation(lines):
    """
    Ф берет на вход все строки с бота и
    выполняет основную программу с каждой из них по очереди.
    Вклеиваем строку воедино, для того, что бы ответ был в одном сообщении.
    :param lines: На вход принимаем Строки разделенные символом '\n'
    :return: Одна длинная строка разделенная '\n'
    """
    my_strings = ''  # здесь будет вся строка
    for line in lines.split('\n'):  # итерируем входящие строки
        if line:  # пустые пропускам
            try:
                my_strings += str(ProductLine(line)) + '\n'  # выполняем основную программу
            except ValueError:  # отлов невалидных строк
                my_strings += str(line) + '\n'  # если невалидная оставляем как было
    return my_strings


# Запускаем бота
bot.polling(none_stop=True, interval=0)
