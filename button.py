import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

my_token = '1184525831:AAGBPIt5EMYsiekswv5tJQ7R2jJnFm8aGII'

chat_id = 1260470636

updater = Updater(token='1184525831:AAGBPIt5EMYsiekswv5tJQ7R2jJnFm8aGII')

bot = telegram.Bot(token=my_token)

updates = bot.getUpdates()

dp = updater.dispatcher

TEST, REALTARO, MENU = range(3)

# 메뉴만들기

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):

    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]

    if header_buttons:

        menu.insert(0, header_buttons)

    if footer_buttons:

        menu.append(footer_buttons)

    return menu


def start(bot, update):
    keyboard = [
        [InlineKeyboardButton(u"test", callback_data=str(TEST))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        u"안녕 나는 타로, 심리 봇이야. 시작하기를 원하면 test 를 눌러",
        reply_markup=reply_markup
    )
    return TEST

#시작메세지전달(타로&심리중에 고르기)
def test(bot, update):
    query = update.callback_query
    print("test")

    show_list = []

    show_list.append(InlineKeyboardButton("타로", callback_data=str(REALTARO)))

    show_list.append(InlineKeyboardButton("심리", callback_data=str(MENU)))

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"원하는 걸 선택하세요."
    )

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=show_markup
    )

    if(update.callback_query==str(REALTARO)) :
        return REALTARO
    else :
        return MENU


def realtaro(bot, update):
    query = update.callback_query
    print("realtaro")

    show_list = []
    show_list.append(InlineKeyboardButton("성격카드", callback_data="생일점"))

    show_list.append(InlineKeyboardButton("오늘의 운세", callback_data="오늘의 운세"))

    show_list.append(InlineKeyboardButton("취소", callback_data="취소"))

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"주제를 보여드리겠습니다."
    )

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=show_markup
    )

    return

#심리테스트선택시 호출되는 함수
def test_menu(bot, update):
    query = update.callback_query
    print(test_menu)

    show_list = []

    show_list.append(InlineKeyboardButton("1.문", callback_data="문"))

    show_list.append(InlineKeyboardButton("2.동물", callback_data="동물"))

    show_list.append(InlineKeyboardButton("3.사진", callback_data="사진"))

    show_list.append(InlineKeyboardButton("4.숫자", callback_data="숫자"))

    show_list.append(InlineKeyboardButton("5.취소", callback_data="취소"))

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"원하는 심리테스트 종료를 선택하시오."
    )

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=show_markup
    )
    return



bot.sendMessage(chat_id=chat_id, text='안녕 나는 타로, 심리 봇이야. 시작하기를 원하면 /start 를 눌러')

conv_handler = ConversationHandler(
       entry_points=[CommandHandler('start', start)],
       states={
           TEST: [CallbackQueryHandler(test)],
           REALTARO: [CallbackQueryHandler(realtaro)],
           MENU: [CallbackQueryHandler(test_menu)]
       },
       fallbacks=[CommandHandler('start', start)]
)

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()

updater.idle()