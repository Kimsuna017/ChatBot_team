import telegram
import sqlite3
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup



my_token ='1075204229:AAGvsmDj3SiyDnWc4vm3S83DZLCTYLSq1uA'
chat_id = 1132917740
updater = Updater(token='1075204229:AAGvsmDj3SiyDnWc4vm3S83DZLCTYLSq1uA')
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
dp = updater.dispatcher

con = sqlite3.connect("C:/sqlite/chatbot")  ##DB생성
cur = con.cursor()  ##커서생성

TEST, REALTARO, MENU, TARO_B, TARO_D, DOOR, ANIMAL, PICTURE, NUMBER, GREEN, BLUE, RED, PURPLE, GREY, A, B, C, D, CANCEL, QA, USER, RECOMMAND, DETAIL, = range(23)


# 메세지 업데이트
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



#생일타로결과생성함수
def sum(bot, update):
    print("sum")
    dd = solve()
    bot.sendMessage(chat_id=update.message.chat_id, text=str(dd))



    if dd == 0 or dd == 22:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648900385?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xznrQu88T7i+4rW7SUoCWhrTO2CrHCON1HbumbfbmzKj15Ish3oECjAndZw4lh7MLQU=&authtoken=6mYNrDp3UNwwAHM+YPfruAI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격카드는 '광대' 입니다! 당신은 본성이 자유로운 사람이며, 무거운 삶의 과제를 안고 살지만 단순 소박합니다. 때로는 미숙하고 부주의하다는 평을 들을 수 있으나 하나에 빠지면 열정적으로 몰입합니다!")
        time.sleep(1.0)
        bot.sendMessage(chat_id= update.message.chat_id , text = "처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 1:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb1.photo.cloud.naver.com/3472427554648076832?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x4UprD0hOQp9Fc4yStZAdFF39ZikKmKtPyREkbJRxQ++Fdtp67aMTzL2RqRZGnRe+gU=&authtoken=Yob6XDaE5Zvmi/SefRU3PgI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '마법사' 입니다! 이 카드는 재주있는 사람을 말하며, 독창적이고 창조적이며 상상력이 뛰어남을 상징합니다. 능수능란한 재주가 있어 꾀를 부려도 남이 잘 알아채지 못합니다!")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 2:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648068640?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IPKf4Hib+AH+h1o8q0T8ugnax4Gxlp43Iw34tqTSQcAbwU=&authtoken=CGx9J1WaRTo0R1oEIxxfygI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '여성 대사제' 입니다! 이 카드는 지혜로운 사람을 말하며, 객관적이며 상황판단을 잘하는 것을 상징합니다. 주로 통찰력있고 직관적으로 행동하지만 사람을 주관적으로 대할 수 있어 상대의 불만을 사기도 합니다. ")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 3:
        bot.send_photo(chat_id=update.message.chat_id,
                       photo='http://thumb2.photo.cloud.naver.com/3472427554648048161?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xw0MQxY7FRdkeMIj+dj+WhOVGbbU3LJGa/Mfq7u1y5p0SXUAgUkmolgif+YD3Mok7AU=&authtoken=kUPe8Nj1Oc+hM4vUf4ubhAI=')
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="당신의 성격 카드는 '여제' 입니다! 이 카드는 부드러운 에너지가 발달한 사람을 말하며, 성취지향적이고 실용적입니다. 다른 사람을 돌보고 그들이 잘 성장할 수 있도록 돕고자 합니다!")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 4:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648066593?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IO2TmlykSyYET0FciV5oESxIIc6uddfsRB0n+7A5rRhHgU=&authtoken=nquKjZhDz82JRFoxjBTCkgI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '황제' 입니다! 이 카드는 가장을 상징하며 가진 것을 지키려고 앴는 사람을 말합니다. 세속적인 힘과 안정, 권위, 확신, 이성을 상징합니다. 남성일 경우 가부장적인 인물을 뜻합니다!")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 5:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648068129?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IPEQw4YF2WtrTKcJ+N/PpLkMs1vJw1CdUy+28+HFRADDgU=&authtoken=Os4EJ1FF5PB8VWgYcXqIjQI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '교황' 입니다! 이 카드는 진리를 가르치려는 교육자를 상징하며 주로 자비로우며 동정심이 강합니다. 주관이 뚜렷하며 의식을 중시하고 원칙을 따르려고 합니다. 주로 집단과 행동을 같이하고 지식 획득과 깨달음을 위해 노력합니다!")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 6:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648105504?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x9ShSmaRXb7sBW8WNRMaArMFoSagtMeIBuBBSQeqMLHwmHqF+WKd2fRzeomdiYBbIgU=&authtoken=rv2nnDEewW0D4s/1CifwrAI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '연인' 입니다! 이 카드는 인간관계를 중시하며 사랑이나 미에 높은 사람을 말합니다. 자신을 꾸미는 능력이 있고 이를 완성시키며 조화를 이루려고 합니다. 깊은 감정을 느끼며, 누군가와 그 정서를 교류하고 싶어합니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 7:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648196384?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xwCFy3+bnViFK87QgpUWtNWSkggfCMn//0duim9pPKVQcdM8GMuOezdfatKqwz7kkAU=&authtoken=LXNspjA2tUDRI87t/A0+ZAI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '전차' 입니다! 이 카드는 역경극복의 의지를 나타냅니다. 이 카드를 성격카드로 가진 사람은 한 가지에 집중하기 보다는 여러가지 일에 관심을 가지며, 실제로 그 일을 모두 해내는 경향이 있습니다. 그렇기 때문에 마음의 변화에 귀 기울이는 것이 중요합니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 8:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648186912?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x/O/NOEOJ91MV3VlI7ZV8zYu999M/eHsMpJit9QK7ljNQvB8mJ+qvKLSWP+F7OnAVQU=&authtoken=+5oXaVy35z6BixRrINPFOgI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '힘' 입니다! 이 카드는 외유내강형의 사람과 화난 사람을 진정시킬 줄 아는 사람을 말하며, 이 사람들은 주로 내적 용기와 힘, 결단력, 확신, 도전적 태도를 지닙니다. 그러나 내면의 두려움과 맞서야하는 과제를 안고 있습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 9:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648369441?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xwuxECnrWUOLyyH8pcx4deGIEgKFduLlU1JG1ySnZKNN0kp7H2KZu7kO/sSi4cRzzQU=&authtoken=XUUidelNiacLIJsgSPNl+AI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '은둔자' 입니다! 이 카드는 관심이 내면에 있는 사람이며 외부대상이나 환경에 신경을 쓰지 않는 편입니다. 감정을 억제하며 사려깊고 신중해 조언하기를 좋아합니다. 행동이 빠르지 않고 고요하며, 간혹 지나치게 침울한 사람도 있습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 10:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648396320?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7LAGt+TiuzcFNH9TmPqj9+nPtdnxywWVQkb664bqB6sDnFnoXPEj/7UcNa1BFd9YQU=&authtoken=1HKQUhvKXE+W9YUpdpsDnQI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '운명의 수레바퀴' 입니다! 이 카드는 재주있는 사람을 가리키며 행위의 결과가 자신에게 돌아오니 조심성을 가질 필요가 있습니다. 진리라 생각하는 분야를 배워 타인을 위해 가르치거나 공공의 이익을 위해 사용하는 것이 좋습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 11:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648384800?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7scJk+FDIjkv6Ddkp6ahDSiyYM75K8nJRV6o1SNhIVuFR2vCet/BLB7fIsnLQIK4wU=&authtoken=tcSj8+OVNal234GIN1K3nQI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '정의' 입니다! 이 카드는 공평무사, 균형 그리고 조화를 이루려는 것을 나타냅니다. 이 카드를 성격카드로 지닌 사람은 분별력이 있으며 판단 후에는 실쳔력이 빠르고 올바름, 미덕, 명예를 중시하는 경향이 있습니다. 그러나 대인관계에서도 판단이 앞선 나머지 정서적인 면을 간과할 수 있습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 12:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648429344?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xzf+M2SA1Ztl99EtXwHfvcFPBl7O03e90XCZr5Vm/ujFrkXxsrfXtW3rx9m35dxJRQU=&authtoken=8MOx387lcXEusGTUxARYawI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '매달린 사람' 입니다! 이 카드를 성격 카드를 지닌 사람은 말과 행동이 느리며 둔감한 편이라 정성적 표현이 부족한 경향이 있습니다. 그러나 내면에서는 많은 것이 일어나기 때문에 인내심을 가지고 지켜볼 필요가 있습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 13:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648660256?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xyScqqH/p2HWG9MWTceCsJ0KX/vS5TQvlzJepTYlNvvcrndBt8Llh3Qsg25amBmy/QU=&authtoken=EuL9U+1DI0ifh62mGOiPXwI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '죽음' 입니다! 이 카드는 변형을 일으키는 사람을 말합니다. 신체적인 죽음이 아니라 새로운 것을 위해 과거의 것을 과감히 제거하는 사람으로 익수한 상황을 유지하기 보다는 새 상황의 시작을 즐기고 새로움을 추구합니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 14:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648525600?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xxFGESAG+nBJTJrxNAjnAr/LTJErbFLc+1Y/1pyijcSunU8V+H5AM68RyVdUdiX0kgU=&authtoken=k3tj5fxYm3aS/4hev3IOyQI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '절제' 입니다! 이 카드를 성격 카드로 가진 사람은 자기통제와 검소한 태도를 통해 목표를 달성합니다. 환경에 순응하고 주변과 조화를 이루며 큰 목표를 위해 힘을 합칠 줄 압니다. 그러나 역작용이 일어나면 중독에 빠질 수 있습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 15:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648549665?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x/CwFMG5TRfXQUr1Pi1jrtOb2rQ9k+OyEJYsOsUBzZcRWMYtjW1safoCUtylRQaDIQU=&authtoken=e3KyM4XsGxDS3cWfIsg4XgI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '악마' 입니다! 이 카드는 집착이 강한 사람을 말하며, 자신과 관련된 대상에 대해 걱정을 많이 합니다. 실패 경험을 너무 오래 생각하면 자신과 주변이 힘들어 질 수 있습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 16:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648559648?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7pnovZiTrHNOqXu1Kj3FjER2KgDdaqrnGQ7El4HBNfmQV5dlSAboZMLBfpaubJ/GwU=&authtoken=+c8iRU2sztFJufBpZKH+dgI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '탑' 입니다! 이 카드는 변화의 충격으르 강하게 받는 사람을 말하며, 진실을 인식하고 맞지 않는 경우에는 가진 것을 모두 버릴 수 있는 과감함을 지니고 있습니다. 과거 대인 관계를 꾸준히 유지하기 보다 변화를 추구하는 경향이 있습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 17:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648692256?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x6ppsN1vzwMg1NU/UROoh6jnPcZn64sccWCkVfSJkJMudgea5K02i4AXUniKqPVWDQU=&authtoken=NwVtFoOR6ei+NTikaOTUkAI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '별' 입니다! 이 카드는 어둠속에 희망의 등불이 되려하는 사람을 말합니다. 주로 사람들에게 힘이 되고 싶어하며 신념이 있고 낙천적, 긍적적입니다. 그러나 그렇기 때문에 현재의 어려운 상황을 간과할 우려가 있습니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 18:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648705568?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x2UoC4cjV5+jbvRWun8/hSuGiXK+yf6X7Tg9DmCLGGg02EZtWRAXJb0vMDKGWkmqfwU=&authtoken=ct9aR2FQ+JVOS7v/x7p11QI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 운명의 '달' 입니다! 이 카드를 성격 카드로 지닌 사람은 마음이 자주 바뀌며 의심이 많습니다. 자신이 너무 순수해 잘 속는다고 생각합니다. 내적 변화를 인정하고 즐기는 방법을 찾는 것이 중요합니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 19:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648756768?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7RS0p5Vi/SPI7N/Pxfn8xtWZZMxLUpUQY5wtL7C/9VmEcWbI0dl8IAuiSpoLk5mVgU=&authtoken=QlZly3qsuRBnc+jTwivzNAI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '태양' 입니다! 이 카드는 어린애처럼 순수한 사람을 말하며, 자신의 역량보다 더 큰 일을 해내는 용기와 믿음이 있습니다. 고생이 많아도 특별한 보살핌 또한 경험했을 가능성이 있으며 이에 대한 감사를 잊으면 안됩니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 20:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648845857?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x70tL5v6OyhRVcVqf1brOzMBFupHaPOhzkFQJoAGAkLZzBHiByx787wf7AvJhd9ABgU=&authtoken=uj7wzCW2j9ejVZgpRn7FpAI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '심판' 입니다! 이 카드는 옳고 그름에 대한 판단이 바르고,정의로운 사람을 말합니다. 희생을 감수해 진리를 드러내고자 하며 억울한 사람을 보면 무심해지기 어려워 적극 개입합니다.")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    elif dd == 21:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648860961?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x6vWAqAFs8f5zGm0SDoi2q9PezVrDoVJU4tHCrJOgDunNcKfwdHq9CUmjXAacUWU1QU=&authtoken=nOD0cf1XlO4TK0lzgXrp1QI=')

        bot.sendMessage(chat_id=update.message.chat_id,

                        text="당신의 성격 카드는 '세계' 입니다! 이 카드는 어떠한 환경에서도 완성을 이루려는 사람을 말하며 주로 완벽주의자고 시야가 넓습니다. 가족이 도움을 구하면 자기 일처럼 돕습니다. ")
        time.sleep(1.0)
        bot.sendMessage(chat_id=update.message.chat_id, text="처음으로 돌아가려면 /start 를 눌러주세요!")
    return dd


