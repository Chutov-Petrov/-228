import telebot
from telebot import types
import telebot

BOT_API = '7862542822:AAHZb98VPleLDePavpNbLvpQNHEGXbJ9I04'

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])
@bot.message_handler(commands=['Help'])

def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Гайды по бравл старс', callback_data='BS')
    markup.add(btn1)
    file = open('превью.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)

def Help(message):
    markup = types.InlineKeyboardMarkup()
    caption = 'Бот помогает новичкам и олдам собрать своих персонажей для максимального импакта для актуальной версии игры. Позволяет выбрать карту и озакомиться с выбором персонажа для выбранной карты. Указаны наилучшие комбинации бойцов для выбранных вами карт.'
    bot.send_massage(message.chat.id, caption, reply_markup=markup)

@bot.callback_query_handler(func = lambda call:True)
def answer(call):
    if call.data == 'BS':
        markup2 = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton(text='Захват кристаллов', callback_data='Gems')
        btn3 = types.InlineKeyboardButton(text='Броулбол', callback_data='Browlball')
        btn4 = types.InlineKeyboardButton(text='Ограбление', callback_data='Ograb')
        markup2.add(btn2, btn3, btn4)
        bot.send_message(call.message.chat.id, 'Выберите режим:', reply_markup=markup2)

#Захват кристалов
    if call.data == 'Gems':
        markup3 = types.InlineKeyboardMarkup()
        btn5 = types.InlineKeyboardButton(text='Роковая шахта', callback_data='RockMine')
        btn8 = types.InlineKeyboardButton(text='Кристальная аркада', callback_data='CArcade')
        btn9 = types.InlineKeyboardButton(text='Поганковая запядня', callback_data='PZ')
        markup3.add(btn5)
        markup3.add(btn8)
        markup3.add(btn9)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup3)
        btn6 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
    
    if call.data == 'RockMine':
        markup4 = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('к.jpg', 'rb')
        markup4.add(btn7)
        caption = ' 1)правый фланг: Рико левый фланг:Мр. П. мид:Пайпер 2)правый фланг:Рико. левый фланг:Пайпер мид:Мортис. 3)правый фланг:Брок левый фланг:Эдгар мид:8-Бит'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup4)

    if call.data == 'CArcade':
        markup5 = types.InlineKeyboardMarkup()
        btn10 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('аркада.jpg', 'rb')
        markup5.add(btn10)
        caption = '1)правый фланг:Поко левый фланг:Роза мид:Тара  2)правый фланг:Джесси левый фланг:Нита мид:Поко 3)правый фланг:Джесси левый фланг:Мортис мид:Поко'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup5)

    if call.data == 'PZ':
        markup6 = types.InlineKeyboardMarkup()
        btn11 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('западня.jpg', 'rb')
        markup6.add(btn11)
        caption = '1)правый фланг:Кольт левый фланг:Джесси мид:Поко 2)правый фланг:Кольт левый фланг:Джесси мид:Мортис 3)первый фланг:Кольт левый фланг:Эдгар мид:Джесси'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup6)

#Броулбол
    if call.data == 'Browlball':
        markup7 = types.InlineKeyboardMarkup()
        btn13 = types.InlineKeyboardButton(text='Трипл-дриблинг', callback_data='Td')
        btn14 = types.InlineKeyboardButton(text='Дворовый чемпионат', callback_data='BB')
        btn15 = types.InlineKeyboardButton(text='Пляжный воллейбол', callback_data='BBowl;')
        markup7.add(btn13)
        markup7.add(btn14)
        markup7.add(btn15)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup7)
        btn12 = types.InlineKeyboardButton(text='Назад', callback_data='Back')

    if call.data == 'Td':
        markup8 = types.InlineKeyboardMarkup()
        btn16 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('Пляж.jpg', 'rb')
        markup8.add(btn16)
        caption = '1)правый фланг:Мортис левый фланг:рико мид:Фрэнк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup8)

    if call.data == 'BB':
        markup9 = types.InlineKeyboardMarkup()
        btn17 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('Бэкбол.jpg', 'rb')
        markup9.add(btn17)
        caption = '1)правый фланг:белль левый фланг:Мортис мид:рико'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup9)

    if call.data == 'BBowl;':
        markup10 = types.InlineKeyboardMarkup()
        btn18 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('Вол.jpg', 'rb')
        markup10.add(btn18)
        caption = '1)правый фланг:базз левый фланг:меллоди мид:динамайк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup10)

#Ограбление
    if call.data == 'Ograb':
        markup11 = types.InlineKeyboardMarkup()
        btn19 = types.InlineKeyboardButton(text='Надёжное укрытие', callback_data='Ty')
        btn20 = types.InlineKeyboardButton(text='Горячая кукуруза', callback_data='Gk')
        btn21 = types.InlineKeyboardButton(text='Большое озеро', callback_data='Bo')
        markup11.add(btn19)
        markup11.add(btn20)
        markup11.add(btn21)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup11)
        btn22 = types.InlineKeyboardButton(text='Назад', callback_data='Back')

    if call.data == 'Ty':
        markup12 = types.InlineKeyboardMarkup()
        btn23 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('Ty.jpg', 'rb')
        markup12.add(btn23)
        caption = '1)правый фланг:Мортис левый фланг:Гейл мид:Фрэнк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup12)

    if call.data == 'Gk':
        markup13 = types.InlineKeyboardMarkup()
        btn24 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('Gk.jpg', 'rb')
        markup13.add(btn24)
        caption = '1)правый фланг:Мортис левый фланг:Кольт мид:Динамайк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup13)

    if call.data == 'Bo':
        markup14 = types.InlineKeyboardMarkup()
        btn25 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        file = open('Ty.jpg', 'rb')
        markup14.add(btn25)
        caption = '1)правый фланг:Ворон левый фланг:рико мид:Фрэнк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup14)
        
    elif call.data == 'Back':  
        bot.edit_message_text(call.message.chat.id, call.message.message_id, reply_markup=start(call.message))

storage = dict()

def init_storage(user_id):
    storage[user_id] = dict(attemp=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

bot.polling()
