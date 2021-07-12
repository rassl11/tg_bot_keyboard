import time

from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton


def start(update,context):
    user_id=update.message.chat_id
    inline_keyboard = [InlineKeyboardButton(text = 'Галерея',callback_data='gallery'),InlineKeyboardButton(text = 'Обо Мне',callback_data = 'about_me'),
    InlineKeyboardButton(text = 'Оценить Бота',callback_data='mark')]
    context.bot.send_message(chat_id = user_id,text = 'Добро пожаловать в мой бот',reply_markup = InlineKeyboardMarkup([inline_keyboard]))

def gallery(update,context):
    user_id = update.callback_query.from_user.id
    first_photo = [KeyboardButton(text = 'Фотография с кальяном')]
    second_photo = [KeyboardButton(text='Фотография с оленем')]
    third_photo = [KeyboardButton(text='Фотография с медведем')]
    fourth_photo = [KeyboardButton(text='Фотография с тигром')]
    context.bot.send_message(chat_id = user_id,text ="Выбери какую фотограю хочешь посмотреть",
                             reply_markup = ReplyKeyboardMarkup([first_photo,second_photo,third_photo,fourth_photo],resize_keyboard=True,one_time_keyboard=True))

def others_methods(update,context):
    text = update.message.text
    user_id = update.message.chat_id
    name = update.message.from_user.first_name


    if text == 'Фотография с кальяном':
        context.bot.send_photo(chat_id = user_id,
                               photo='https://avatars.mds.yandex.net/get-altay/1777247/2a0000016aed4b3710db9d56d20bec3138b3/XXL')
    elif text == 'Фотография с оленем':
        context.bot.send_photo(chat_id=user_id,
                               photo='https://fotovmire.ru/wp-content/uploads/2019/07/19556/olen-i-voron-v-pole.jpg')
    elif text == 'Фотография с медведем':
        context.bot.send_photo(chat_id=user_id,
                               photo='https://placepic.ru/wp-content/uploads/2018/11/fd2880eb2e0275bae3298bd231bd78de.jpg')
    elif text == 'Фотография с тигром':
        context.bot.send_photo(chat_id=user_id,
                               photo='https://ferma-biz.ru/wp-content/uploads/2021/03/Animals___Wild_cats_____The_face_of_a_tiger_042529_.jpg')
    else:
        datetime = time.asctime()
        Logpath = 'answers.txt'
        log = open(Logpath, 'a')
        logstr = "{} | user_id:{},  Имя:{},  отзыв: {} \n".format(datetime, user_id,name, text)
        log.writelines(logstr)





def about_me(update,context):
    user_id = update.callback_query.from_user.id
    context.bot.send_message(chat_id = user_id,text = """Держи информацию обо мне:
    Я был создан Расулом и BotFatherом 11.07.2021 пока что я мало что  умею, но вскоре мой фунционал увеличиться""")

def mark(update,context):
    user_id = update.callback_query.from_user.id
    context.bot.send_message(chat_id = user_id,text = "Оставь отзыв обо мне!!!")








