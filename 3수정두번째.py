from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize
import time
from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler

updater = Updater(token='1162111643:AAEPZuDg6Ecxn515KYhLGG8yMHFoHvE76R0')
dispatcher = updater.dispatcher
updater.start_polling()


def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    if '심리테스트' in text:
        bot.send_message(chat_id=chat_id, text='다음 중 심리테스트 종류를 고르시오.')
    elif '타로점' in text:
        bot.send_message(chat_id=chat_id, text='타로점을 고르셨습니다.')
    else:
        bot.send_message(chat_id=chat_id, text='잘 모르겠습니다.')


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)


updater = Updater(token='1162111643:AAEPZuDg6Ecxn515KYhLGG8yMHFoHvE76R0', use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


#메뉴나오게하기

def cmd_task_buttons(update, context):
    task_buttons = [[
        InlineKeyboardButton('1.혈액형', callback_data=1)
        , InlineKeyboardButton('2.동물', callback_data=2)
        , InlineKeyboardButton('3.색깔', callback_data=3)
    ], [
        InlineKeyboardButton('4.취소', callback_data=4)
    ]]

    reply_markup = InlineKeyboardMarkup(task_buttons)

    context.bot.send_message(
        chat_id=update.message.chat_id
        , text='원하는 심리테스트 종류를 선택하시오.'
        , reply_markup=reply_markup
    )


def cb_button(update, context):
    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id=update.effective_user.id
        , action=ChatAction.TYPING
    )

    if data == '4':
        context.bot.edit_message_text(
            text='취소되었습니다.'
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )
    else:
        context.bot.edit_message_text(
            text='[{}] 잠시만 기다려주세요.'.format(data)
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )

        if data == '1':
            crawl_blood()
        elif data == '2':
            crawl_animal()

        context.bot.send_message(
            chat_id=update.effective_chat.id
            , text='[{}] 작업을 완료하였습니다.'.format(data)
        )


def crawl_blood():
    time.sleep(5)
    print('혈액형 심테하게 하기.')


def crawl_animal():
    time.sleep(5)
    print('동물 심테하게 하기.')


task_buttons_handler = CommandHandler('test', cmd_task_buttons)
button_callback_handler = CallbackQueryHandler(cb_button)

dispatcher.add_handler(task_buttons_handler)
dispatcher.add_handler(button_callback_handler)

updater.start_polling()
updater.idle()
