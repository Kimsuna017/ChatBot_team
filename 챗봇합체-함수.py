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
    show_list.append(InlineKeyboardButton("성격카드", callback_data="생일점"))
    show_list.append(InlineKeyboardButton("오늘의 운세", callback_data="오늘의 운세"))
    show_list.append(InlineKeyboardButton("취소", callback_data="취소"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("둘 중 고르세요", reply_markup=show_markup)


def taro_b(bot, update):
    print("taro_b")
    t = "태어난 연도, 월, 일을 입력하세요. ex)20000305"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    #update.message.reply_text("입력을 마치면 /sum 을 누르세요")


def taro_d(bot, update):
    print("taro_d")

    t = "0부터 22까지 마음에 드는 숫자를 골라보세요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    update.message.reply_text("입력을 마치면 /today 를 누르세요")


def sum(bot, update):
    print("sum")

    dd = solve()
    bot.sendMessage(chat_id=update.message.chat_id, text=str(dd))

    if dd == 0 or dd == 22:
        bot.send_photo(chat_id=chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648900385?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xznrQu88T7i+4rW7SUoCWhrTO2CrHCON1HbumbfbmzKj15Ish3oECjAndZw4lh7MLQU=&authtoken=6mYNrDp3UNwwAHM+YPfruAI=')
        bot.sendMessage(chat_id=chat_id,
                        text="당신의 성격카드는 '광대' 입니다! 당신은 본성이 자유로운 사람이며, 무거운 삶의 과제를 안고 살지만 단순 소박합니다. 때로는 미숙하고 부주의하다는 평을 들을 수 있으나 하나에 빠지면 열정적으로 몰입합니다!")
    elif dd == 1:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648076832?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x4UprD0hOQp9Fc4yStZAdFF39ZikKmKtPyREkbJRxQ++Fdtp67aMTzL2RqRZGnRe+gU=&authtoken=O9FvP4XpOUH2tbLIv/Wz5gI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '마법사' 입니다! 이 카드는 재주있는 사람을 말하며, 독창적이고 창조적이며 상상력이 뛰어남을 상징합니다. 능수능란한 재주가 있어 꾀를 부려도 남이 잘 알아채지 못합니다!")
    elif dd == 2:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648068640?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IPKf4Hib+AH+h1o8q0T8ugnax4Gxlp43Iw34tqTSQcAbwU=&authtoken=CGx9J1WaRTo0R1oEIxxfygI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '여성 대사제' 입니다! 이 카드는 지혜로운 사람을 말하며, 객관적이며 상황판단을 잘하는 것을 상징합니다. 주로 통찰력있고 직관적으로 행동하지만 사람을 주관적으로 대할 수 있어 상대의 불만을 사기도 합니다. ")
    elif dd == 3:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648048161?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xw0MQxY7FRdkeMIj+dj+WhOVGbbU3LJGa/Mfq7u1y5p0SXUAgUkmolgif+YD3Mok7AU=&authtoken=kUPe8Nj1Oc+hM4vUf4ubhAI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '여제' 입니다! 이 카드는 부드러운 에너지가 발달한 사람을 말하며, 성취지향적이고 실용적입니다. 다른 사람을 돌보고 그들이 잘 성장할 수 있도록 돕고자 합니다!")
    elif dd == 4:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648066593?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IO2TmlykSyYET0FciV5oESxIIc6uddfsRB0n+7A5rRhHgU=&authtoken=nquKjZhDz82JRFoxjBTCkgI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '황제' 입니다! 이 카드는 가장을 상징하며 가진 것을 지키려고 앴는 사람을 말합니다. 세속적인 힘과 안정, 권위, 확신, 이성을 상징합니다. 남성일 경우 가부장적인 인물을 뜻합니다!")
    elif dd == 5:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648068129?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IPEQw4YF2WtrTKcJ+N/PpLkMs1vJw1CdUy+28+HFRADDgU=&authtoken=Os4EJ1FF5PB8VWgYcXqIjQI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '교황' 입니다! 이 카드는 진리를 가르치려는 교육자를 상징하며 주로 자비로우며 동정심이 강합니다. 주관이 뚜렷하며 의식을 중시하고 원칙을 따르려고 합니다. 주로 집단과 행동을 같이하고 지식 획득과 깨달음을 위해 노력합니다!")
    elif dd == 6:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb1.photo.cloud.naver.com/3472427554648105504?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x9ShSmaRXb7sBW8WNRMaArMFoSagtMeIBuBBSQeqMLHwmHqF+WKd2fRzeomdiYBbIgU=&authtoken=rv2nnDEewW0D4s/1CifwrAI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '연인' 입니다! 이 카드는 인간관계를 중시하며 사랑이나 미에 높은 사람을 말합니다. 자신을 꾸미는 능력이 있고 이를 완성시키며 조화를 이루려고 합니다. 깊은 감정을 느끼며, 누군가와 그 정서를 교류하고 싶어합니다.")
    elif dd == 7:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb1.photo.cloud.naver.com/3472427554648196384?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xwCFy3+bnViFK87QgpUWtNWSkggfCMn//0duim9pPKVQcdM8GMuOezdfatKqwz7kkAU=&authtoken=LXNspjA2tUDRI87t/A0+ZAI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '전차' 입니다! 이 카드는 역경극복의 의지를 나타냅니다. 이 카드를 성격카드로 가진 사람은 한 가지에 집중하기 보다는 여러가지 일에 관심을 가지며, 실제로 그 일을 모두 해내는 경향이 있습니다. 그렇기 때문에 마음의 변화에 귀 기울이는 것이 중요합니다.")
    elif dd == 8:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648186912?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x/O/NOEOJ91MV3VlI7ZV8zYu999M/eHsMpJit9QK7ljNQvB8mJ+qvKLSWP+F7OnAVQU=&authtoken=+5oXaVy35z6BixRrINPFOgI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '힘' 입니다! 이 카드는 외유내강형의 사람과 화난 사람을 진정시킬 줄 아는 사람을 말하며, 이 사람들은 주로 내적 용기와 힘, 결단력, 확신, 도전적 태도를 지닙니다. 그러나 내면의 두려움과 맞서야하는 과제를 안고 있습니다.")
    elif dd == 9:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb1.photo.cloud.naver.com/3472427554648369441?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xwuxECnrWUOLyyH8pcx4deGIEgKFduLlU1JG1ySnZKNN0kp7H2KZu7kO/sSi4cRzzQU=&authtoken=XUUidelNiacLIJsgSPNl+AI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '은둔자' 입니다! 이 카드는 관심이 내면에 있는 사람이며 외부대상이나 환경에 신경을 쓰지 않는 편입니다. 감정을 억제하며 사려깊고 신중해 조언하기를 좋아합니다. 행동이 빠르지 않고 고요하며, 간혹 지나치게 침울한 사람도 있습니다.")
    elif dd == 10:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648396320?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7LAGt+TiuzcFNH9TmPqj9+nPtdnxywWVQkb664bqB6sDnFnoXPEj/7UcNa1BFd9YQU=&authtoken=1HKQUhvKXE+W9YUpdpsDnQI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '운명의 수레바퀴' 입니다! 이 카드는 재주있는 사람을 가리키며 행위의 결과가 자신에게 돌아오니 조심성을 가질 필요가 있습니다. 진리라 생각하는 분야를 배워 타인을 위해 가르치거나 공공의 이익을 위해 사용하는 것이 좋습니다.")
    elif dd == 11:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648384800?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7scJk+FDIjkv6Ddkp6ahDSiyYM75K8nJRV6o1SNhIVuFR2vCet/BLB7fIsnLQIK4wU=&authtoken=tcSj8+OVNal234GIN1K3nQI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '정의' 입니다! 이 카드는 공평무사, 균형 그리고 조화를 이루려는 것을 나타냅니다. 이 카드를 성격카드로 지닌 사람은 분별력이 있으며 판단 후에는 실쳔력이 빠르고 올바름, 미덕, 명예를 중시하는 경향이 있습니다. 그러나 대인관계에서도 판단이 앞선 나머지 정서적인 면을 간과할 수 있습니다.")
    elif dd == 12:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648429344?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xzf+M2SA1Ztl99EtXwHfvcFPBl7O03e90XCZr5Vm/ujFrkXxsrfXtW3rx9m35dxJRQU=&authtoken=8MOx387lcXEusGTUxARYawI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '매달린 사람' 입니다! 이 카드를 성격 카드를 지닌 사람은 말과 행동이 느리며 둔감한 편이라 정성적 표현이 부족한 경향이 있습니다. 그러나 내면에서는 많은 것이 일어나기 때문에 인내심을 가지고 지켜볼 필요가 있습니다.")
    elif dd == 13:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648660256?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xyScqqH/p2HWG9MWTceCsJ0KX/vS5TQvlzJepTYlNvvcrndBt8Llh3Qsg25amBmy/QU=&authtoken=EuL9U+1DI0ifh62mGOiPXwI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '죽음' 입니다! 이 카드는 변형을 일으키는 사람을 말합니다. 신체적인 죽음이 아니라 새로운 것을 위해 과거의 것을 과감히 제거하는 사람으로 익수한 상황을 유지하기 보다는 새 상황의 시작을 즐기고 새로움을 추구합니다.")
    elif dd == 14:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb1.photo.cloud.naver.com/3472427554648525600?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xxFGESAG+nBJTJrxNAjnAr/LTJErbFLc+1Y/1pyijcSunU8V+H5AM68RyVdUdiX0kgU=&authtoken=k3tj5fxYm3aS/4hev3IOyQI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '절제' 입니다! 이 카드를 성격 카드로 가진 사람은 자기통제와 검소한 태도를 통해 목표를 달성합니다. 환경에 순응하고 주변과 조화를 이루며 큰 목표를 위해 힘을 합칠 줄 압니다. 그러나 역작용이 일어나면 중독에 빠질 수 있습니다.")
    elif dd == 15:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648549665?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x/CwFMG5TRfXQUr1Pi1jrtOb2rQ9k+OyEJYsOsUBzZcRWMYtjW1safoCUtylRQaDIQU=&authtoken=e3KyM4XsGxDS3cWfIsg4XgI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '악마' 입니다! 이 카드는 집착이 강한 사람을 말하며, 자신과 관련된 대상에 대해 걱정을 많이 합니다. 실패 경험을 너무 오래 생각하면 자신과 주변이 힘들어 질 수 있습니다.")
    elif dd == 16:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648559648?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7pnovZiTrHNOqXu1Kj3FjER2KgDdaqrnGQ7El4HBNfmQV5dlSAboZMLBfpaubJ/GwU=&authtoken=+c8iRU2sztFJufBpZKH+dgI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '탑' 입니다! 이 카드는 변화의 충격으르 강하게 받는 사람을 말하며, 진실을 인식하고 맞지 않는 경우에는 가진 것을 모두 버릴 수 있는 과감함을 지니고 있습니다. 과거 대인 관계를 꾸준히 유지하기 보다 변화를 추구하는 경향이 있습니다.")
    elif dd == 17:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb1.photo.cloud.naver.com/3472427554648692256?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x6ppsN1vzwMg1NU/UROoh6jnPcZn64sccWCkVfSJkJMudgea5K02i4AXUniKqPVWDQU=&authtoken=NwVtFoOR6ei+NTikaOTUkAI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '별' 입니다! 이 카드는 어둠속에 희망의 등불이 되려하는 사람을 말합니다. 주로 사람들에게 힘이 되고 싶어하며 신념이 있고 낙천적, 긍적적입니다. 그러나 그렇기 때문에 현재의 어려운 상황을 간과할 우려가 있습니다.")
    elif dd == 18:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648705568?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x2UoC4cjV5+jbvRWun8/hSuGiXK+yf6X7Tg9DmCLGGg02EZtWRAXJb0vMDKGWkmqfwU=&authtoken=ct9aR2FQ+JVOS7v/x7p11QI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 운명의 '달' 입니다! 이 카드를 성격 카드로 지닌 사람은 마음이 자주 바뀌며 의심이 많습니다. 자신이 너무 순수해 잘 속는다고 생각합니다. 내적 변화를 인정하고 즐기는 방법을 찾는 것이 중요합니다.")
    elif dd == 19:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648756768?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7RS0p5Vi/SPI7N/Pxfn8xtWZZMxLUpUQY5wtL7C/9VmEcWbI0dl8IAuiSpoLk5mVgU=&authtoken=QlZly3qsuRBnc+jTwivzNAI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '태양' 입니다! 이 카드는 어린애처럼 순수한 사람을 말하며, 자신의 역량보다 더 큰 일을 해내는 용기와 믿음이 있습니다. 고생이 많아도 특별한 보살핌 또한 경험했을 가능성이 있으며 이에 대한 감사를 잊으면 안됩니다.")
    elif dd == 20:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648845857?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x70tL5v6OyhRVcVqf1brOzMBFupHaPOhzkFQJoAGAkLZzBHiByx787wf7AvJhd9ABgU=&authtoken=uj7wzCW2j9ejVZgpRn7FpAI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '심판' 입니다! 이 카드는 옳고 그름에 대한 판단이 바르고,정의로운 사람을 말합니다. 희생을 감수해 진리를 드러내고자 하며 억울한 사람을 보면 무심해지기 어려워 적극 개입합니다.")
    elif dd == 21:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb1.photo.cloud.naver.com/3472427554648860961?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x6vWAqAFs8f5zGm0SDoi2q9PezVrDoVJU4tHCrJOgDunNcKfwdHq9CUmjXAacUWU1QU=&authtoken=nOD0cf1XlO4TK0lzgXrp1QI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '세계' 입니다! 이 카드는 어떠한 환경에서도 완성을 이루려는 사람을 말하며 주로 완벽주의자고 시야가 넓습니다. 가족이 도움을 구하면 자기 일처럼 돕습니다. ")
    return dd


def today(bot, update):
    print("today")

    value = today_2()
    if value == '1':
        bot.sendMessage(chat_id=chat_id, text='오늘은 매우 행복한 날이네요!')
        bot.send_photo(chat_id=chat_id, photo=open('C:/DB/picture3.gif', 'rb'))
    elif value == 10:
        bot.sendMessage(chat_id=chat_id, text='오늘은 별로')


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

    if (result2[0] + result2[1] + result2[2] + result2[3] <= 22):
        return result2[0] + result2[1] + result2[2] + result2[3]
    else:
        i = result2[0] + result2[1] + result2[2] + result2[3]
        result2.insert(0, i // 10)
        i = i % 10
        result2.insert(1, i // 1)
        return result2[0] + result2[1]


def today_2():
    return num[0]


def solution(bot, update):
    print("solution")
    dd = solve()

    if dd == 10:
        bot.sendMessage(chat_id=update.message.chat_id, text="당신은 아주 행운아에요")


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
    bot.sendMessage(chat_id=chat_id, text='원하는 심리테스트 종료를 선택하시오.')
    show_list = []
    show_list.append(InlineKeyboardButton("1.문", callback_data="문"))
    show_list.append(InlineKeyboardButton("2.동물", callback_data="동물"))
    show_list.append(InlineKeyboardButton("3.사진", callback_data="사진"))
    show_list.append(InlineKeyboardButton("4.취소", callback_data="취소"))
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))
    update.message.reply_text("흥미 있는 주제를 골라줘!", reply_markup=show_markup)


# 동물관련 심리테스트
def crawl_animal(bot, update):
    bot.sendMessage(chat_id=chat_id, text='이 사진에는 총 9마리의 동물, 곤충 등이 있는데요!')
    bot.send_photo(chat_id=update.message.chat_id, photo='https://pbs.twimg.com/media/DY9aTtFVQAAm2aG.jpg')
    bot.sendMessage(chat_id=chat_id, text='이 중 가장 먼저 떠오르는 동물은 무엇인가요?')


# 문관련 심리테스트

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


# 사진 관련 심리테스트
def picture(bot, update):
    print("test")

    t = "가장 마음에 드는 그림을 선택하세요!"
    bot.sendMessage(chat_id=update.message.chat_id, text=t)
    bot.send_photo(chat_id=update.message.chat_id,
                   photo='https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F998D84385B6B27D52D')

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


def get_message(bot, update):
    text, i, j, uu = update.message.text, 10000000, 0, 0

    if '심리테스트' in text and '심리' in text:
        bot.send_message(chat_id=chat_id, text='/menu 를 입력해주세요')

    elif '타로점' in text and '타로' in text:
        bot.send_message(chat_id=chat_id, text='타로점을 고르셨습니다.')

    elif '말' in text:
        bot.send_message(chat_id=chat_id, text='말은 야망이 강한 사람으로 자유롭고 야생적이며 성공하기 위해 노력하는 타입입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='비록 장애물에 부딪힐 수 있지만 포기하지 않고 꾸준히 노력하는 성향을 가지고 있습니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='또한! 그 성격을 아는 주변 사람들에게 정직한 성격을 가진 이로 신뢰를 받고 있을 것 입니다.')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    elif '닭' in text:
        bot.send_message(chat_id=chat_id, text='닭이 먼저 보였다면 인내심이 강한 타입입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='끈기와 민첩성을 가진 당신은 온순하지 않지만\n당신의 인내심을 깰만한 사람은 별로 없다고 보면 됩니다.')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    elif '꽃게' in text:
        bot.send_message(chat_id=chat_id, text='꽃게를 먼저 본 당신은 무뚝뚝하면서도 속은 부드러운 사람입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='신뢰를 가장 중요시하는 타입으로 진심을 소중히 여기고\n사랑하는 사람들을 먼저 생각 합니다.')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    elif '사마귀' in text:
        bot.send_message(chat_id=chat_id, text='사마귀가 먼저 보였다면 직감같은 감각 자체가 뛰어난 사람입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='누구보다 날카로운 직감을 가진 당신은\n원하는 것을 얻기 위해 마음의 소리에 따라 충동적인 행동을 할 때도 많을 것 입니다.')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    elif '늑대' in text:
        bot.send_message(chat_id=chat_id, text='늑대를 가장 먼저 보았다면\n 당신은 부드러운 외면과 사납지만 용기 있는 내면을 가진 사람입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='용감함을 가지고 있는 당신은\n사람들에게 둘러싸여 있어도 눈에 띄는 존재감!을 가지고 있을 것입니다.')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    elif '강아지' in text:
        bot.send_message(chat_id=chat_id, text='강아지가 먼저 눈에 들어왔다면\n성실하고 지조를 갖춘 사람입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='대개 사려가 깊으며 다정다감한 당신은\n먼저 사람을 잘 돕고 늘 주변을 위한 성격으로 인기가 많은 타입입니다.')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    elif '매' in text:
        bot.send_mesage(chat_id=chat_id, text='매는 당신의 정해진 목표를 향해 굳건하게 흔들리지 않으며 날아가는 타입입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='한 번 무언가를 결심하고 결정하면 끝까지 노력하고 청취하려 합니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='달콤한 유혹도 잘 견뎌내고 결국엔 원하는 결과물을 직접 만들어 냅니다!')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    elif '나비' in text:
        bot.send_message(chat_id=chat_id, text='나비를 먼저 보았다면 빠른 상황대처 능력을 가져\n적응력이 남들보다 뛰어난 사람입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='아무리 험난하고 고된 시련이 와도 아름다움을 유지하는 당신은\n시련을 이겨낼 줄 아는 강인한 성격을 가진 타입입니다.')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    elif '비둘기' in text:
        bot.send_message(chat_id=chat_id, text='비둘기를 먼저 보았다면\n인생에서 사랑을 가장 중요하게 생각하는 타입입니다.')
        time.sleep(0.7)
        bot.send_message(chat_id=chat_id, text='영리하고 현명한 당신은 주위 사람들에게 늘 침착하고 부드러운 성품을 보이며\n용기와 희망을 전해주고 있습니다.')
        time.sleep(1.5)
        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")
    else:
        if text.isdigit() == False:
            bot.send_message(chat_id=chat_id, text='잘못입력하였습니다.\n다시 입력하세요!')

    if (int(update.message.text) > 10000000):
        i = int(update.message.text)
        result.insert(0, i // 10000)
        i = int(update.message.text) % 10000000
        i = int(update.message.text) % 1000000
        i = int(update.message.text) % 100000
        i = int(update.message.text) % 10000
        result.insert(1, i // 100)
        i = int(update.message.text) % 1000
        i = int(update.message.text) % 100
        result.insert(2, i // 1)
        uu = sum(bot, update)

    if (int(update.message.text) >= 0 and int(update.message.text) < 9):
        i = update.message.text
        num.insert(0, i)

    elif (int(update.message.text) >= 10 and int(update.message.text) <= 22):
        i = int(update.message.text)
        num.insert(0, i)


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
