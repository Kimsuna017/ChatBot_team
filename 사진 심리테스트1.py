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
    t = "가장 마음에 드는 그림을 선택하세요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    bot.send_photo(chat_id=update.message.chat_id, photo='https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F998D84385B6B27D52D')
    show_list = []
    show_list.append(InlineKeyboardButton("A", callback_data="A"))
    show_list.append(InlineKeyboardButton("B", callback_data="B"))
    show_list.append(InlineKeyboardButton("C", callback_data="C"))
    show_list.append(InlineKeyboardButton("D", callback_data="D"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("힘들 때 당신이 가장 많이 의지하는 것에 대한 테스트입니다!", reply_markup=show_markup)


def callback_get(bot, update):
    print("callback")
    if update.callback_query.data == "A":
        bot.edit_message_text(text="/A 를 클릭해주세요.".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "B":
        bot.edit_message_text(text="/B 를 클릭해주세요.~".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "C":
        bot.edit_message_text(text="/C 를 클릭해주세요.".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "D":
        bot.edit_message_text(text="/D 를 클릭해주세요.".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)



def A(bot, update):
    print("A")
    t = "힘들 때 당신이 가장 많이 의지하는 것은 <연인> 이에요"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "지금 여인이 없다면," + "\n" + "연애를 원하는 이유가 의지하고 싶은 마음 때문입니다."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "A를 선택한 사람의 특징은" + "\n" + "무엇보다 감정을 중요하게 생각하는 편으로,"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "연인에게 가장 바라는 점은 당신의 감정을 잘 알아주길 바란답니다!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")

def B(bot, update):
    print("B")
    t = "힘들 때 당신이 가장 많이 의지하는 것은 <자기자신> 이에요"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "의지라기 보다는 스스로에 대한 믿음이 강하다는 표현이 더 어울리네요~"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "B를 선택한 사람들의 특징은" + "\n" + "무척이나 강인한 정신력을 가지고 있어서" + "\n" + "어떠한 일도 스스로 해결하고자 하는 마음이 큽니다."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "따라서 힘든 상황에 놓여도 주변에 절대로 티를 내지 않는 타입입니다!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "아주 이상적인 타입이긴 하지만 왠지 좀 쓸쓸해보이기도 합니다."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")

def C(bot, update):
    print("C")
    t = "힘들 때 당신이 가장 많이 의지하는 것은 <꿈! 미래! 희망!> 이에요"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "지금 당장의 고통은 더 행복한 미래를 위해" + "\n" + "어쩔 수 없다고 생각하는 긍정적인 마음을 가지고 있습니다."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "C를 선택한 사람들의 특징은" + "\n" + "미래에 대한 구체적인 계획을 가지고 있다는 점인데요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "그렇기 때문에 어렵고 힘든 시간이 찾아와도" + "\n" + "흔들림 없이 꿈을 향해 나아갈 수 있습니다"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")

def D(bot, update):
    print("D")
    t = "힘들 때 당신이 가장 많이 의지하는 것은 <친구> 입니다"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "주변에 진정한 친구가 많기 때문에" + "\n" + "어려울 때 친구들이 먼저 생각납니다."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "진정한 친구가 많다는 것은" + "\n" + "그만큼 훌륭한 대인관계를 유지하고 있다는 뜻인데요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(0.5)
    t = "당신은 어렵고 힘든 일을 겪을 때 " + "\n" + "도움의 손길을 먼저 내밀어 줄 친구들에게 많이 의지를 한답니다."
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    time.sleep(1.5)
    update.message.reply_text("또 다른 결과가 보고싶다면 /test 를 눌러주세요")




# 메인
if __name__ == '__main__':
    bot.sendMessage(chat_id=chat_id, text='안녕 나는 타로, 심리 봇이야. 시작하기를 원하면 /test 를 눌러')
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CallbackQueryHandler(callback_get))
    dp.add_handler(CommandHandler('A', A))
    dp.add_handler(CommandHandler('B', B))
    dp.add_handler(CommandHandler('C', C))
    dp.add_handler(CommandHandler('D', D))
    updater.start_polling(timeout=3, clean=True)
    updater.idle()