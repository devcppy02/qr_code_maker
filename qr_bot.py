import telebot
import qrcode


bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'a bot that creates a qr code from a link\nclick to generate qr code /qr_code')


@bot.message_handler(commands=['qr_code'])
def qr(message):
    bot.send_message(message.from_user.id, 'send what to convert into qr code')
    bot.register_next_step_handler(message, create)


def create(message):
    data = message.text
    img = qrcode.make(data)
    img.save('res.png')

    bot.send_document(message.from_user.id, document = open('res.png', 'rb')) 

bot.polling(non_stop=True)