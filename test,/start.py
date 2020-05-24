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



def start(bot,upddate):
    bot.send_message(chat_id=chat_id, text='안녕! 나는 너의 심리테스트를 봐줄 심리봇이야><')
    bot.send_message(chat_id=chat_id, text='심리테스트를 보려면 /test 를 눌러줘!')


def test(bot, update):
    bot.send_message(chat_id=chat_id, text='당신의 눈 앞에 5가지 색깔의 다른 문이 있어요.')
    bot.send_message(chat_id=chat_id, text='이중에서 당신의 마음에 드는 문을 한 가지 선택해주세요!')
    bot.send_photo(chat_id=chat_id, photo='https://t1.daumcdn.net/cfile/blog/99C8804E5CB0FCFE0F')



def main():
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, start))
    dp.add_handler(CommandHandler('test', test))
    updater.start_polling()
    updater.idle()