#오늘의운세결과출력함수
def today(bot, update):

    print("today")

    value = today_2()

    if value == 0 :

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648900385?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xznrQu88T7i+4rW7SUoCWhrTO2CrHCON1HbumbfbmzKj15Ish3oECjAndZw4lh7MLQU=&authtoken=6mYNrDp3UNwwAHM+YPfruAI=')

        t = "오늘의 카드는 The Fool!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "태양이 비추는 절벽끝에 서있는 광대의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "발밑은 끝을 알 수 없는 절벽에 서있는 당신!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "일을 서두르면 망칠 가능성이 높네요, 오늘은 조급한 마음을 살짝 내려놓는게 어떨까요?"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 1:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648076832?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x4UprD0hOQp9Fc4yStZAdFF39ZikKmKtPyREkbJRxQ++Fdtp67aMTzL2RqRZGnRe+gU=&authtoken=Yob6XDaE5Zvmi/SefRU3PgI=')

        t = "오늘의 카드는 The Magician!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "꼬리를 문 뱀을 허리에 감고 있는 마법사의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "마법과 같은 말은 말에 휩쓸려 불이익이 생길지도 몰라요!" + "\n" + "오늘은 결정을 잠시 미뤄두는게 어떨까요?"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 2:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648068640?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IPKf4Hib+AH+h1o8q0T8ugnax4Gxlp43Iw34tqTSQcAbwU=&authtoken=CGx9J1WaRTo0R1oEIxxfygI=')

        t = "오늘의 카드는 The High Priestess!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "의자에 앉아 있는 여교황의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "보는 눈이 많아 뒷탈이 있을지도 모르는 오늘!" + "\n" + "눈에 띄지 않게 조심히 행동하는게 어떨까요?"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 3:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648048161?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xw0MQxY7FRdkeMIj+dj+WhOVGbbU3LJGa/Mfq7u1y5p0SXUAgUkmolgif+YD3Mok7AU=&authtoken=kUPe8Nj1Oc+hM4vUf4ubhAI=')

        t = "오늘의 카드는 The Empress!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "풍요로움 속에 있는 여황제의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "오늘은 안정적이고 하던일이 성공하는 하루가 될거에요!" + "\n" + "그런데 한가지! '집착'을 조심해야해요~"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 4:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648066593?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IO2TmlykSyYET0FciV5oESxIIc6uddfsRB0n+7A5rRhHgU=&authtoken=nquKjZhDz82JRFoxjBTCkgI=')

        t = "오늘의 카드는 The Emperor!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "불안한 듯한 황제의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "리더의 위치에 있다면 보수적인 모습으로 인해 사람이 떠나갈 수 있어요." + "\n" + "융통성을 가질 필요가 있을 것 같네요!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 5:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648068129?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x1kyUvVUk1/5PADuOWqm3IPEQw4YF2WtrTKcJ+N/PpLkMs1vJw1CdUy+28+HFRADDgU=&authtoken=Os4EJ1FF5PB8VWgYcXqIjQI=')

        t = "오늘의 카드는 The Hierophant!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "두사람에게 지시를 내리는 듯한 교황의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "이중 생활이나 약속으로 곤란한 상황이 생길 수 있는 하루에요!" + "\n" + "평소보다 더 신중해질 필요가 있어요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 6:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648105504?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x9ShSmaRXb7sBW8WNRMaArMFoSagtMeIBuBBSQeqMLHwmHqF+WKd2fRzeomdiYBbIgU=&authtoken=rv2nnDEewW0D4s/1CifwrAI=')

        t = "오늘의 카드는 The Lovers!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "서로 마주보고 있는 연인들의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "뱀의 유혹과 같은 말을 조심하고 혹은 천사와 같이 다른 사람의 실수를 모른척 넘어가 주어야 하는 날이에요!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 7:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648196384?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xwCFy3+bnViFK87QgpUWtNWSkggfCMn//0duim9pPKVQcdM8GMuOezdfatKqwz7kkAU=&authtoken=LXNspjA2tUDRI87t/A0+ZAI=')

        t = "오늘의 카드는 The Chariot!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "전차에 올라있는 기사 앞에 스핑크스 두마리가 있는 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "오늘은 조율과 통제가 필요한 날이에요!" + "\n" + "하려는 일에 의욕이 넘치는 모습도 좋지만 균형을 이루는 전략이나 계획이 먼저 필요해요!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 8:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648186912?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x/O/NOEOJ91MV3VlI7ZV8zYu999M/eHsMpJit9QK7ljNQvB8mJ+qvKLSWP+F7OnAVQU=&authtoken=+5oXaVy35z6BixRrINPFOgI=')

        t = "오늘의 카드는 The Strength!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "꽃을 두른 여성이 사자를 어루만지는 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "사자와 같은 욕망이나 욕심, 본능이 해로울 수 있는 날이에요!" + "\n" + "오늘은 평소보다 의지, 인내, 신념을 강하게 가져보는 것은 어떨까요?"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 9:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648369441?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xwuxECnrWUOLyyH8pcx4deGIEgKFduLlU1JG1ySnZKNN0kp7H2KZu7kO/sSi4cRzzQU=&authtoken=XUUidelNiacLIJsgSPNl+AI=')

        t = "오늘의 카드는 The Hermit!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "지팡이와 등불을 들고 있는 노인의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "혹시 혼자만의 고민이 있지는 않은가요?" + "\n" + "오늘은 내면의 소리에 귀길울여 보세요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 10:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648396320?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7LAGt+TiuzcFNH9TmPqj9+nPtdnxywWVQkb664bqB6sDnFnoXPEj/7UcNa1BFd9YQU=&authtoken=1HKQUhvKXE+W9YUpdpsDnQI=')

        t = "오늘의 카드는 The Wheel of Fortune!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "운명의 수레바퀴의 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "무언가 새로 시작하려고 하고 있지 않나요?" + "\n" + "당신을 위한 주변의 도움이 기다리고 있네요!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 11:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648384800?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7scJk+FDIjkv6Ddkp6ahDSiyYM75K8nJRV6o1SNhIVuFR2vCet/BLB7fIsnLQIK4wU=&authtoken=tcSj8+OVNal234GIN1K3nQI=')

        t = "오늘의 카드는 The Justice!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "왼손에는 천칭, 오른손에는 검을 들고 앉아있는 사람의 모습이보이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "자신의 상황에 냉정해질 필요가 있어요!" + "\n" + "어느 쪽으로도 치우치지 않는 공정한 판단이 필요할 것 같네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 12:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648429344?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xzf+M2SA1Ztl99EtXwHfvcFPBl7O03e90XCZr5Vm/ujFrkXxsrfXtW3rx9m35dxJRQU=&authtoken=8MOx387lcXEusGTUxARYawI=')

        t = "오늘의 카드는 The Hanged Man!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "거꾸로 매달려 있는 남자의 모습이 보이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "당신의 희생이 목표달성으로 이루어 질 수 있는 날!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 13:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648660256?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xyScqqH/p2HWG9MWTceCsJ0KX/vS5TQvlzJepTYlNvvcrndBt8Llh3Qsg25amBmy/QU=&authtoken=EuL9U+1DI0ifh62mGOiPXwI=')

        t = "오늘의 카드는 The Death!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "해골기사와 시체와 사람들의 모습이 보이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "이전과는 전혀다른 새로운 것이 시작되는 하루가 될꺼에요!" + "\n" + "갑작스러운 변화에 고통이 따르지만 그 후에는 얻는 것이 있을 거에요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 14:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648525600?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9xxFGESAG+nBJTJrxNAjnAr/LTJErbFLc+1Y/1pyijcSunU8V+H5AM68RyVdUdiX0kgU=&authtoken=k3tj5fxYm3aS/4hev3IOyQI=')

        t = "오늘의 카드는 The Temperance!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "천사가 한발은 땅에, 한발은 물에 두고 있는 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "절제로 상황을 조정할 필요가 있는 날이에요!" + "\n" + "성급하지 않은 접근이 포인트랍니다!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 15:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648549665?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x/CwFMG5TRfXQUr1Pi1jrtOb2rQ9k+OyEJYsOsUBzZcRWMYtjW1safoCUtylRQaDIQU=&authtoken=e3KyM4XsGxDS3cWfIsg4XgI=')

        t = "오늘의 카드는 The Devil!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "악마와 결박되어 있는 두 사람이 보이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "이것은 당신을 향한 경고!" + "\n" + "내면의 두려움 또는 욕망, 인간관계등 어떠한 것에 집착하지 않도록 주의하세요!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 16:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648559648?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7pnovZiTrHNOqXu1Kj3FjER2KgDdaqrnGQ7El4HBNfmQV5dlSAboZMLBfpaubJ/GwU=&authtoken=+c8iRU2sztFJufBpZKH+dgI=')

        t = "오늘의 카드는 The Tower!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "불길이 치솟는 탑과 떨어지는 두 사람이 보이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "뜻밖의 사건이 오늘 하루를 어렵게 할지도 몰라요!" + "\n" + "어려움을 기회로 만들어 보는 것을 어떨까요?"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 17:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648692256?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x6ppsN1vzwMg1NU/UROoh6jnPcZn64sccWCkVfSJkJMudgea5K02i4AXUniKqPVWDQU=&authtoken=NwVtFoOR6ei+NTikaOTUkAI=')

        t = "오늘의 카드는 The Star!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "하늘에 떠있는 별들과 물을 붓고 있는 여성이 보이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "당신에게 행운이 찾아올거에요!" + "\n" + "하고 있는 일에 긍정적인 결과가 생길 것 같네요!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 18:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648705568?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x2UoC4cjV5+jbvRWun8/hSuGiXK+yf6X7Tg9DmCLGGg02EZtWRAXJb0vMDKGWkmqfwU=&authtoken=ct9aR2FQ+JVOS7v/x7p11QI=')

        t = "오늘의 카드는 The Moon!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "사람의 옆모습을 한 달이 밤하늘에 떠있는 모습이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "혹시 지금 불안해하고 있지 않나요?" + "\n" + "재빠르게 행동하지 못하면 불이익이 생길 수도 있어요!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 19:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648756768?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x7RS0p5Vi/SPI7N/Pxfn8xtWZZMxLUpUQY5wtL7C/9VmEcWbI0dl8IAuiSpoLk5mVgU=&authtoken=QlZly3qsuRBnc+jTwivzNAI=')

        t = "오늘의 카드는 The Sun!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "밝은 태양아래 꽃들과 백마를 탄 아이의 모습이 보이네요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "오늘은 모든 것이 명확해지는 날이에요!" + "\n" + "확실한 성공이 당신을 따를거에요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 20:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb2.photo.cloud.naver.com/3472427554648845857?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x70tL5v6OyhRVcVqf1brOzMBFupHaPOhzkFQJoAGAkLZzBHiByx787wf7AvJhd9ABgU=&authtoken=uj7wzCW2j9ejVZgpRn7FpAI=')

        t = "오늘의 카드는 The Judgement!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "하늘엔 천사가 나팔을 불고 땅에는 죽었던 사람이 일어나는 모습이에요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "오늘은 그동안의 어려움이 해결되는 날!" + "\n" + "다른 사람의 도움을 거절하지 마세요!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")



    if value == 21:

        bot.send_photo(chat_id=update.message.chat_id,

                       photo='http://thumb1.photo.cloud.naver.com/3472427554648860961?type=m3&setidc=2&filelink=vbDHg5Gj4B1dZofT7fR9x6vWAqAFs8f5zGm0SDoi2q9PezVrDoVJU4tHCrJOgDunNcKfwdHq9CUmjXAacUWU1QU=&authtoken=nOD0cf1XlO4TK0lzgXrp1QI=')

        t = "오늘의 카드는 The World!"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "월계수 원 안에서 여인이 춤을 추고 있는 모습이에요."

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.0)

        t = "어떤일의 마무리에 있지 않나요?" + "\n" + "결과가 어떠하든 툭툭 털고 새로운 시작을 해보는게 어떨까요?"

        bot.sendMessage(chat_id=update.message.chat_id, text=t)

        time.sleep(1.5)

        update.message.reply_text("또다른 테스트를 하고 싶다면 /test 를 눌러보세요!")


