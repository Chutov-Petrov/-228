import telebot
from telebot import types
import telebot

BOT_API = '7862542822:AAHZb98VPleLDePavpNbLvpQNHEGXbJ9I04'

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])

def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Гайды по бравл старс', callback_data='BS')
    btn_help = types.InlineKeyboardButton(text='О боте', callback_data='help')
    markup.add(btn1, btn_help)
    file = open('images/превью.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)

@bot.callback_query_handler(func = lambda call:True)
def answer(call):
    if call.data == 'help':
        markup_help = types.InlineKeyboardMarkup()
        btn26 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        markup_help.add(btn26)
        bot.send_message(call.message.chat.id, '''
Бот помогает новичкам и олдам собрать своих персонажей для максимального импакта для актуальной версии игры. 
Позволяет выбрать карту и озакомиться с выбором персонажа для выбранной карты. 
Указаны наилучшие комбинации бойцов для выбранных вами карт.''', reply_markup=markup_help)

#Выбор режима
    if call.data == 'BS':
        markup2 = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton(text='Захват кристаллов', callback_data='Gems')
        btn3 = types.InlineKeyboardButton(text='Броулбол', callback_data='Browlball')
        btn4 = types.InlineKeyboardButton(text='Ограбление', callback_data='Ograb')
        btn_BSback = types.InlineKeyboardButton(text='Назад', callback_data='Back')
        markup2.add(btn2, btn3, btn4, btn_BSback)
        bot.send_message(call.message.chat.id, 'Выберите режим: \nПеред вами представленно 3 режима: \n-Захват кристалов - цель: захватить 10 кристалов и удержать 15 секунд \n-Броулбол - футбол \n-Ограбление - сломать вражеский сейф', reply_markup=markup2)

#Захват кристалов
    if call.data == 'Gems':
        markup3 = types.InlineKeyboardMarkup()
        btn10 = types.InlineKeyboardButton(text='О режиме', callback_data='help_gems')
        btn5 = types.InlineKeyboardButton(text='Роковая шахта', callback_data='RockMine')
        btn8 = types.InlineKeyboardButton(text='Кристальная аркада', callback_data='CArcade')
        btn9 = types.InlineKeyboardButton(text='Поганковая запядня', callback_data='PZ')
        btn_backgems = types.InlineKeyboardButton(text='Назад', callback_data='back_rezhim')
        markup3.add(btn10)
        markup3.add(btn5)
        markup3.add(btn8)
        markup3.add(btn9)
        markup3.add(btn_backgems)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup3)

    if call.data == 'help_gems':
        markup19 = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        markup19.add(btn7)
        caption = 'Первый режим, который доступен новичкам. Соревнуются две команды, по три человека в каждой. Главная цель — собрать на команду 10 и более кристаллов, а затем удержать их в течение 15 секунд. Отсчёт времени начнётся заново, если количество вражеских кристаллов упадёт до 9 и менее.'
        bot.send_message(call.message.chat.id, caption, reply_markup=markup19)
    
    if call.data == 'RockMine':
        markup4 = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/к.jpg', 'rb')
        markup4.add(btn7)
        caption = 'Правый фланг: Рико \nЛевый фланг: Мр. П. \nМид: Пайпер'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup4)

    if call.data == 'CArcade':
        markup5 = types.InlineKeyboardMarkup()
        btn10 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/аркада.jpg', 'rb')
        markup5.add(btn10)
        caption = 'Правый фланг: Поко \nЛевый фланг: Роза \nМид: Тара'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup5)

    if call.data == 'PZ':
        markup6 = types.InlineKeyboardMarkup()
        btn11 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/западня.jpg', 'rb')
        markup6.add(btn11)
        caption = 'Правый фланг: Кольт \nЛевый фланг: Джесси \nМид: Поко'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup6)

#Броулбол
    if call.data == 'Browlball':
        markup7 = types.InlineKeyboardMarkup()
        btn13 = types.InlineKeyboardButton(text='Трипл-дриблинг', callback_data='Td')
        btn14 = types.InlineKeyboardButton(text='Дворовый чемпионат', callback_data='BB')
        btn15 = types.InlineKeyboardButton(text='Пляжный воллейбол', callback_data='BBowl;')
        btn_backbb = types.InlineKeyboardButton(text='Назад',callback_data = 'BS')
        btn16 = types.InlineKeyboardButton(text='О режиме',callback_data = 'help_BB')
        markup7.add(btn16, btn13, btn14, btn15, btn_backbb,)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup7)

    if call.data == 'help_BB':
        markup19 = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        markup19.add(btn7)
        caption = 'Режим «Броулбол» в игре Brawl Stars работает так: в турнире участвуют две команды по три игрока в каждой. Цель — доставить мяч (который начинается в середине) к воротам противоположной команды и забить гол.'
        bot.send_message(call.message.chat.id, caption, reply_markup=markup19)

    if call.data == 'Td':
        markup8 = types.InlineKeyboardMarkup()
        btn16 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/Пляж.jpg', 'rb')
        markup8.add(btn16)
        caption = 'Правый фланг: Мортис \nЛевый фланг: Рико \nМид: Фрэнк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup8)

    if call.data == 'BB':
        markup9 = types.InlineKeyboardMarkup()
        btn17 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/Бэкбол.jpg', 'rb')
        markup9.add(btn17)
        caption = 'Правый фланг: Белль \nЛевый фланг: Мортис \nМид: Рико'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup9)

    if call.data == 'BBowl;':
        markup10 = types.InlineKeyboardMarkup()
        btn18 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/Вол.jpg', 'rb')
        markup10.add(btn18)
        caption = 'Правый фланг: Базз \nЛевый фланг: Меллоди \nМид: Динамайк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup10)

