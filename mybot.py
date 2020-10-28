import time
import telebot
from telebot import types


pumpStart = "CAACAgIAAxkBAAEBfZBfkor728WtYLSKWedo99vpK6FhwgACnwIAAsxUSQk_aObxhqH53BsE"
pumpScary = "CAACAgIAAxkBAAEBfZJfkotKEKXGqLitG48IJyxSUPIYmgACmQIAAsxUSQncybHvbbp9UhsE"
pumpCongrats = "CAACAgIAAxkBAAEBfZRfkpN5-G_Yru1BAr-6TPy7OYSCBQACSQEAAladvQp1bSI3184pVBsE"
utyaClown = "CAACAgIAAxkBAAEBfqhfk-YpXiz7BMoRbngQ_ecX1S4smgACqAIAAladvQq3JSWRBwLaGxsE"
pumpBat = "CAACAgIAAxkBAAEBfqpfk-eNftzJLJC6GcpuhZFD0uQaHwACewEAAjDUnRF6pcpNH1twzBsE"
idshka = -417453928
bot = telebot.TeleBot("xxxxx")
winners=[]

@bot.message_handler(commands=["start"])
def starting(msg):
    try:
        current_nick = "@"+str(msg.from_user.username)
        if  current_nick not in winners:
            knopka = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            knopka.add("Да")
            bot.send_message(msg.chat.id, "Приветствую тебя, " + msg.from_user.first_name + "!")
            bot.send_sticker(msg.chat.id, pumpStart)
            mes = bot.send_message(msg.chat.id,
                             "🎃 Вот и настал жуткий праздник Хэллоуин! 🎃\n" +
                             'Три главных "к" на Хэллоуин - это костюмы, конфеты и... кристаллы)\n\n' +
                             'Сейчас у тебя есть возможность заработать 5💎 кристаллов.\n' +
                             'Чтобы их получить, совсем не нужно стучаться в двери с фразой "Кристаллы или жизнь?" 🧙🏻 \n' +
                             'Достаточно пройти небольшой квест - найти три кодовых слова.\n\n' +
                             'Ну что, поиграем? 👻', reply_markup=knopka)
            bot.register_next_step_handler(mes, quest_start)
        else:
            bot.send_message(msg.chat.id, "Квест пройден. Поздравляю!")
    except:
        bot.send_message(msg.chat.id, "Что-то пошло не так.")
        # bot.send_message(idshka, "Технические неполадки. Что-то пошло не так.")


def quest_start(msg):
    try:
        if msg.text==None:
            bot.register_next_step_handler(msg, quest_start)
        elif msg.text.lower().strip()!=None and msg.text.lower().strip() == "да":
            bot.send_message(msg.chat.id, "Отлично!")
            bot.send_sticker(msg.chat.id, pumpScary)
            mes = bot.send_message(msg.chat.id,
                             "Первый секретный код ты можешь найти в одном из 📚 домашних заданий.\n" +
                             "Внимательно просмотри задания, выданные преподавателями, и отправь мне кодовое слово.\n")
            bot.register_next_step_handler(mes, first_check)
        else:
            mes = bot.send_message(msg.chat.id, 'А, может, скажешь мне "Да"? :c')
            bot.register_next_step_handler(mes, quest_start)
    except:
        bot.send_message(msg.chat.id, "Что-то пошло не так.")
    # bot.send_message(idshka, "Технические неполадки. Что-то пошло не так.")


def first_check(msg):
    try:
        if msg.text==None:
            bot.register_next_step_handler(msg, first_check)
        else:
            ans = msg.text.lower().strip()
            if ans!=None and (ans == "пеннивайз"\
                    or ans == "пенивайз"\
                    or ans == "пэннивайз"\
                    or ans == "пэнивайз"):
                bot.send_message(msg.chat.id, "А ты молодец! Еще немного и кристаллы у тебя в кармане.")
                bot.send_sticker(msg.chat.id, utyaClown)
                mes = bot.send_message(msg.chat.id, "Для того, чтобы найти второй код, загляни в коридор.\n" +
                                              "Нет, не у тебя дома, а на нашем Дискорд-сервере)\n\n" +
                                              "Проявив внимательность 🕵🏻, ты легко его найдешь.\n" +
                                              "Как найдешь, отправляй сюда.")
                bot.register_next_step_handler(mes, second_check)
            else:
                mes = bot.send_message(msg.chat.id, "Не то. Будь внимательней в поисках и попробуй еще раз.")
                bot.register_next_step_handler(mes, first_check)
    except:
        mes = bot.send_message(msg.chat.id, "Что-то пошло не так.")
        bot.register_next_step_handler(mes, first_check)
        # bot.send_message(idshka, "Технические неполадки. Что-то пошло не так.")


