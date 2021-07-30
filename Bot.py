import telebot
import Bot2
bot=telebot.TeleBot('1921095688:AAGBKHRe46VwyVs1xknEBXzYTZIGtH5xb0A');
@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)
    
#RUN
bot.polling(none_stop=True)