#생일타로입력값 계산함수
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




#num배열의 값을 리턴
def today_2():

    return num[0]



# 동물관련 심리테스트

def door1(bot, update):
    query = update.callback_query

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"당신의 눈앞에 5가지 색깔 문이 있어요." + "\n" + "이 중에서 당신의 마음에 드는 문을 한가지 선택해주세요."
    )

    show_list = []

    show_list.append(InlineKeyboardButton("초록", callback_data=str(GREEN)))

    show_list.append(InlineKeyboardButton("파랑", callback_data=str(BLUE)))

    show_list.append(InlineKeyboardButton("빨강", callback_data=str(RED)))

    show_list.append(InlineKeyboardButton("보라", callback_data=str(PURPLE)))

    show_list.append(InlineKeyboardButton("회색", callback_data=str(GREY)))

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=show_markup
    )

    return CallbackQueryHandler(callback_get)


#숫자관련 심리테스트

def number_check(bot, update):
    query = update.callback_query

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"제가 당신이 좋아하는 숫자와 당신의 나이를 맞춰보려고 하는데요!"
    )

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"제가 지시하는 대로 따라해 주실래요?"
    )

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"1부터 10 중에 아.무 숫자나 하나 골라 보세요!"
    )

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"고른 숫자는 저를 알려주지 말고 마음속으로만 생각하세요!"
    )

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"골랐나요? 골랐다면 /yes 를 눌러 주세요!"
    )