def second_check(msg):
    try:
        if msg.text==None:
            bot.register_next_step_handler(msg, second_check)
        else:
            ans = msg.text.lower().strip()
            if ans!=None and (ans == "фредди крюгер"\
                    or ans == "фреди крюгер"\
                    or ans == "фрэдди крюгер" \
                    or ans == "фрэди крюгер" \
                    or ans == "крюгер"):
                bot.send_message(msg.chat.id, "Да ты монстр!🔥 Ты уже на финишной прямой, от кристаллов тебя отделяет всего один ответ.")
                bot.send_sticker(msg.chat.id, pumpBat)
                mes = bot.send_message(msg.chat.id, "Введи дату основания Компьютерной Академии Шаг в г. Алматы. Отправляй в таком формате: 1 января 2020.")
                bot.register_next_step_handler(mes, third_check)
            else:
                mes = bot.send_message(msg.chat.id, "Неверно. Давай, ты сможешь.")
                bot.register_next_step_handler(mes, second_check)
    except:
        mes = bot.send_message(msg.chat.id, "Что-то пошло не так.")
        bot.register_next_step_handler(mes, second_check)
        # bot.send_message(idshka, "Технические неполадки. Что-то пошло не так.")


def third_check(msg):
    try:
        if msg.text==None:
            bot.register_next_step_handler(msg, third_check)
        else:
            ans = msg.text.lower().strip()
            if ans!=None and (ans == "10 октября 2013" or ans == "10.10.2013" or ans == "10.10.13"):
                bot.send_message(msg.chat.id, "УРА! Теперь ты победитель! 🎉🎉🎉\n"+
                                    "\nЧтобы получить свои 5 кристаллов, отправь скриншот этого победного сообщения в учебную часть - @Itstepalmaty.\n\n"+
                                    "Ты молодчина! Спасибо за игру! 👻")
                bot.send_sticker(msg.chat.id, pumpCongrats)
                winner_nick = "@" + str(msg.from_user.username)
                winner_name = msg.from_user.first_name+" "+msg.from_user.last_name
                bot.send_message(idshka, "+1 победитель: " + str(winner_nick) + " - " + str(winner_name))
                if winner_nick == "@None":
                    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                    send_num = types.KeyboardButton("Отправить свой контакт", request_contact=True)
                    kbrd.add(send_num)
                    mes = bot.send_message(msg.chat.id, "Жаль, что у тебя нет никнейма в телеграм( Не могу внести тебя в список победителей.", reply_markup=kbrd)
                    bot.register_next_step_handler(mes, get_contact)
                else:
                    global winners
                    winners.append(winner_nick)
                # cursor.execute("""INSERT INTO winners VALUES(?, ?)""", (winner_nick, winner_name))
                # db.commit()
            else:
                mes = bot.send_message(msg.chat.id, "Почти, попробуй еще раз.")
                bot.register_next_step_handler(mes, third_check)
    except:
        mes = bot.send_message(msg.chat.id, "Технические неполадки. Что-то пошло не так.")
        bot.register_next_step_handler(mes, third_check)

def get_contact(msg):
    if msg.contact!=None:
        while 1:
            try:
                winners.append(str(msg.contact.phone_number))
                break
            except:
                pass
        bot.send_message(msg.chat.id, "Спасибо! Поздравляю с победой.")
    else:
        mes = bot.send_message(msg.chat.id, "Ошибка.")
        bot.register_next_step_handler(mes, get_contact)


bot.polling()




