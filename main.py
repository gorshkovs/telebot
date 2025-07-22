import telebot

from telebot import types
import time

bot = telebot.TeleBot('8019074887:AAGZgIX9_60PnQtrhdjB_5hqncaMS9KmpHo')

# Первый уровень меню. пользователь начал диалог с ботом
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Одежда')
    btn2 = types.KeyboardButton('Обувь')
    btn3 = types.KeyboardButton('Аксессуары')
    btn4 = types.KeyboardButton('Контакты')
    markup.add(btn1,btn2,btn3, btn4)
    bot.send_message(message.chat.id, "Привет, выберите категорию.", reply_markup=markup)


# Пользователь выбрал раздел Одежда. перешел в меню раздела. 
# Здесь все варианты выбора кнопок из первого уровня меню

@bot.message_handler(content_types='text')
def start(message):
    if (message.text == 'Одежда'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1a = types.KeyboardButton('Футболки')
        btn2a = types.KeyboardButton('Шорты')
        btn3a = types.KeyboardButton('Вратарская форма')
        back = types.KeyboardButton('Назад')
        markup.add(btn1a,btn2a,btn3a, back)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
    elif (message.text == 'Обувь'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1b = types.KeyboardButton('Бутсы')
        btn2b = types.KeyboardButton('Футзалки')
        btn3b = types.KeyboardButton('Кроссовки')
        back = types.KeyboardButton('Назад')
        markup.add(btn1b,btn2b,btn3b, back)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
    elif (message.text == 'Аксессуары'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1c = types.KeyboardButton('Перчатки')
        btn2c = types.KeyboardButton('Мячи')
        btn3c = types.KeyboardButton('Щитки')
        back = types.KeyboardButton('Назад')
        markup.add(btn1c,btn2c,btn3c, back)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)

    elif (message.text == 'Контакты'):
        description = (
                "Адреса магазинов\n"
                "Санкт-Петербург: адрес\n"
                "Телефон магазина: +7 999 999 99 99\n\n"
                "Омск: адрес \n"
                "Телефон магазина: +7 999 999 99 99\n\n"
                "Соцеальные сети:\n"
                "Вконтакте: https://vk.com/jomaomsk\n"
                "Telegram: https://t.me/jomasiberia\n"
            )
        bot.send_message(message.chat.id, description)


# кнопка возвращяет на первое меню        
    elif (message.text == 'Назад'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Одежда')
        btn2 = types.KeyboardButton('Обувь')
        btn3 = types.KeyboardButton('Аксессуары')
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id, "Привет, выберите категорию.", reply_markup=markup)   



# 3 блока для менб радела одежда.
# пользователь выбрал Футболки во втором меню. ему на выбор предоставляются актуальные футболки                
    elif (message.text == 'Футболки'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        foot1 = types.KeyboardButton('Футболка Joma Gold VII')
        foot2 = types.KeyboardButton('Футболка 1')
        foot3 = types.KeyboardButton('Футболка 2')
        back1 = types.KeyboardButton('\u21A9 Назад')
        markup.add(foot1, foot2, foot3, back1)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)

# пользователь выбрал раздел шорты и попал в меню выбора товара
    elif (message.text == 'Шорты'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        short1 = types.KeyboardButton('Шорты 1')
        short2 = types.KeyboardButton('Шорты 2')
        short3 = types.KeyboardButton('Шорты 3')
        back2 = types.KeyboardButton('\u21A9 Назад')
        markup.add(short1, short2, short3, back2)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
# пользователь выбрал раздел врт формы и попал в меню выбора товара
    elif (message.text == 'Вратарская форма'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        vrateq1 = types.KeyboardButton('Форма 1')
        vrateq2 = types.KeyboardButton('Форма 2')
        vrateq3 = types.KeyboardButton('Форма 3')
        back3 = types.KeyboardButton('\u21A9 Назад')
        markup.add(vrateq1, vrateq2, vrateq3, back3)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)    
    elif (message.text == '\u21A9 Назад'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1a = types.KeyboardButton('Футболки')
        btn2a = types.KeyboardButton('Шорты')
        btn3a = types.KeyboardButton('Вратарская форма')
        back = types.KeyboardButton('Назад')
        markup.add(btn1a,btn2a,btn3a, back)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)


# 3 блока для менб раздела обувь
# пользователь выбрал раздел бутсы и попал в меню выбора товара
    elif (message.text == 'Бутсы'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bytsi1 = types.KeyboardButton('Бутсы 1')
        bytsi2 = types.KeyboardButton('Бутсы 2')
        bytsi3 = types.KeyboardButton('Бутсы 3')
        back4 = types.KeyboardButton('\U0001F519 Назад')
        markup.add(bytsi1, bytsi2, bytsi3, back4)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup) 
# пользователь выбрал раздел футзалки и попал в меню выбора товара
    elif (message.text == 'Футзалки'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        fuatzal1 = types.KeyboardButton('DRIS2301IN')
        fuatzal2 = types.KeyboardButton('DRIS2303IN')
        fuatzal3 = types.KeyboardButton('DRIS2309IN')
        fuatzal4 = types.KeyboardButton('MUNS2302IN')
        fuatzal5 = types.KeyboardButton('MUNS2328IN')
        fuatzal6 = types.KeyboardButton('MUNS2304IN')
        
        back4 = types.KeyboardButton('\U0001F519 Назад')
        markup.add(fuatzal1, fuatzal2, fuatzal3, fuatzal4, fuatzal5, fuatzal6, back4)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup) 
# пользователь выбрал раздел кроссовки и попал в меню выбора товара
    elif (message.text == 'Кроссовки'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        kross1 = types.KeyboardButton('Кроссовки 1')
        kross2 = types.KeyboardButton('Кроссовки 2')
        kross3 = types.KeyboardButton('Кроссовки 3')
        back4 = types.KeyboardButton('\U0001F519 Назад')
        markup.add(kross1, kross2, kross3, back4)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)         
    elif (message.text == '\U0001F519 Назад'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1b = types.KeyboardButton('Бутсы')
        btn2b = types.KeyboardButton('Футзалки')
        btn3b = types.KeyboardButton('Кроссовки')
        back = types.KeyboardButton('Назад')
        markup.add(btn1b,btn2b,btn3b, back)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)


# 3 блока условий для раздела аксессуары 
# пользователь перчатки выбрал раздел и попал в меню выбора товара
    elif (message.text == 'Перчатки'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        perch1 = types.KeyboardButton('Перчатки 1')
        perch2 = types.KeyboardButton('Перчатки 2')
        perch3 = types.KeyboardButton('Перчатки 3')
        back5 = types.KeyboardButton('\u23EE Назад')
        markup.add(perch1, perch2, perch3, back5)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup) 
# пользователь мячи выбрал раздел и попал в меню выбора товара
    elif (message.text == 'Мячи'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        boal1 = types.KeyboardButton('Мячи 1')
        boal2 = types.KeyboardButton('Мячи 2')
        boal3 = types.KeyboardButton('Мячи 3')
        back5 = types.KeyboardButton('\u23EE Назад')
        markup.add(boal1, boal2, boal3, back5)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup) 
# пользователь щетки выбрал раздел и попал в меню выбора товара
    elif (message.text == 'Щитки'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        chetki1 = types.KeyboardButton('Щитки 1')
        chetki2 = types.KeyboardButton('Щитки 2')
        chetki3 = types.KeyboardButton('Щитки 3')
        back5 = types.KeyboardButton('\u23EE Назад')
        markup.add(chetki1, chetki2, chetki3, back5)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup) 
    elif (message.text == '\u23EE Назад'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1c = types.KeyboardButton('Перчатки')
        btn2c = types.KeyboardButton('Мячи')
        btn3c = types.KeyboardButton('Щитки')
        back = types.KeyboardButton('Назад')
        markup.add(btn1c,btn2c,btn3c, back)
        bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)



### пользователь выбрал футболку. он должен получить в ответ: фотографии футболок, полное название, цену,
# описание товара, варианты цветов, вывести 2 кнопки с телефоном и id менеджера.        

# товары в разделе футболки    
    elif (message.text == 'Футболка Joma Gold VII'):
        photo1 = open('media/t-shorts/gold 7/1.jpg', 'rb')
        photo2 = open('media/t-shorts/gold 7/2.jpg', 'rb')
        photo3 = open('media/t-shorts/gold 7/3.jpg', 'rb')

        try:
            media = [
                types.InputMediaPhoto(photo1),
                types.InputMediaPhoto(photo2),
                types.InputMediaPhoto(photo3)
            ]
            
            bot.send_media_group(message.chat.id, media)
            #time.sleep(0.5)
            description = (
                "CAMISETA MANGA CORTA GOLD VII NEGRO BLANCO\n"
                "Артикул: 104488.102\n"
                "Размеры: S, M, L, XL, 2XL\n"
                "Цена: 5126 руб. \n\n"
                "Рубашка с короткими рукавами идеально подходит для занятий различными видами спорта, такими как футбол, баскетбол, гандбол, мини-футбол и другими.\n\n"
                "📞 Позвонить: +7 (923) 678-83-64\n"
            )
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("📨 Написать", url="https://t.me/shyctruk"))
            bot.send_message(
                message.chat.id,
                description,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        finally:
            photo1.close()
            photo2.close()
            photo3.close()

# раздел с футзалками            
    elif (message.text == 'DRIS2301IN'):
        photo1 = open('media/futzalki/DRIS2301IN/1.jpg', 'rb')
        photo2 = open('media/futzalki/DRIS2301IN/2.jpg', 'rb')
        photo3 = open('media/futzalki/DRIS2301IN/3.jpg', 'rb')

        try:
            media = [
                types.InputMediaPhoto(photo1),
                types.InputMediaPhoto(photo2),
                types.InputMediaPhoto(photo3)
            ]
            
            bot.send_media_group(message.chat.id, media)
            #time.sleep(0.5)
            description = (
                "Футзалки DRIBLING DRIS2301IN\n"
                "Артикул: DRIS2301IN\n"
                "Бренд: Joma\n"
                "Размеры: 39, 40, 40.5, 41, 42, 42.5, 43, 43.5, 44, 44.5, 45\n"
                "\u274CСтарая цена: 4990 руб. \n"
                "\u2714Новая цена: 3990 руб. \n\n"
                "Эта футзальная модель изготовлена ​​из прочных материалов и подходит для любого поля. С этой универсальной обувью любое место может стать футбольным полем. Воздухопроницаемость, устойчивость и сопротивление являются результатом идеального сочетания синтетического материала и сетчатой ​​сетки, из которой сделана верхняя часть.\n\n"
                "📞 Позвонить: +7 (923) 678-83-64\n"
            )
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("📨 Написать", url="https://t.me/shyctruk"))
            bot.send_message(
                message.chat.id,
                description,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        finally:
            photo1.close()
            photo2.close()
            photo3.close()


# второй товар в разделе футзалки
    elif (message.text == 'DRIS2303IN'):
        photo1 = open('media/futzalki/DRIS2303IN/1.jpg', 'rb')
        photo2 = open('media/futzalki/DRIS2303IN/2.jpg', 'rb')
        photo3 = open('media/futzalki/DRIS2303IN/3.jpg', 'rb')

        try:
            media = [
                types.InputMediaPhoto(photo1),
                types.InputMediaPhoto(photo2),
                types.InputMediaPhoto(photo3)
            ]
            
            bot.send_media_group(message.chat.id, media)
            #time.sleep(0.5)
            description = (
                "Футзалки DRIBLING DRIS2303IN\n"
                "Артикул: DRIS2303IN\n"
                "Бренд: Joma\n"
                "Размеры: 40, 40.5, 41, 42, 42.5, 43 43.5, 44, 44.5\n"
                "\u274CСтарая цена: 4990 руб. \n"
                "\u2714Новая цена: 3990 руб. \n\n"
                "Эта футзальная модель изготовлена ​​из прочных материалов и подходит для любого поля. С этой универсальной обувью любое место может стать футбольным полем. Воздухопроницаемость, устойчивость и сопротивление являются результатом идеального сочетания синтетического материала и сетчатой ​​сетки, из которой сделана верхняя часть.\n\n"
                "📞 Позвонить: +7 (923) 678-83-64\n"
            )
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("📨 Написать", url="https://t.me/shyctruk"))
            bot.send_message(
                message.chat.id,
                description,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        finally:
            photo1.close()
            photo2.close()
            photo3.close()          

# третий товар в разделе футзалки
    elif (message.text == 'DRIS2309IN'):
        photo1 = open('media/futzalki/DRIS2309IN/1.jpg', 'rb')
        photo2 = open('media/futzalki/DRIS2309IN/2.jpg', 'rb')
        photo3 = open('media/futzalki/DRIS2309IN/3.jpg', 'rb')

        try:
            media = [
                types.InputMediaPhoto(photo1),
                types.InputMediaPhoto(photo2),
                types.InputMediaPhoto(photo3)
            ]
            
            bot.send_media_group(message.chat.id, media)
            #time.sleep(0.5)
            description = (
                "Футзалки DRIBLING DRIS2309IN\n"
                "Артикул: DRIS2309IN\n"
                "Бренд: Joma\n"
                "Размеры: 42, 43, 44, 45\n"
                "\u274CСтарая цена: 4990 руб. \n"
                "\u2714Новая цена: 3990 руб. \n\n"
                "Эта футзальная модель изготовлена ​​из прочных материалов и подходит для любого поля. С этой универсальной обувью любое место может стать футбольным полем. Воздухопроницаемость, устойчивость и сопротивление являются результатом идеального сочетания синтетического материала и сетчатой ​​сетки, из которой сделана верхняя часть.\n\n"
                "📞 Позвонить: +7 (923) 678-83-64\n"
            )
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("📨 Написать", url="https://t.me/shyctruk"))
            bot.send_message(
                message.chat.id,
                description,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        finally:
            photo1.close()
            photo2.close()
            photo3.close()
# 4 товар в разделе футзалки
    elif (message.text == 'MUNS2302IN'):
        photo1 = open('media/futzalki/MUNS2302IN/1.jpg', 'rb')
        photo2 = open('media/futzalki/MUNS2302IN/2.jpg', 'rb')
        photo3 = open('media/futzalki/MUNS2302IN/3.jpg', 'rb')

        try:
            media = [
                types.InputMediaPhoto(photo1),
                types.InputMediaPhoto(photo2),
                types.InputMediaPhoto(photo3)
            ]
            
            bot.send_media_group(message.chat.id, media)
            #time.sleep(0.5)
            description = (
                "Футзалки JOMA MUNDIAL MUNS2302IN\n"
                "Артикул: MUNS2302IN\n"
                "Бренд: Joma\n"
                "Размеры: 42.5, 43, 43.5, 44, 44.5\n"
                "\u274CСтарая цена: 4990 руб. \n"
                "\u2714Новая цена: 3990 руб. \n\n"
                "Классическая модель, выполненная из комбинации кожи, замши и синтетических материалов, что обеспечивает лучший контакт с мячом и износостойкость.\n\n"
                "📞 Позвонить: +7 (923) 678-83-64\n"
            )
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("📨 Написать", url="https://t.me/shyctruk"))
            bot.send_message(
                message.chat.id,
                description,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        finally:
            photo1.close()
            photo2.close()
            photo3.close()

# 5 товар в разделе футзалки
    elif (message.text == 'MUNS2328IN'):
        photo1 = open('media/futzalki/MUNS2328IN/1.jpg', 'rb')
        photo2 = open('media/futzalki/MUNS2328IN/2.jpg', 'rb')
        photo3 = open('media/futzalki/MUNS2328IN/3.jpg', 'rb')

        try:
            media = [
                types.InputMediaPhoto(photo1),
                types.InputMediaPhoto(photo2),
                types.InputMediaPhoto(photo3)
            ]
            
            bot.send_media_group(message.chat.id, media)
            #time.sleep(0.5)
            description = (
                "Футзалки MUNDIAL MUNS2328IN\n"
                "Артикул: MUNS2328IN\n"
                "Бренд: Joma\n"
                "Размеры: 40, 40.5, 42, 42.5, 43, 43.5, 44\n"
                "\u274CСтарая цена: 4990 руб. \n"
                "\u2714Новая цена: 3990 руб. \n\n"
                "Классическая модель, выполненная из комбинации кожи, замши и синтетических материалов, что обеспечивает лучший контакт с мячом и износостойкость.\n\n"
                "📞 Позвонить: +7 (923) 678-83-64\n"
            )
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("📨 Написать", url="https://t.me/shyctruk"))
            bot.send_message(
                message.chat.id,
                description,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        finally:
            photo1.close()
            photo2.close()
            photo3.close()

# 6 товар в разделе футзалки
    elif (message.text == 'MUNS2304IN'):
        photo1 = open('media/futzalki/MUNS2304IN/1.jpg', 'rb')
        photo2 = open('media/futzalki/MUNS2304IN/2.jpg', 'rb')
        photo3 = open('media/futzalki/MUNS2304IN/3.jpg', 'rb')

        try:
            media = [
                types.InputMediaPhoto(photo1),
                types.InputMediaPhoto(photo2),
                types.InputMediaPhoto(photo3)
            ]
            
            bot.send_media_group(message.chat.id, media)
            #time.sleep(0.5)
            description = (
                "Футзалки JOMA MUNDIAL MUNS2304IN\n"
                "Артикул: MUNS2304IN\n"
                "Бренд: Joma\n"
                "Размеры: 39, 40, 40.5, 42.5, 43, 43.5, 44, 44.5\n"
                "\u274CСтарая цена: 4990 руб. \n"
                "\u2714Новая цена: 3990 руб. \n\n"
                "Классическая модель, выполненная из комбинации кожи, замши и синтетических материалов, что обеспечивает лучший контакт с мячом и износостойкость.\n\n"
                "📞 Позвонить: +7 (923) 678-83-64\n"
            )
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("📨 Написать", url="https://t.me/shyctruk"))
            bot.send_message(
                message.chat.id,
                description,
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        finally:
            photo1.close()
            photo2.close()
            photo3.close()





bot.polling(non_stop=True)