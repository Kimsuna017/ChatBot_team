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
    show_list.append(InlineKeyboardButton("오늘의 운세", callback_data="오늘의 운세"))
    show_list.append(InlineKeyboardButton("취소", callback_data="취소"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("둘 중 고르세요", reply_markup=show_markup)


def callback_get(bot, update):
    print("callback")
    if update.callback_query.data == "생일점":
        bot.edit_message_text(text="/taro_b 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "오늘의 운세":
        bot.edit_message_text(text="/taro_d 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "심리":
        bot.edit_message_text(text=" /menu 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "타로":
        bot.edit_message_text(text="/realtaro 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "취소":
        bot.edit_message_text(text="취소가 선택되었습니다. 다시 처음으로 돌아가고 싶으면 /test 를 누르세요.".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "혈액형":
        bot.edit_message_text(text=" 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "동물":
        bot.edit_message_text(text="/animal 이 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "색깔":
        bot.edit_message_text(text=" 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)


def test_menu(bot, update):
    print(test_menu)
    bot.sendMessage(chat_id=chat_id, text='원하는 심리테스트 종료를 선택하시오.')
    show_list = []
    show_list.append(InlineKeyboardButton("1.혈액형", callback_data="혈액형"))
    show_list.append(InlineKeyboardButton("2.동물", callback_data="동물"))
    show_list.append(InlineKeyboardButton("3.색깔", callback_data="색깔"))
    show_list.append(InlineKeyboardButton("4.취소", callback_data="취소"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("흥미 있는 주제를 골라줘!", reply_markup=show_markup)


def crawl_animal(bot, update):
    bot.sendMessage(chat_id=chat_id, text='당신이 정글에서 한마리의 야생 동물이 된다면 다음 중 어떤 동물이 되고 싶나요?.\n1.사자\n2.기린')


def taro_b(bot, update):
    print("taro_b")
    t = "태어난 연도, 월, 일을 입력하세요. ex)20000305"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    update.message.reply_text("입력을 마치면 /sum 을 누르세요")


def taro_d(bot, update):
    print("taro_d")
    t = "0부터 22까지 마음에 드는 숫자를 골라보세요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    update.message.reply_text("입력을 마치면 /today 를 누르세요")


def sum(bot, update):
    print("sum")
    dd = solve()
    bot.sendMessage(chat_id=update.message.chat_id, text=str(dd))

    if dd == 10:
        bot.sendMessage(chat_id=update.message.chat_id, text="당신의 성격 카드는 운명의 수레바퀴입니다! 이 카드는 재주있는 사람 어쩌구")
        bot.send_photo(chat_id=update.message.chat_id, photo=open('C:/CookPython/taro10.png', 'rb'))
    # update.message.reply_text("결과를 보려면 /solution 누르세요")
    return dd


def today(bot, update):
    print("today")
    value = today_2()
    if value == '1':
        bot.sendMessage(chat_id=chat_id, text='오늘은 매우 행복한 날이네요!')
        bot.send_photo(chat_id=chat_id, photo=open('C:/DB/picture3.gif', 'rb'))
    elif value == 10:
        bot.sendMessage(chat_id=chat_id, text='오늘은 별로')


def get_message(bot, update):
    text, i, j = update.message.text, 10000000, 0

    if '심리테스트' in text and '심리' in text:
        bot.send_message(chat_id=chat_id, text='/menu 를 입력해주세요')
    elif '타로점' in text and '타로' in text:
        bot.send_message(chat_id=chat_id, text='타로점을 고르셨습니다.')
    elif '사자' in text:
        bot.send_message(chat_id=chat_id,
                         text='사자를 고른 당신은 강한 것 같지만 여린 사람!\n경쟁심이 약한 편이다.\n남의 것을 빼앗는 일은 있을 수 없다.\n항상 평화적이고 여린 마음을 지니고 있어 상대에게 모질게 할 수도 없다.')
    elif '기린' in text:
        bot.send_message(chat_id=chat_id,
                         text='기린을 고른 당신은 분석력과 쟁취심이 강한 사람!\n상대방의 치명적인 약점을 잘 파악한다.\n남을 딛고 일어서는 일에 크게 가책을 느끼지 않고 경쟁이라 생각한다.\n다소 충동적인 면이 있으나 경쟁심이 강해 모든 일을 이겨내는 강인함을 가지고 있다.')
    elif 'A' in text:
        bot.send_message(chat_id=chat_id, text='당신은 아마 소심이!')
    else:
        bot.send_message(chat_id=chat_id, text='잘 모르겠습니다.')

    if (int(update.message.text) > 10000000):
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

    if (int(update.message.text) >= 0 and int(update.message.text) < 9):
        i = update.message.text
        num.insert(0, i)
    elif (int(update.message.text) >= 10 and int(update.message.text) <= 22):
        i = int(update.message.text)
        num.insert(0, i)


def solve():
    k, i, j = 0, 0, 1000
    k = result[0] + result[1] + result[2]
    result2.insert(0, k // 1000)
    k = k % 1000
    result2.insert(1, k // 100)
    k = k % 100
    result2.insert(2, k // 10)
    k = k % 10
    result2.insert(3, k // 1)

    return result2[0] + result2[1] + result2[2] + result2[3]


def today_2():
    return num[0]


def solution(bot, update):
    print("solution")
    dd = solve()

    if dd == 10:
        bot.sendMessage(chat_id=update.message.chat_id, text="당신은 아주 행운아에요")


# 전역
result = [0, 0, 0]
pp = result[0] + result[1] + result[2]
result2 = [0, 0, 0, 0]
dd = result2[0] + result2[1] + result2[2] + result2[3]
num = [0]
value = num[0]

# 메인
if __name__ == '__main__':
    bot.sendMessage(chat_id=chat_id, text='안녕 나는 타로, 심리 봇이야. 시작하기를 원하면 /test 를 눌러')
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CallbackQueryHandler(callback_get))
    dp.add_handler(CommandHandler('realtaro', realtaro))
    dp.add_handler(CommandHandler('taro_b', taro_b))
    dp.add_handler(CommandHandler('sum', sum))
    dp.add_handler(CommandHandler('taro_d', taro_d))
    dp.add_handler(CommandHandler('today', today))
    dp.add_handler(CommandHandler('animal', crawl_animal))
    dp.add_handler(CommandHandler('menu', test_menu))
    dp.add_handler(MessageHandler(Filters.text, get_message))
    updater.start_polling(timeout=3, clean=True)
    updater.idle()