def yes(bot, update):
    bot.sendMessage(chat_id=chat_id, text='조금 더 저를 어렵게 만들고 싶다면 고른 숫자에 9를 곱하세요!')
    bot.sendMessage(chat_id=chat_id, text='곱한 숫자는 저를 알려주지 말고 마음속으로만 생각하세요!')
    bot.sendMessage(chat_id=chat_id, text='골랐나요? 골랐다면 /yes2 를 눌러 주세요!')


def yes2(bot, update):
    bot.sendMessage(chat_id=chat_id, text='그 곱한 수가 한자리면 그냥 냅두고\n두자리라면 각 자리의 숫자를 더해주세요!\nex)4->4, 14->1+4=5')
    bot.sendMessage(chat_id=chat_id, text='나온 숫자는 저를 알려주지 말고 마음속으로만 생각하세요!')
    bot.sendMessage(chat_id=chat_id, text='구했나요? 구했다면 /yes3 를 눌러 주세요!')


def yes3(bot, update):
    bot.sendMessage(chat_id=chat_id, text='나온 숫자에 13을 더해주세요!')
    bot.sendMessage(chat_id=chat_id, text='더한 숫자는 저를 알려주지 말고 마음속으로만 생각하세요!')
    bot.sendMessage(chat_id=chat_id, text='더했나요? 더했다면 /yes4 를 눌러 주세요!')


