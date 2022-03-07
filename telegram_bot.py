import telebot
from telebot import types
import kino
import py_mongo_test

token = 'SuperBotToken'
bot = telebot.TeleBot(token)


# keyboard_start = telebot.types.ReplyKeyboardMarkup()
# keyboard_start.row('Привет', 'Пока')

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я помогу тебе найти информацию о фильме. Просто отправь название фильма")


@bot.message_handler(content_types=["text"])
def find_message(message):
    res = py_mongo_test.find_document({'title': message.text.strip()})
    if res is None:
        res_kino = kino.find_movie(message.text)
        if res_kino is None:
            bot.send_message(message.chat.id, f'Сожалею, фильм {message.text} не найден')
        else:
            py_mongo_test.insert_document(res_kino)
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text=f'{res_kino["url"]}', url=res_kino["url"])
            keyboard.add(callback_button)
            bot.send_message(message.chat.id, f'{res_kino["title"]}, {res_kino["year"]}', reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text=f'{res["url"]}', url=res["url"])
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, f'{res["title"]}, {res["year"]}', reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
    # bot.infinity_poling()
