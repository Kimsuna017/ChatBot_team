import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

my_token = '1173273675:AAGqVv9pWGhbqe4FKdbj_u8yJp92gAU_em8'
chat_id = 1132917740
updater = Updater(token='1173273675:AAGqVv9pWGhbqe4FKdbj_u8yJp92gAU_em8')
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
dp = updater.dispatcher

for u in updates:
    print(u.message)


# 메뉴만들기
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
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    show_list = []
    show_list.append(InlineKeyboardButton("타로", callback_data="타로"))
    show_list.append(InlineKeyboardButton("심리", callback_data="심리"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("둘 중 고르세요", reply_markup=show_markup)


def realtaro(bot, update):
    print("realtaro")
    t = "주제를 보여드리겠습니다."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    show_list = []
    show_list.append(InlineKeyboardButton("생일점", callback_data="생일점"))
    show_list.append(InlineKeyboardButton("취소", callback_data="취소"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("둘 중 고르세요", reply_markup=show_markup)


def callback_get(bot, update):
    print("callback")
    if update.callback_query.data == "생일점":
        bot.edit_message_text(text="/taro 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "심리":
        bot.edit_message_text(text="심리가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "타로":
        bot.edit_message_text(text="/realtaro 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "취소":
        bot.edit_message_text(text="취소가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)


def taro(bot, update):
    print("taro")
    t = "태어난 연도, 월, 일을 입력하세요. ex)20000305"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    update.message.reply_text("입력을 마치면 /sum 을 누르세요")

def sum(bot, update):
    print("sum")
    dd = solve()
    bot.sendMessage(chat_id=update.message.chat_id, text=str(dd))

    if dd == 10 :
        #bot.sendMessage(chat_id=update.message.chat_id, photo=open('C:/Users/dudqh/Pictures/img/taro.10.jpg', 'rb'))
        bot.sendMessage(chat_id=update.message.chat_id, text = "당신의 성격 카드는 운명의 수레바퀴입니다! 이 카드는 재주있는 사람 어쩌구")
    #update.message.reply_text("결과를 보려면 /solution 누르세요")
    return dd

def get_message( bot, update):
    i , j=10000000, 0

    if(int(update.message.text)>10000000) :
        i = int(update.message.text)
        result.insert(0, i // 10000)
        i = int(update.message.text) % 10000000
        i = int(update.message.text) % 1000000
        i = int(update.message.text) % 1000000
        i = int(update.message.text) % 10000
        result.insert(1, i // 100)
        i = int(update.message.text) % 1000
        i = int(update.message.text) % 100
        i = int(update.message.text) % 10
        result.insert(2, i // 1)

def solve():
    k,i, j= 0,0, 1000
    k = result[0]+result[1]+result[2]
    result2.insert(0, k//1000)
    k = k%1000
    result2.insert(1, k // 100)
    k = k%100
    result2.insert(2, k // 10)
    k = k%10
    result2.insert(3, k // 1)

    return result2[0] + result2[1] + result2[2] + result2[3]

def solution(bot, update):
    print("solution")
    dd = solve()

    if dd == 10 :
        bot.sendMessage(chat_id=update.message.chat_id, text = "당신은 아주 행운아에요")




# 전역
result = [0,0,0]
pp = result[0]+result[1]+result[2]
result2 = [0,0,0,0]
dd= result2[0]+result2[1]+result2[2]+result2[3]
# 메인
if __name__ == '__main__':
    bot.sendMessage(chat_id=chat_id, text='안녕 나는 타로, 심리 봇이야. 시작하기를 원하면 /test 를 눌러')
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CallbackQueryHandler(callback_get))
    dp.add_handler(CommandHandler('realtaro', realtaro))
    dp.add_handler(CommandHandler('taro', taro))
    dp.add_handler(CommandHandler('sum', sum))
    dp.add_handler(MessageHandler(Filters.text, get_message))
    updater.start_polling(timeout=3, clean=True)
    updater.idle()