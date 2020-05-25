# cmd_handler_bot.py
from datetime import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import CommandHandler

BOT_TOKEN = '1162111643:AAEPZuDg6Ecxn515KYhLGG8yMHFoHvE76R0'

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


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


def get_message(update, context):
    text = update.message.text
    chat_id = update.message.chat_id

    if '심리테스트' in text:
        context.bot.send_message(chat_id=chat_id, text='/menu를 입력해주세요')
    elif '타로점' in text:
        context.bot.send_message(chat_id=chat_id, text='타로점을 고르셨습니다.')
    elif '사자' in text:
        context.bot.send_message(chat_id=chat_id, text='사자를 고른 당신은 강한 것 같지만 여린 사람!\n경쟁심이 약한 편이다.\n남의 것을 빼앗는 일은 있을 수 없다.\n항상 평화적이고 여린 마음을 지니고 있어 상대에게 모질게 할 수도 없다.')
    elif '기린' in text:
        context.bot.send_message(chat_id=chat_id, text='기린을 고른 당신은 분석력과 쟁취심이 강한 사람!\n상대방의 치명적인 약점을 잘 파악한다.\n남을 딛고 일어서는 일에 크게 가책을 느끼지 않고 경쟁이라 생각한다.\n다소 충동적인 면이 있으나 경쟁심이 강해 모든 일을 이겨내는 강인함을 가지고 있다.')
    elif 'A' in text:
        context.bot.send_message(chat_id=chat_id, text='당신은 아마 소심이!')
    else:
        context.bot.send_message(chat_id=chat_id, text='잘 모르겠습니다.')




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
            crawl_animal(update, context)

        context.bot.send_message(
            chat_id=update.effective_chat.id
            , text='[{}] 작업을 완료하였습니다.'.format(data)
        )


def crawl_blood(update, context):
    #time.sleep(5)

    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id=update.effective_user.id
        , action=ChatAction.TYPING
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id
        , text='[{}] 당신의 혈액형은?.\n1.A형\n2.B형'.format(data)
    )


def crawl_animal(update, context):
    # time.sleep(5)

    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id=update.effective_user.id
        , action=ChatAction.TYPING
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id
        , text='[{}] 당신이 정글에서 한마리의 야생 동물이 된다면 다음 중 어떤 동물이 되고 싶나요?.\n1.사자\n2.기린'.format(data)
    )




menu_handler  = CommandHandler('menu', cmd_task_buttons)
message_handler  = MessageHandler(Filters.text, get_message)
button_callback_handler = CallbackQueryHandler(cb_button)

dispatcher.add_handler(menu_handler )
dispatcher.add_handler(message_handler )
dispatcher.add_handler(button_callback_handler)

updater.start_polling()
updater.idle()