def yes4(bot, update):
    bot.sendMessage(chat_id=chat_id, text='나온 숫자에 드디어 당신이 좋.아.하.는 숫자를 더해주세요!')
    bot.sendMessage(chat_id=chat_id, text='더해서 나온 값을 입력해 주시겠어요?')



# 문관련 심리테스트
def crawl_animal(bot, update):
    query = update.callback_query
    print("test")

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"이 사진에는 총 9마리의 동물, 곤충 등이 있는데요!"
    )

    bot.send_photo(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        photo=u'https://pbs.twimg.com/media/DY9aTtFVQAAm2aG.jpg'
    )

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"이 중 가장 먼저 보이는 동물은 무엇인가요?"
    )


#문심리테스트결과1
def green(bot, update):
    query = update.callback_query
    print("green")
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"초록 문을 선택한 당신은" + "\n" + "뛰어난 관찰력과 의사소통 능력으로 사람들 사이에서 중재자 역할을 담당하는 밝은 성격의 소유자에요."
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"주변사람들을 잘 챙기고 힘이 되어주며 쾌활하고 밝은 에너지를 가지고 있어요!" + "\n" + "또한 타인의 고민을 잘 들어주고 공감해 주기도 하죠"
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"하지만 새로운 변화를 좋아하지 않고" + "\n" + "선택이나 결정을 쉽게 하지 못하는 우유부단한 성격이 있어요!"
    )


    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )


#문심리테스트결과2
def blue(bot, update):
    query = update.callback_query
    print("blue")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"파란 문을 선택한 당신은" + "\n" + "똑똑하고 체계적인 성격의 소유자에요."
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"온화한 성품을 갖고 있으며 뛰어난 절제력으로 자기관리를 잘하는 사람이죠!" + "\n" + "분석적이며 통찰력을 가지고 있기도해요"
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"하지만 비판에 민감하고" + "\n" + "때로는 비관적인 경우가 있으며 완벽주의 성향으로 일을 늦출수 있어요!"
    )

    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )


#문심리테스트결과3
def red(bot, update):
    query = update.callback_query
    print("red")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"빨간 문을 선택한 당신은" + "\n" + "빠른 의사결정 능력으로 명쾌하고 시원한 답변을 내리는 해결사 성격의 소유자에요."
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"즉각적으로 일을 처리하며 주관이 뚜렷하고 개성있는 사람이죠!" + "\n" + "감각적이고 뛰어난 안목을 갖고 있어요."
    )
    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"하지만 참을성이 부족한 편이에요" + "\n" + "때로는 단호한 성격으로 이해 주변 사람이 어려움을 겪는 경우가 있어요!"
    )

    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )



#문심리테스트결과4
def purple(bot, update):
    query = update.callback_query
    print("purple")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"보라색 문을 선택한 당신은" + "\n" + "신비로운 매력과 예술 감각을 가진 예술가 성격의 소유자에요."
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"침착한 성격을 갖고 있으며 풍부한 감수성을 가진 사람이죠!" + "\n" + "뛰어난 관찰력으로 다양하고 폭넓은 아이디어 뱅크에요."
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"하지만 예민한 성격도 가지고 있어요" + "\n" + "다소 변덕스럽고 감정기복이 심해 쉽게 흥분할 수가  있어요!"
    )

    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )



#문심리테스트결과5
def grey(bot, update):
    query = update.callback_query
    print("grey")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"회색 문을 선택한 당신은" + "\n" + "매사에 신중하고 뛰어난 분별력을 가진 성격의 소유자에요."
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"성실한 성격을 가지고 있는 사람이죠!" + "\n" + "평화주의자로 매사에 균형을 유지하고 세련된 취향을 가지고 있어요."
    )

    time.sleep(0.7)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"하지만 소심한 부분이 있고" + "\n" + "때로는 자기중심적으로 비춰질때가 있고 우유부단하며 의존적인 면이 있어요!"
    )

    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )



# 사진 관련 심리테스트

def picture(bot, update):
    query = update.callback_query
    print("test")

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"힘들 때 당신이 가장 많이 의지하는 것에 대한 테스트입니다!"
    )

    bot.send_photo(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        photo='https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F998D84385B6B27D52D'
    )

    show_list = []

    show_list.append(InlineKeyboardButton("A", callback_data=str(A)))

    show_list.append(InlineKeyboardButton("B", callback_data=str(B)))

    show_list.append(InlineKeyboardButton("C", callback_data=str(C)))

    show_list.append(InlineKeyboardButton("D", callback_data=str(D)))

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))


    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=show_markup
    )

    bot.send_photo_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=show_markup
    )


    return CallbackQueryHandler(callback_get)


#사진심리테스트결과1
def a(bot, update):
    query = update.callback_query
    print("A")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"힘들 때 당신이 가장 많이 의지하는 것은 <연인> 이에요"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"지금 연인이 없다면," + "\n" + "연애를 원하는 이유가 의지하고 싶은 마음 때문입니다."
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"A를 선택한 사람의 특징은" + "\n" + "무엇보다 감정을 중요하게 생각하는 편으로,"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"연인에게 가장 바라는 점은 당신의 감정을 잘 알아주길 바란답니다!"
    )

    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )




#사진심리테스트결과2
def b(bot, update):
    query = update.callback_query
    print("B")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"힘들 때 당신이 가장 많이 의지하는 것은 <자기자신> 이에요"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"의지라기 보다는 스스로에 대한 믿음이 강하다는 표현이 더 어울리네요~"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"B를 선택한 사람들의 특징은" + "\n" + "무척이나 강인한 정신력을 가지고 있어서" + "\n" + "어떠한 일도 스스로 해결하고자 하는 마음이 큽니다."
    )

    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"따라서 힘든 상황에 놓여도 주변에 절대로 티를 내지 않는 타입입니다!"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"아주 이상적인 타입이긴 하지만 왠지 좀 쓸쓸해보이기도 합니다."
    )

    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )




#사진심리테스트결과3
def c(bot, update):
    query = update.callback_query
    print("C")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"힘들 때 당신이 가장 많이 의지하는 것은 <꿈! 미래! 희망!> 이에요"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"지금 당장의 고통은 더 행복한 미래를 위해" + "\n" + "어쩔 수 없다고 생각하는 긍정적인 마음을 가지고 있습니다."
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"C를 선택한 사람들의 특징은" + "\n" + "미래에 대한 구체적인 계획을 가지고 있다는 점인데요!"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"그렇기 때문에 어렵고 힘든 시간이 찾아와도" + "\n" + "흔들림 없이 꿈을 향해 나아갈 수 있습니다"
    )

    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )




