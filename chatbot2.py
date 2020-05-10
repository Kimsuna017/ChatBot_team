import telegram   #텔레그램 모듈을 가져옵니다.
from telegram.ext import Updater, MessageHandler, Filters  # import modules

my_token = '1184525831:AAGXQ9-Es5COmMc8TSjV3Z6EWGHy3efjyUI'   #토큰을 변수에 저장합니다.

bot = telegram.Bot(token = my_token)   #bot을 선언합니다.

updates = bot.getUpdates()  #업데이트 내역을 받아옵니다.

for u in updates :   # 내역중 메세지를 출력합니다.
    print(u.message)



print('start telegram chat bot')


# message reply function
def get_message(bot, update):
    if update.message.text=="안녕" :
        update.message.reply_text(update.message.text)
        update.message.reply_text("타로점 볼래?")

def get_message1(bot, update):
    if ((update.message.text=="응") or (update.message.text=="그래") or (update.message.text=="좋아")):
        update.message.reply_text("생년, 월, 일을 말해줘")
        update.message.reply_text("2000 05 08 이런 식으로!")



updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

message_handler1 = MessageHandler(Filters.text, get_message1)
updater.dispatcher.add_handler(message_handler1)


updater.start_polling(timeout=3, clean=True)
updater.idle()