import telebot
from telebot import types
import  random

# токен для бота, типа API
bot = telebot.TeleBot('individual_token')

# Психологи
psyhologs = ["Евгений Геннадьевич +7 777 745 4859", "Рустем Нурланов +7 705 4546", "Омар Таймасулы +7 708 969 1312",
             "Артем  +7 705 555 1616", "телефон доверия +7 495 122 32 77"
            ]
# Отделение полиции
polic = ["Желтоқсан 19/2", "улица Жақып Омаров, 53а, Нур-Султан", "Иманова, 21", "проспект Мәңгілік Ел, 55/4",
         "проспект Тәуелсіздік, 1", "Шоқан Уәлиханов, 24/3"
         ]

# Бастапкы мәндер
name = []


# главная функция, выполняется при нажатии кнопку start
@bot.message_handler(commands=['start'])
def start(message):
   mess = f'Как вас зовут?'
   bot.register_next_step_handler(message, year_step)
   bot.send_message(message.chat.id, mess)


def year_step(message):
   # имя
   print(message.text)
   name.append(message.text)
   bot.send_message(message.chat.id, "Введите ваш возраст: ")
   bot.register_next_step_handler(message, name_step)


# Есім енгізілген соң орындалатын функция
def name_step(message):
   print(message.text)
   markup = types.InlineKeyboardMarkup(row_width=1)
   item1 = types.InlineKeyboardButton("Психологическая помощь", callback_data="psyho")
   item2 = types.InlineKeyboardButton("Сексуальное насилие", callback_data="sexual")
   item3 = types.InlineKeyboardButton("Харасмент", callback_data="harasment")
   item4 = types.InlineKeyboardButton("Физическое насилие", callback_data="fiz")
   item5 = types.InlineKeyboardButton("Домашнее насилиe", callback_data="dom")
   item6 = types.InlineKeyboardButton("Другое ", callback_data="any")
   markup.add(item1)
   markup.add(item2)
   markup.add(item3)
   markup.add(item4)
   markup.add(item5)
   markup.add(item6)
   year = message.text
   name.append(year)
   mess = f'Здравствуйте {name[0]} чем могу вам помочь?'
   bot.send_message(message.chat.id, mess, reply_markup=markup)

   # Кнопка другого типа
   markupRep = types.ReplyKeyboardMarkup(resize_keyboard=True)
   ite = types.KeyboardButton("Срочная помощь")
   markupRep.add(ite)
   bot.send_message(message.chat.id, "Выберите одну", reply_markup=markupRep)

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
       if call.data == "psyho":
          mes = psi()
          bot.send_message(call.message.chat.id, "Телефон психологов: ")
          bot.send_message(call.message.chat.id, mes)
          bot.send_message(call.message.chat.id, "пожалуйста позаботьтесь о себе :)")
       elif call.data == "sexual" or call.data == "harasment" or call.data=="fiz" or call.data=="dom":
          bot.send_message(call.message.chat.id, "Ваш адрес?")
          bot.register_next_step_handler(call.message, adress_bar)
       elif call.data == "any":
          bot.send_message(call.message.chat.id, "Опишите вашу пробему :")
          bot.register_next_step_handler(call.message, problem)


# Егер қолданушы адрес енгізетін болса
def adress_bar(message):
   adres = message.text
   print(adres)
   # адрес полиции выбирается рандомно
   pol = "Самый ближайший адрес полиции "+ random.choice(polic)
   bot.send_message(message.chat.id, pol)
   mes = psi()
   bot.send_message(message.chat.id, "Телефон психологов: ")
   bot.send_message(message.chat.id, mes)
   bot.send_message(message.chat.id, "пожалуйста позаботьтесь о себе :)")


# Енгізілген сөздерді өңдеу
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Срочная помощь":
       bot.send_message(message.chat.id, "Телефонные номера экстренных служб: ")
       soz = """
       Пожарная служба --- 101
Полиция --- 102
Скорая мед. помощь ---103
Аварийная служба газа --- 104
       """
       bot.send_message(message.chat.id, soz)


def problem(message):
   # сохраним проблему пользователья для дальнейшего обработки
   problem_of_user = message.text
   print(problem_of_user)
   mes = "Отчет отправлен в виде:" + "\n" + "Имя: " + name[0] + "\n" + "Возраст: " + name[1] +"\n" + "Проблема: " + "\n"+ problem_of_user
   bot.send_message(message.chat.id, "Мы обязательно свяжемся с вами ")
   bot.send_message(message.chat.id,  mes)
   bot.send_message(message.chat.id, "пожалуйста позаботьтесь о себе :)")


# Псiхологтар тізімін қайтаратын функция
def psi():
   mes = ""
   for i in psyhologs:
      mes = mes + i + "\n"
   return  mes


# Программаны бастау
if __name__ == '__main__':
   bot.polling(none_stop=True)


