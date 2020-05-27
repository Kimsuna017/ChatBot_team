import telegram
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

my_token = '1267154414:AAGtzLdN_e_SX4wtrUi8EdQ4rSjyPGLY3Y0'
chat_id = 1172979047
updater = Updater(token ='1267154414:AAGtzLdN_e_SX4wtrUi8EdQ4rSjyPGLY3Y0')
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
dp = updater.dispatcher

for u in updates :
    print(u.message)


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def test(bot, update):
    print("test")
    t = "당신의 눈앞에 5가지 색깔 문이 있어요." + "\n" + "이 중에서 당신의 마음에 드는 문을 한가지 선택해주세요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    show_list = []
    show_list.append(InlineKeyboardButton("초록", callback_data="초록"))
    show_list.append(InlineKeyboardButton("파랑", callback_data="파랑"))
    show_list.append(InlineKeyboardButton("빨강", callback_data="빨강"))
    show_list.append(InlineKeyboardButton("보라", callback_data="보라"))
    show_list.append(InlineKeyboardButton("회색", callback_data="회색"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("어떤 문이 가장 마음에 드나요?", reply_markup=show_markup)


def callback_get(bot, update):
    print("callback")
    if update.callback_query.data == "초록":
        bot.edit_message_text(text="/green 을 선택했네요! 결과가 보고 싶으면 클릭~".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "파랑":
        bot.edit_message_text(text="/blue 을 선택했네요! 결과가 보고 싶으면 클릭~".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "빨강":
        bot.edit_message_text(text="/red 를 선택했네요! 결과가 보고 싶으면 클릭~".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "보라":
        bot.edit_message_text(text="/purple 을 선택했네요! 결과가 보고 싶으면 클릭~".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "회색":
        bot.edit_message_text(text="/grey 를 선택했네요! 결과가 보고 싶으면 클릭~".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)


def green(bot, update):
    print("green")
    t = "초록 문을 선택한 당신은" + "\n" + "뛰어난 관찰력과 의사소통 능력으로 사람들 사이에서 중재자 역할을 담당하는 밝은 성격의 소유자에요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "주변사람들을 잘 챙기고 힘이 되어주며 쾌활하고 밝은 에너지를 가지고 있어요!" + "\n" + "또한 타인의 고민을 잘 들어주고 공감해 주기도 하죠"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "하지만 새로운 변화를 좋아하지 않고" + "\n" + "선택이나 결정을 쉽게 하지 못하는 우유부단한 성격이 있어요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")

def blue(bot, update):
    print("blue")
    t = "파란 문을 선택한 당신은" + "\n" + "똑똑하고 체계적인 성격의 소유자에요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "온화한 성품을 갖고 있으며 뛰어난 절제력으로 자기관리를 잘하는 사람이죠!" + "\n" + "분석적이며 통찰력을 가지고 있기도해요"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "하지만 비판에 민감하고" + "\n" + "때로는 비관적인 경우가 있으며 완벽주의 성향으로 일을 늦출수 있어요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")

def red(bot, update):
    print("red")
    t = "빨간 문을 선택한 당신은" + "\n" + "빠른 의사결정 능력으로 명쾌하고 시원한 답변을 내리는 해결사 성격의 소유자에요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "즉각적으로 일을 처리하며 주관이 뚜렷하고 개성있는 사람이죠!" + "\n" + "감각적이고 뛰어난 안목을 갖고 있어요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "하지만 참을성이 부족한 편이에요" + "\n" + "때로는 단호한 성격으로 이해 주변 사람이 어려움을 겪는 경우가 있어요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")

def purple(bot, update):
    print("purple")
    t = "보라색 문을 선택한 당신은" + "\n" + "신비로운 매력과 예술 감각을 가진 예술가 성격의 소유자에요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "침착한 성격을 갖고 있으며 풍부한 감수성을 가진 사람이죠!" + "\n" + "뛰어난 관찰력으로 다양하고 폭넓은 아이디어 뱅크에요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "하지만 예민한 성격도 가지고 있어요" + "\n" + "다소 변덕스럽고 감정기복이 심해 쉽게 흥분할 수가  있어요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")

def grey(bot, update):
    print("grey")
    t = "회색 문을 선택한 당신은" + "\n" + "매사에 신중하고 뛰어난 분별력을 가진 성격의 소유자에요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "성실한 성격을 가지고 있는 사람이죠!" + "\n" + "평화주의자로 매사에 균형을 유지하고 세련된 취향을 가지고 있어요."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.7)
    t = "하지만 소심한 부분이 있고" + "\n" + "때로는 자기중심적으로 비춰질때가 있고 우유부단하며 의존적인 면이 있어요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")




# 메인
if __name__ == '__main__':
    bot.sendMessage(chat_id=chat_id, text='안녕 나는 타로, 심리 봇이야. 시작하기를 원하면 /test 를 눌러')
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CallbackQueryHandler(callback_get))
    dp.add_handler(CommandHandler('green', green))
    dp.add_handler(CommandHandler('blue', blue))
    dp.add_handler(CommandHandler('red', red))
    dp.add_handler(CommandHandler('purple', purple))
    dp.add_handler(CommandHandler('grey', grey))
    updater.start_polling(timeout=3, clean=True)
    updater.idle()