#사진심리테스트결과4
def d(bot, update):
    query = update.callback_query
    print("D")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"힘들 때 당신이 가장 많이 의지하는 것은 <친구> 입니다"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"주변에 진정한 친구가 많기 때문에" + "\n" + "어려울 때 친구들이 먼저 생각납니다."
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"진정한 친구가 많다는 것은" + "\n" + "그만큼 훌륭한 대인관계를 유지하고 있다는 뜻인데요!"
    )

    time.sleep(0.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"당신은 어렵고 힘든 일을 겪을 때 " + "\n" + "도움의 손길을 먼저 내밀어 줄 친구들에게 많이 의지를 한답니다."
    )

    time.sleep(1.5)

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"다른 테스트를 하고 싶다면 /start를 누르세요!"
    )




#입력된 모든 데이터를 분류
def get_message(bot, update):

    text, i, j = update.message.text, 10000000, 0


    if '타로점' in text and '타로' in text:

        bot.send_message(chat_id=update.message.chat_id, text='타로점을 고르셨습니다.')



    elif '말' in text:

        bot.send_message(chat_id=update.message.chat_id, text='말은 야망이 강한 사람으로 자유롭고 야생적이며 성공하기 위해 노력하는 타입입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='비록 장애물에 부딪힐 수 있지만 포기하지 않고 꾸준히 노력하는 성향을 가지고 있습니다.')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='또한! 그 성격을 아는 주변 사람들에게 정직한 성격을 가진 이로 신뢰를 받고 있을 것 입니다.')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")



    elif '닭' in text:

        bot.send_message(chat_id=update.message.chat_id, text='닭이 먼저 보였다면 인내심이 강한 타입입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='끈기와 민첩성을 가진 당신은 온순하지 않지만\n당신의 인내심을 깰만한 사람은 별로 없다고 보면 됩니다.')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")



    elif '꽃게' in text:

        bot.send_message(chat_id=update.message.chat_id, text='꽃게를 먼저 본 당신은 무뚝뚝하면서도 속은 부드러운 사람입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='신뢰를 가장 중요시하는 타입으로 진심을 소중히 여기고\n사랑하는 사람들을 먼저 생각 합니다.')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")



    elif '사마귀' in text:

        bot.send_message(chat_id=update.message.chat_id, text='사마귀가 먼저 보였다면 직감같은 감각 자체가 뛰어난 사람입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='누구보다 날카로운 직감을 가진 당신은\n원하는 것을 얻기 위해 마음의 소리에 따라 충동적인 행동을 할 때도 많을 것 입니다.')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")



    elif '늑대' in text:

        bot.send_message(chat_id=update.message.chat_id, text='늑대를 가장 먼저 보았다면\n당신은 부드러운 외면과 사납지만 용기 있는 내면을 가진 사람입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='용감함을 가지고 있는 당신은\n사람들에게 둘러싸여 있어도 눈에 띄는 존재감!을 가지고 있을 것입니다.')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")



    elif '강아지' in text:

        bot.send_message(chat_id=update.message.chat_id, text='강아지가 먼저 눈에 들어왔다면\n성실하고 지조를 갖춘 사람입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='대개 사려가 깊으며 다정다감한 당신은\n먼저 사람을 잘 돕고 늘 주변을 위한 성격으로 인기가 많은 타입입니다.')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")



    elif '매' in text:

        bot.send_mesage(chat_id=update.message.chat_id, text='매는 당신의 정해진 목표를 향해 굳건하게 흔들리지 않으며 날아가는 타입입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='한 번 무언가를 결심하고 결정하면 끝까지 노력하고 청취하려 합니다.')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='달콤한 유혹도 잘 견뎌내고 결국엔 원하는 결과물을 직접 만들어 냅니다!')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")



    elif '나비' in text:

        bot.send_message(chat_id=update.message.chat_id, text='나비를 먼저 보았다면 빠른 상황대처 능력을 가져\n적응력이 남들보다 뛰어난 사람입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='아무리 험난하고 고된 시련이 와도 아름다움을 유지하는 당신은\n시련을 이겨낼 줄 아는 강인한 성격을 가진 타입입니다.')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")



    elif '비둘기' in text:

        bot.send_message(chat_id=update.message.chat_id, text='비둘기를 먼저 보았다면\n인생에서 사랑을 가장 중요하게 생각하는 타입입니다!')

        time.sleep(0.7)

        bot.send_message(chat_id=update.message.chat_id, text='영리하고 현명한 당신은 주위 사람들에게 늘 침착하고 부드러운 성품을 보이며\n용기와 희망을 전해주고 있습니다.')

        time.sleep(1.5)

        update.message.reply_text("이 심리테스트에 대한 또 다른 결과가 보고싶다면 다른 동물 또는 곤충을 입력해주시고\n 다른 심리테스트를 하기 원한다면 /menu 를 눌러주세요")

    else:

        if text.isdigit() == False:

            bot.send_message(chat_id=update.message.chat_id, text='그런 동물은 존재하지 않아요ㅠㅠ\n다시 입력하세요!')



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



    if (int(update.message.text) >= 0 and int(update.message.text) <= 9):

        i = int(update.message.text)

        num.insert(0, i)

        uu = today(bot, update)

    elif (int(update.message.text) >= 10 and int(update.message.text) <= 22):

        i = int(update.message.text)

        num.insert(0, i)

        uu = today(bot, update)



    if (int(update.message.text) > 22 and int(update.message.text) < 99):

        text = int(update.message.text)-22
        bot.sendMessage(chat_id=chat_id, text='당신이 좋아하는 숫자는 바로바로!')
        bot.sendMessage(chat_id=chat_id, text=text)
        bot.sendMessage(chat_id=chat_id, text='정답이죠?ㅎㅎ')
        bot.sendMessage(chat_id=chat_id, text='또 다른 테스트를 하고 싶다면 /test 를 눌러주세요!')



# 전역변수
result = [0, 0, 0]

pp = result[0] + result[1] + result[2]

result2 = [0, 0, 0, 0]

dd = result2[0] + result2[1] + result2[2] + result2[3]

num = [0]

value = num[0]



##고친함수들

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


# 시작메세지전달(타로&심리중에 고르기)
def test(bot, update):
    query = update.callback_query
    print("test")

    show_list = []

    show_list.append(InlineKeyboardButton("타로", callback_data=str(REALTARO)))

    show_list.append(InlineKeyboardButton("심리", callback_data=str(MENU)))

    show_list.append(InlineKeyboardButton("Q&A", callback_data=str(QA)))

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"원하는 걸 선택하세요.",
    )

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=show_markup
    )

    return CallbackQueryHandler(callback_get)


def realtaro(bot, update):
    query = update.callback_query
    print("realtaro")

    show_list = []
    show_list.append(InlineKeyboardButton("성격카드", callback_data=str(TARO_B)))

    show_list.append(InlineKeyboardButton("오늘의 운세", callback_data=str(TARO_D)))

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

    return CallbackQueryHandler(callback_get)


#생일타로함수
def taro_b(bot, update):
    query = update.callback_query
    print("taro_b")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"태어난 연도, 월, 일을 입력하세요. ex)20000305"
    )



#오늘의운세타로
def taro_d(bot, update):
    query = update.callback_query
    print("taro_d")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"0부터 22까지 마음에 드는 숫자를 골라보세요!"
    )

#Q&A 메뉴

def question(bot, update):
    query = update.callback_query

    print("question")

    show_list = []

    show_list.append(InlineKeyboardButton("1. 총 이용자수", callback_data=str(USER)))

    show_list.append(InlineKeyboardButton("2. 인기 메뉴", callback_data=str(RECOMMAND)))

    show_list.append(InlineKeyboardButton("3.세부사항", callback_data=str(DETAIL)))

    show_list.append(InlineKeyboardButton("4.취소", callback_data=str(CANCEL)))

    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 1))

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"궁금한 것을 골라줘!"
    )

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=show_markup
    )
    return CallbackQueryHandler(callback_get)


