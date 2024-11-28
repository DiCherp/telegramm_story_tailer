import telebot
from telebot import types

bot = telebot.TeleBot('7278512647:AAF37i1OqLvnWad-BNRIqiwj8xx-eq7o6JU')

privetstv = 'привет! я бот, который модет рассказывать истории с нелинейным сюжетом, зависящим от твоих выборов!'
vybor = 'выбери историю, которую хотел бы узнать'





@bot.message_handler(commands=['start'])
def nachalo(message):
    bot.send_message(message.chat.id, privetstv)
    markup = types.InlineKeyboardMarkup()
    story_1 = types.InlineKeyboardButton('Горящее сердце', callback_data='goryaschee_serdce')
    markup.add(story_1)
    bot.send_message(message.chat.id, vybor, reply_markup=markup)

@bot.message_handler(commands=['hello'])
def nachalo(message):
    bot.send_message(message.chat.id, privetstv)
    markup = types.InlineKeyboardMarkup()
    story_1 = types.InlineKeyboardButton('Горящее сердце', callback_data='goryaschee_serdce')
    markup.add(story_1)
    bot.send_message(message.chat.id, vybor, reply_markup=markup)



