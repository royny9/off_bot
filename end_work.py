import os 
import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_mess(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('turn off computer🖥️')
    btn2 = types.KeyboardButton('restart a computer🔄')
    btn3 = types.KeyboardButton('sleep mode💤')
    
    markup.add(btn1,btn2,btn3)
    
    bot.send_message(message.chat.id,'Choose what you need',reply_markup=markup)


@bot.message_handler(content_types='text')
def reply_message(message):
    try:
        if message.text == 'turn off computer🖥️':
            bot.send_message(message.chat.id, 'your computer will be turned off in 1 minute')
            os.system('shutdown -s -t 60') 
        if message.text == 'restart a computer🔄':
            bot.send_message(message.chat.id, 'your computer will restart in 1 minute')
            os.system('shutdown -r -t 60')
        if message.text == 'sleep mode💤':
            bot.send_message(message.chat.id, 'your computer will be sent to sleep')
            os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')
    except Exception as e:
        print(repr(e))
        
bot.polling(non_stop=True, interval=0)