# 심리테스트선택시 호출되는 함수
def test_menu(bot, update):
    query = update.callback_query
    print(test_menu)

    show_list = []

    show_list.append(InlineKeyboardButton("1.문", callback_data= str(DOOR)))

    show_list.append(InlineKeyboardButton("2.동물", callback_data=str(ANIMAL)))

    show_list.append(InlineKeyboardButton("3.사진", callback_data=str(PICTURE)))

    show_list.append(InlineKeyboardButton("4.숫자", callback_data=str(NUMBER)))

    show_list.append(InlineKeyboardButton("5.취소", callback_data=str(CANCEL)))

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
    return CallbackQueryHandler(callback_get)


def cancel(bot,update):
    query = update.callback_query

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"취소가 선택되었습니다. 다시 처음으로 돌아가고 싶으면 /start 를 누르세요."
    )



# 버튼 처리할 함수
def callback_get(bot, update):
    query = update.callback_query

    print("callback")

    con, cur = None, None
    global birth, tod, door, animal, photo, number, Max, Min, Sum

    con = sqlite3.connect("C:/sqlite/chatbot")  ##DB생성
    cur = con.cursor()  ##커서생성

    if update.callback_query.data == str(REALTARO):
        uu = realtaro(bot, update)

    elif update.callback_query.data == str(MENU):
        uu = test_menu(bot, update)
    elif update.callback_query.data == str(QA):
        uu = question(bot, update)
    elif update.callback_query.data == str(USER):
        uu = user(bot, update)
    elif update.callback_query.data == str(RECOMMAND):
        uu = recommand(bot, update)
    elif update.callback_query.data == str(DETAIL):
        uu = detail(bot, update)
    elif update.callback_query.data == str(TARO_B):
        sql = "INSERT INTO chatbot(sel1, sel2, sel3) VALUES('타로','생일점','')"
        cur.execute(sql)
        uu = taro_b(bot, update)

    elif update.callback_query.data == str(TARO_D):
        sql = "INSERT INTO chatbot(sel1, sel2, sel3) VALUES('타로','오늘의운세','')"
        cur.execute(sql)
        uu = taro_d(bot, update)

    # elif update.callback_query.data == str(DOOR):
    #     sql = "INSERT INTO chatbot(sel1, sel2, sel3) VALUES('심리','문','')"
    #     cur.execute(sql)
    #     uu = door(bot, update)

    elif update.callback_query.data == str(ANIMAL):
        sql = "INSERT INTO chatbot(sel1, sel2, sel3) VALUES('심리','동물','')"
        cur.execute(sql)
        crawl_animal(bot, update)

    elif update.callback_query.data == str(DOOR):
        sql = "INSERT INTO chatbot(sel1, sel2, sel3) VALUES('심리','문','')"
        cur.execute(sql)
        uu = door1(bot, update)


    elif update.callback_query.data == str(PICTURE):
        sql = "INSERT INTO chatbot(sel1, sel2, sel3) VALUES('심리','사진','')"
        cur.execute(sql)
        uu = picture(bot, update)

    elif update.callback_query.data == str(NUMBER):
        sql = "INSERT INTO chatbot(sel1, sel2, sel3) VALUES('심리','숫자','')"
        cur.execute(sql)
        uu = number_check(bot, update)

    elif update.callback_query.data == str(GREEN):
        uu = green(bot, update)
    elif update.callback_query.data == str(BLUE):
        uu= blue(bot, update)
    elif update.callback_query.data == str(RED):
        uu = red(bot, update)
    elif update.callback_query.data == str(PURPLE):
        uu = purple(bot, update)
    elif update.callback_query.data == str(GREY):
        uu = grey(bot, update)
    elif update.callback_query.data == str(A):
        uu = a(bot, update)
    elif update.callback_query.data == str(B):
        uu = b(bot, update)
    elif update.callback_query.data == str(C):
        uu = c(bot, update)
    elif update.callback_query.data == str(D):
        uu = d(bot, update)
    #elif update.callback_query.data == str(CANCEL):

#DB 저장 및 값가져오기
    con.commit()

    cur.execute("select count(*) from chatbot")
    data = cur.fetchone()
    Sum = data[0]
    print(Sum)
    cur.execute("select count(*) from chatbot where sel2='생일점'")
    data = cur.fetchone()
    birth = data[0]
    print(birth)
    #bot.sendMessage(chat_id=update.message.chat_id, text=birth)
    cur.execute("select count(*) from chatbot where sel2='오늘의운세'")
    data = cur.fetchone()
    tod=data[0]
    print(tod)
    cur.execute("select count(*) from chatbot where sel2='문'")
    data = cur.fetchone()
    door=data[0]
    print(door)
    cur.execute("select count(*) from chatbot where sel2='동물'")
    data = cur.fetchone()
    animal=data[0]
    print(animal)
    cur.execute("select count(*) from chatbot where sel2='사진'")
    data = cur.fetchone()
    photo=data[0]
    print(photo)
    cur.execute("select count(*) from chatbot where sel2='숫자'")
    data = cur.fetchone()
    number=data[0]
    print(number)




# 이용자수

def user(bot, update):
    query = update.callback_query

    print("user")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"저희 챗봇의 총 이용자 수가 궁금하시다구요?"
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'저희 챗봇의 총 이용자 수는 \"' + str(Sum) + '\"명이에요!'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"더 많은 이용 부탁 드릴게요!!"
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"또다른 궁금한 사항이 있다면 /question 을 눌러주세요~"
    )
    time.sleep(0.5)



# 인기 메뉴