#Ограбление
    if call.data == 'Ograb':
        markup11 = types.InlineKeyboardMarkup()
        btn19 = types.InlineKeyboardButton(text='Надёжное укрытие', callback_data='Ty')
        btn20 = types.InlineKeyboardButton(text='Горячая кукуруза', callback_data='Gk')
        btn21 = types.InlineKeyboardButton(text='Большое озеро', callback_data='Bo')
        btn22 = types.InlineKeyboardButton(text='О режиме', callback_data='piska')
        btn_backog = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        markup11.add(btn22, btn19, btn20, btn21, btn_backog)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup11)

    if call.data == 'piska':
        markup20 = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        markup20.add(btn7)
        caption = 'В ограблении есть две команды, каждая из которых состоит из трёх игроков. На обеих сторонах карты есть сейф с 45 000 очками здоровья. Цель состоит в том, чтобы сламать вражеский сейф'
        bot.send_message(call.message.chat.id, caption, reply_markup=markup20)    

    if call.data == 'Ty':
        markup12 = types.InlineKeyboardMarkup()
        btn23 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/Ty.jpg', 'rb')
        markup12.add(btn23)
        caption = 'Правый фланг: Мортис \nЛевый фланг: Гейл \nМид: Фрэнк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup12)

    if call.data == 'Gk':
        markup13 = types.InlineKeyboardMarkup()
        btn24 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/Gk.jpg', 'rb')
        markup13.add(btn24)
        caption = 'Правый фланг: Мортис \nЛевый фланг:Кольт \nМид: Динамайк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup13)

    if call.data == 'Bo':
        markup14 = types.InlineKeyboardMarkup()
        btn25 = types.InlineKeyboardButton(text='Назад', callback_data='BS')
        file = open('images/Bo.jpg', 'rb')
        markup14.add(btn25)
        caption = 'Правый фланг: Ворон \nЛевый фланг: Рико \nМид: Фрэнк'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup14)

 
    elif call.data == 'Back':  
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Гайды по бравл старс', callback_data='BS')
        btn_help = types.InlineKeyboardButton(text='О боте', callback_data='help')
        markup.add(btn1, btn_help)
        file = open('images/превью.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, reply_markup=markup)
    
    elif call.data == 'back_map_gems':
        markup15 = types.InlineKeyboardMarkup()
        btn5 = types.InlineKeyboardButton(text='Роковая шахта', callback_data='RockMine')
        btn8 = types.InlineKeyboardButton(text='Кристальная аркада', callback_data='CArcade')
        btn9 = types.InlineKeyboardButton(text='Поганковая запядня', callback_data='PZ')
        markup15.add(btn5, btn8, btn9)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup15)
        btn6 = types.InlineKeyboardButton(text='Назад', callback_data='back_map_gems')

    elif call.data == 'back_bb_map':
        markup16 = types.InlineKeyboardMarkup()
        btn13 = types.InlineKeyboardButton(text='Трипл-дриблинг', callback_data='Td')
        btn14 = types.InlineKeyboardButton(text='Дворовый чемпионат', callback_data='BB')
        btn15 = types.InlineKeyboardButton(text='Пляжный воллейбол', callback_data='BBowl;')
        markup16.add(btn13, btn14, btn15)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup7)
        btn12 = types.InlineKeyboardButton(text='Назад', callback_data='Back')

    elif call.data == 'back_map_og':
        markup17 = types.InlineKeyboardMarkup()
        btn19 = types.InlineKeyboardButton(text='Надёжное укрытие', callback_data='Ty')
        btn20 = types.InlineKeyboardButton(text='Горячая кукуруза', callback_data='Gk')
        btn21 = types.InlineKeyboardButton(text='Большое озеро', callback_data='Bo')
        markup17.add(btn19, btn20, btn21)
        bot.send_message(call.message.chat.id, 'Выберите карту', reply_markup=markup11)

    elif call.data == 'back_rezhim':
        markup18 = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton(text='Захват кристаллов', callback_data='Gems')
        btn3 = types.InlineKeyboardButton(text='Броулбол', callback_data='Browlball')
        btn4 = types.InlineKeyboardButton(text='Ограбление', callback_data='Ograb')
        markup18.add(btn2, btn3, btn4)
        bot.send_message(call.message.chat.id, 'Выберите режим:', reply_markup=markup18)
        
storage = dict()

def init_storage(user_id):
    storage[user_id] = dict(attemp=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

bot.polling()
