import telebot
import random

from telebot import types

bot = telebot.TeleBot(1284877651:AAGHVnO4VA0jBX7KZLOac8C7JNjEFFfbD4A)

name = ''
surname = ''
work = ''
kids = ''
rr = ''
age = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open ('pasha.webp','rb')


    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Как дела??')
    item3 = types.KeyboardButton('Шутка')
    item4 = types.KeyboardButton('Анкеты/Тест')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Добро пожаловать,{0.first_name}\nЯ - <b>{1.first_name})</b>, бот для тестирования'.format(message.from_user, bot.get_me()),parse_mode= 'html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == ('private') :
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Как дела??':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item4 = types.InlineKeyboardButton("Плохо", callback_data='bad')

            markup.add(item3, item4)

            bot.send_message(message.chat.id, 'Отлично! Как сам?', reply_markup=markup)

        elif message.text == 'Шутка':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Смешно', callback_data='fun')
            item2 = types.InlineKeyboardButton('Не смешно', callback_data='nofun')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Колобок повесился!', reply_markup=markup)

        elif message.text == 'Анкеты/Тест':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Пройти тест!', callback_data='test')
            item2 = types.InlineKeyboardButton('Анкеты', callback_data='ank')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Выбирайте!', reply_markup=markup)

        elif message.text == 'Пидр':
            bot.send_message(message.chat.id, 'ПОШЕЛ НАХУЙ!')
        elif message.text == 'Тест':
            bot.send_message(message.chat.id, 'Добро пожаловать на тест!\nКак вас зовут?')
            bot.register_next_step_handler(message, reg_name)
        elif message.text == 'тест':
            bot.send_message(message.chat.id, 'Добро пожаловать на тест!\nКак вас зовут?')
            bot.register_next_step_handler(message, reg_name)
        elif message.text == 'Test':
            bot.send_message(message.chat.id, 'Welcome to out test! What is your name?')
            bot.register_next_step_handler(message, reg_name1)
        elif message.text == 'test':
            bot.send_message(message.chat.id, 'Welcome to out test! What is your name?')
            bot.register_next_step_handler(message, reg_name1)
        elif message.text == 'Паспорт загран':
            paszgr = open ('paszgr.pdf', 'rd')


        else:
            bot.send_message(message.chat.id, "Команда введена некорректно!")

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у вас фамилия?")
    bot.register_next_step_handler(message, reg_surname)
def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Cколько вам лет?")
    bot.register_next_step_handler(message, reg_age)

def reg_age (message):
    global age
    age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message('Вводите цифрами!')

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = "Вам " + str(age) + 'лет? и тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
def reg_work(message):
    global work
    work = message.text
    bot.send_message(message.from_user.id, "У вас есть дети?\nесть/нет")
    bot.register_next_step_handler(message, reg_kids)
def reg_kids(message):
    global kids
    kids = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes2 = types.InlineKeyboardButton(text='Да', callback_data='yes3')
    keyboard.add(key_yes2)
    key_no2 = types.InlineKeyboardButton(text='Нет', callback_data='no3')
    keyboard.add(key_no2)
    question ='Вас зовут - ' + name + ' ' + surname + '. Вам ' + str(age) + 'лет, вы ' +work+', и у вас ' +kids+' дети'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


#ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION ENGLISH VERSION
def reg_name1(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "What is your surname?")
    bot.register_next_step_handler(message, reg_surname1)
def reg_surname1(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "How old are you?")
    bot.register_next_step_handler(message, reg_age1)
def reg_age1(message):
    global age
    age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message('Enter in numbers!')
    keyboard = types.InlineKeyboardMarkup()
    key_yes11 = types.InlineKeyboardButton(text='Yes', callback_data='yes11')
    keyboard.add(key_yes11)
    key_no11 = types.InlineKeyboardButton(text='No', callback_data='no11')
    keyboard.add(key_no11)
    question = "You are " + str(age) + ' years old? And your name is: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
def reg_work1(message):
    global work
    work = message.text
    bot.send_message(message.from_user.id, "Do you have children?\nwrite:'\nhave / dont have")
    bot.register_next_step_handler(message, reg_kids1)
def reg_kids1(message):
    global kids
    kids = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes22 = types.InlineKeyboardButton(text='Yes', callback_data='yes22')
    keyboard.add(key_yes22)
    key_no22 = types.InlineKeyboardButton(text='No', callback_data='no22')
    keyboard.add(key_no22)
    question ='Your name is - ' + name + ' ' + surname + '. You are ' + str(age) + 'years old, you are ' +work+', and you ' +kids+' kids'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)





def reg_rr(message):
    global rr
    rr = message.text







@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько!')
            if call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Значит ты пидр!')
            if call.data == 'fun':
                bot.send_message(call.message.chat.id, 'Поздравляю, у вас есть чувство юмора!')
            if call.data == 'nofun':
                bot.send_message(call.message.chat.id, 'Поздравляю, вы пидр!')
            if call.data == 'ank':
                bot.send_message(call.message.chat.id, 'Анкеты в базе отсутсвуют')
            if call.data == 'test':
                bot.send_message(call.message.chat.id,'Напишите слово "Тест" / Write "Test" ')
            if call.data == 'yes':
                bot.send_message(call.message.chat.id,'Приятно познакомиться, '+name)
                bot.send_message(call.message.chat.id,'Кем вы работаете?')
                bot.register_next_step_handler(call.message, reg_work)
            if call.data == 'no':
                bot.send_message(call.message.chat.id, 'Попробуем еще раз!')
                bot.send_message(call.message.chat.id,'Добро пожаловать на тест! Как вас зовут?')
                bot.register_next_step_handler(call.message, reg_name)
            if call.data == 'yes11':
                bot.send_message(call.message.chat.id, 'Nice to meet you, '+name)
                bot.send_message(call.message.chat.id, 'What is your profession?')
                bot.register_next_step_handler(call.message, reg_work1)
            if call.data == 'no11':
                bot.send_message(call.message.chat.id, 'Lets try again!"')
                bot.send_message(call.message.chat.id, 'Welcome to out test! What is your name?')
                bot.register_next_step_handler(call.message, reg_name1)






    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)