def recommand(bot, update):
    query = update.callback_query

    print("recommand")

    count=0

    #Sum = birth + tod + door + animal + photo + number

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"무슨 메뉴를 골라야 할지 고민이면"
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"가장 인기있는 메뉴를 해보는건 어떨까요?"
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'저희 타로심리봇 이용 횟수는 총 \"' + str(Sum) +'\"명인데요!'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"그 중"
    )
    time.sleep(0.5)


    if (birth >= tod and birth >= door and birth >= animal and birth >= photo and birth >= number):
        Max = birth
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u'타로테마의 생일점 이용자 수가 \"' + str(Max) + '\"명으로 가장 인기가 많네요!'
        )
        time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u"이 메뉴를 바로 이용해 보고 싶으시다면 /taro_b 를 눌러주세요!"
        )
        time.sleep(0.5)
        count+=1
    if (tod >= birth and tod >= door and tod >= animal and tod >= photo and tod >= number):
        Max = tod
        if(count!=0):
            bot.send_message(
                chat_id=query.message.chat_id,
                message_id=query.message.message_id,
                text=u"그리고 공동으로"
            )
            time.sleep(0.5)
        bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u'타로테마의 오늘의 운세 이용자 수가 \"' + str(Max) + '\"명으로 가장 인기가 많네요!'
        )
        time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u"이 메뉴를 바로 이용해 보고 싶으시다면 /taro_d 를 눌러주세요!"
        )
        time.sleep(0.5)
        count += 1
    if (door >= birth and door >= tod and door >= animal and door >= photo and door >= number):
        Max = door
        if (count != 0):
            bot.send_message(
                chat_id=query.message.chat_id,
                message_id=query.message.message_id,
                text=u"그리고 공동으로"
            )
            time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u'심리테마의 문 메뉴 이용자 수가 \"' + str(Max) + '\"명으로 가장 인기가 많네요!'
        )
        time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u"이 메뉴를 바로 이용해 보고 싶으시다면 /door 를 눌러주세요!"
        )
        time.sleep(0.5)
        count += 1
    if (animal >= birth and animal >= tod and animal >= door and animal >= photo and animal >= number):
        Max = animal
        if (count != 0):
            bot.send_message_(
                chat_id=query.message.chat_id,
                message_id=query.message.message_id,
                text=u"그리고 공동으로"
            )
            time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u'심리테마의 동물 메뉴 이용자 수가 \"' + str(Max) + '\"명으로 가장 인기가 많네요!'
        )
        time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u"이 메뉴를 바로 이용해 보고 싶으시다면 /animal 를 눌러주세요!"
        )
        time.sleep(0.5)
        count += 1
    if (photo >= birth and photo >= tod and photo >= door and photo >= animal and photo >= number):
        Max = photo
        if (count != 0):
            bot.send_message(
                chat_id=query.message.chat_id,
                message_id=query.message.message_id,
                text=u"그리고 공동으로"
            )
            time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u'심리테마의 사진 메뉴 이용자 수가 \"' + str(Max) + '\"명으로 가장 인기가 많네요!'
        )
        time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u"이 메뉴를 바로 이용해 보고 싶으시다면 /photo 를 눌러주세요!"
        )
        time.sleep(0.5)
        count += 1
    if (number >= birth and number >= tod and number >= door and number >= animal and number >= photo):
        Max = number
        if (count != 0):
            bot.send_message(
                chat_id=query.message.chat_id,
                message_id=query.message.message_id,
                text=u"그리고 공동으로"
            )
            time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u'심리테마의 숫자 메뉴 이용자 수가 \"' + str(Max) + '\"명으로 가장 인기가 많네요!'
        )
        time.sleep(0.5)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u"이 메뉴를 바로 이용해 보고 싶으시다면 /number 를 눌러주세요!"
        )
        time.sleep(0.5)
        count += 1

    #bot.sendMessage(chat_id=update.message.chat_id, text='추천드려요~~')
    #time.sleep(1.0)


    time.sleep(1.0)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"또다른 궁금한 사항이 있다면 /question 을 눌러주세요~"
    )



# 세부사항

def detail(bot, update):
    query = update.callback_query

    print("detail")

    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"각 테마별 이용자 수를 알고 싶으시다구요?"
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"걱정하지 마세요! 제가 알려 드릴게요!!"
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'저희 타로심리봇 이용 횟수는 총 \"' + str(Sum) + '\"명인데요!'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"그 중"
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'생일점 이용자 수는 \"' + str(birth) + '\"명'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'오늘의 운세 이용자 수는 \"' + str(tod) + '\"명'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'문 메뉴 이용자 수는 \"' + str(door) + '\"명'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'동물 메뉴 이용자 수는 \"' + str(animal) + '\"명'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'사진 메뉴 이용자 수는 \"' + str(photo) + '\"명'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u'숫자 메뉴 이용자 수는 \"' + str(number) + '\"명'
    )
    time.sleep(0.5)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"입니다! 더 다양한 메뉴들 많이 이용해주세요~"
    )
    time.sleep(1.0)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"또다른 궁금한 사항이 있다면 /question 을\n어떤 메뉴를 고릴지 결정하셨다면 /test 를 눌러주세요~"
    )




# 메인 함수
if __name__ == '__main__':
    bot.sendMessage(chat_id=chat_id, text='안녕 나는 타로, 심리 봇이야. 시작하기를 원하면 /start 를 눌러')

    conv_handler1 = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            TEST: [CallbackQueryHandler(test)],
        },
        fallbacks=[CommandHandler('start', start)]
    )


    conv_handler2 = ConversationHandler(
        entry_points=[CallbackQueryHandler(callback_get)],
        states={
            REALTARO: [CallbackQueryHandler(realtaro)],
            MENU: [CallbackQueryHandler(test_menu)],
            QA: [CallbackQueryHandler(question)],
            USER: [CallbackQueryHandler(user)],
            RECOMMAND: [CallbackQueryHandler(recommand)],
            DETAIL: [CallbackQueryHandler(detail)],
            TARO_B: [CallbackQueryHandler(taro_b)],
            TARO_D: [CallbackQueryHandler(taro_d)],
            DOOR: [CallbackQueryHandler(door1)],
            ANIMAL: [CallbackQueryHandler(crawl_animal)],
            PICTURE: [CallbackQueryHandler(picture)],
            NUMBER: [CallbackQueryHandler(number_check)],
            GREEN: [CallbackQueryHandler(green)],
            BLUE: [CallbackQueryHandler(blue)],
            RED: [CallbackQueryHandler(red)],
            PURPLE: [CallbackQueryHandler(purple)],
            GREY: [CallbackQueryHandler(grey)],
            A: [CallbackQueryHandler(a)],
            B: [CallbackQueryHandler(b)],
            C: [CallbackQueryHandler(c)],
            D: [CallbackQueryHandler(d)],
            CANCEL: [CallbackQueryHandler(cancel)]
        },
        fallbacks=[CallbackQueryHandler(callback_get)]
    )


    updater.dispatcher.add_handler(conv_handler1)
    updater.dispatcher.add_handler(conv_handler2)
    dp.add_handler(CommandHandler('sum', sum))

    dp.add_handler(CommandHandler('today', today))

    dp.add_handler(CommandHandler('yes', yes))

    dp.add_handler(CommandHandler('yes2', yes2))

    dp.add_handler(CommandHandler('yes3', yes3))

    dp.add_handler(CommandHandler('yes4', yes4))

    dp.add_handler(MessageHandler(Filters.text, get_message))



    updater.start_polling(timeout=3, clean=True)

    updater.idle()