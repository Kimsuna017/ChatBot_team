import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

my_token = '1173273675:AAGqVv9pWGhbqe4FKdbj_u8yJp92gAU_em8'
chat_id = 1132917740
updater = Updater(token ='1173273675:AAGqVv9pWGhbqe4FKdbj_u8yJp92gAU_em8')
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
dp = updater.dispatcher

for u in updates :
    print(u.message)



#메뉴만들기
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def test(bot, update):
    print("test")
    t = "원하는 걸 선택하세요."
    bot.sendMessage(chat_id = update.message.chat_id, text = t)
    show_list = []
    show_list.append(InlineKeyboardButton("생일점", callback_data="생일점"))
    show_list.append(InlineKeyboardButton("취소", callback_data="취소"))
    show_markup =InlineKeyboardMarkup(build_menu(show_list, len(show_list)-1))
    update.message.reply_text("둘 중 고르세요", reply_markup = show_markup)


def callback_get(bot, update):

    print("callback")
    if update.callback_query.data == "생일점":
        bot.edit_message_text(text="/taro 가 선택되었습니다".format(update.callback_query.data),   chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)

    if update.callback_query.data == "취소":
        bot.edit_message_text(text="취소가 선택되었습니다".format(update.callback_query.data),chat_id=update.callback_query.message.chat_id,message_id=update.callback_query.message.message_id)

def taro(bot, update) :

    print("taro")
    t = "탄생연도 끝 2자리를 입력하세요"
    bot.sendMessage(chat_id = update.message.chat_id, text = t)
    #result[0] = calculate(update, a)
    update.message.reply_text("입력을 마치면 /taro1 을 누르세요")
    result[0] = get_message(update)

def taro1(bot, update) :

    print("taro1")
    t = "탄생월 끝 2자리를 입력하세요"
    bot.sendMessage(chat_id = update.message.chat_id, text = t)
    update.message.reply_text("입력을 마치면 /taro2 을 누르세요")
    result[1] = get_message1(update)


def taro2(bot, update) :

    print("taro2")
    t = "탄생일 끝 2자리를 입력하세요"
    bot.sendMessage(chat_id = update.message.chat_id, text = t)
    update.message.reply_text("입력을 마치면 /sum 을 누르세요")
    result[2] = get_message2(update)


def get_message( update) :
    update.message.reply_text(update.message.text)
    a = int(update.message.text)
    return a

def get_message1( update) :
    update.message.reply_text(update.message.text)
    a = int(update.message.text)
    return a

def get_message2( update) :
    update.message.reply_text(update.message.text)
    a = int(update.message.text)
    return a

def sum(update) :
    print("sum")
    t = "아니"
    update.sendMessage(chat_id=update.message.chat_id, text = "아니")
    #sum = py()

def py() :
    sum = result[0]+result[1]+result[2]
    return sum

#전역
result = []
sum
#메인
if __name__=='__main__':
    bot.sendMessage(chat_id = chat_id , text ='안녕 나는 타로, 심리 봇이야. 시작하기를 원하면 /test 를 눌러')
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CallbackQueryHandler(callback_get))
    dp.add_handler(CommandHandler('taro', taro))
    dp.add_handler(CommandHandler('taro1', taro1))
    dp.add_handler(CommandHandler('taro2', taro2))
    dp.add_handler(CommandHandler('sum', sum))
    dp.add_handler(MessageHandler(Filters.text, get_message))
    dp.add_handler(MessageHandler(Filters.text, get_message1))
    dp.add_handler(MessageHandler(Filters.text, get_message2))
    updater.start_polling()
    updater.idle()