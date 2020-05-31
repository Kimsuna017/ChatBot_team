import telegram
import time
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
    if dd == 1 :
        bot.sendMessage(chat_id=chat_id, text = "")
    elif dd == 10 :
        bot.sendMessage(chat_id=update.message.chat_id, text = "당신의 성격 카드는 운명의 수레바퀴입니다! 이 카드는 재주있는 사람 어쩌구")
        bot.send_photo(chat_id=update.message.chat_id, photo=open('C:/CookPython/taro10.png', 'rb'))

    return dd

def today(bot, update):
    print("today")
    value = today_2()
    if value == '1' :
        bot.sendMessage(chat_id = chat_id, text='오늘은 매우 행복한 날이네요!')
        bot.send_photo(chat_id = chat_id, photo=open('C:/DB/picture3.gif','rb'))
    elif value == 10 :
        bot.sendMessage(chat_id = chat_id, text= '오늘은 별로')

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


def today_2() :
    return num[0]

def solution(bot, update):
    print("solution")
    dd = solve()

    if dd == 10 :
        bot.sendMessage(chat_id=update.message.chat_id, text = "당신은 아주 행운아에요")



def callback_get(bot, update):
    print("callback")
    if update.callback_query.data == "생일점":
        bot.edit_message_text(text="/taro_b 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "오늘의 운세":
        bot.edit_message_text(text="/taro_d 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "심리":
        bot.edit_message_text(text=" /menu 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "타로":
        bot.edit_message_text(text="/realtaro 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "취소":
        bot.edit_message_text(text="취소가 선택되었습니다. 다시 처음으로 돌아가고 싶으면 /test 를 누르세요.".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "문":
        bot.edit_message_text(text=" /door 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "동물":
        bot.edit_message_text(text="/animal 이 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "사진":
        bot.edit_message_text(text=" /picture 가 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
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

def test_menu(bot, update):
    print(test_menu)
    bot.sendMessage(chat_id=chat_id, text ='원하는 심리테스트 종료를 선택하시오.')
    show_list = []
    show_list.append(InlineKeyboardButton("1.문", callback_data="문"))
    show_list.append(InlineKeyboardButton("2.동물", callback_data="동물"))
    show_list.append(InlineKeyboardButton("3.사진", callback_data="사진"))
    show_list.append(InlineKeyboardButton("4.취소", callback_data="취소"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("흥미 있는 주제를 골라줘!", reply_markup=show_markup)

#동물관련 심리테스트
def crawl_animal(bot, update):
    bot.sendMessage(chat_id= chat_id, text= '당신이 정글에서 한마리의 야생 동물이 된다면 다음 중 어떤 동물이 되고 싶나요?.\n1.사자\n2.기린')

#문관련 심리테스트
def door(bot, update):
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
    update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 /door 를 누르고 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

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
    update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 /door 를 누르고 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

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
    update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 /door 를 누르고 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

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
    update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 /door 를 누르고 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

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
    update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 /door 를 누르고 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

#사진 관련 심리테스트
def picture(bot, update):
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
    update.message.reply_text("또 다른 결과가 보고싶다면 /picture 를 눌러주세요")

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

def get_message( bot, update):
    text, i , j = update.message.text , 10000000, 0


    if '심리테스트' in text and '심리' in text:
        bot.send_message(chat_id=chat_id, text='/menu 를 입력해주세요')
    elif '타로점' in text and '타로' in text:
        bot.send_message(chat_id=chat_id, text='타로점을 고르셨습니다.')
    elif '사자' in text:
        bot.send_message(chat_id=chat_id,
                                 text='사자를 고른 당신은 강한 것 같지만 여린 사람!\n경쟁심이 약한 편이다.\n남의 것을 빼앗는 일은 있을 수 없다.\n항상 평화적이고 여린 마음을 지니고 있어 상대에게 모질게 할 수도 없다.')
    elif '기린' in text:
        bot.send_message(chat_id=chat_id, text='기린을 고른 당신은 분석력과 쟁취심이 강한 사람!\n상대방의 치명적인 약점을 잘 파악한다.\n남을 딛고 일어서는 일에 크게 가책을 느끼지 않고 경쟁이라 생각한다.\n다소 충동적인 면이 있으나 경쟁심이 강해 모든 일을 이겨내는 강인함을 가지고 있다.')
    elif 'A' in text:
        bot.send_message(chat_id=chat_id, text='당신은 아마 소심이!')
    else:
        bot.send_message(chat_id=chat_id, text='잘 모르겠습니다.')


    if (int(update.message.text)>10000000) :
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

    if (int(update.message.text)>= 0 and int(update.message.text)<9) :
        i = update.message.text
        num.insert(0, i)
    elif (int(update.message.text) >= 10 and int(update.message.text) <= 22):
        i = int(update.message.text)
        num.insert(0, i)


# 전역
result = [0,0,0]
pp = result[0]+result[1]+result[2]
result2 = [0,0,0,0]
dd= result2[0]+result2[1]+result2[2]+result2[3]
num = [ 0]
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
    dp.add_handler(CommandHandler('door', door))
    dp.add_handler(CommandHandler('green', green))
    dp.add_handler(CommandHandler('blue', blue))
    dp.add_handler(CommandHandler('red', red))
    dp.add_handler(CommandHandler('purple', purple))
    dp.add_handler(CommandHandler('grey', grey))
    dp.add_handler(CommandHandler('picture', picture))
    dp.add_handler(CommandHandler('A', A))
    dp.add_handler(CommandHandler('B', B))
    dp.add_handler(CommandHandler('C', C))
    dp.add_handler(CommandHandler('D', D))
    dp.add_handler(MessageHandler(Filters.text, get_message))
    updater.start_polling(timeout=3, clean=True)
    updater.idle()