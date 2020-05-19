from ctypes import util

from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize
import telegram
import time
from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler


api_key = '1267154414:AAGtzLdN_e_SX4wtrUi8EdQ4rSjyPGLY3Y0'
bot = telegram.Bot(token=api_key)
chat_id = 1172979047
updater = Updater(token='1267154414:AAGtzLdN_e_SX4wtrUi8EdQ4rSjyPGLY3Y0')
dispatcher = updater.dispatcher
updater.start_polling()



bot.sendMessage(chat_id=chat_id, text='안녕! 반가워~ 나는 채팅로봇 김치라고해*^^*')

custom_keyboard = [['심리테스트'], ['타로점'], ['둘다 별로야']]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
bot.send_message(chat_id=chat_id, text="심리테스트랑 타로점은 내 전문이야 !\n "
                                       "원하는 걸 골라봐~", reply_markup=reply_markup)


def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id
    if '심리테스트' in text:
        bot.send_message(chat_id=chat_id, text='좋아! 그럼 내가 주제들을 보여줄게 ~ ')
        reply_markup = telegram.ReplyKeyboardRemove()



echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)