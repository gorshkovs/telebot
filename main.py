import telebot
from telebot import types
import json # Для кодирования/декодирования сложных callback_data
from flask import Flask
bot = telebot.TeleBot('8019074887:AAGZgIX9_60PnQtrhdjB_5hqncaMS9KmpHo') # Вставьте ваш токен

PREFIX_CATEGORY = "cat_"
PREFIX_SUBCATEGORY = "subcat_" # Новый префикс для подкатегорий
PREFIX_PRODUCT = "prod_"
PREFIX_ACTION = "act_" # Для действий типа "назад", "контакты"

ACTION_BACK_MAIN_MENU = "back_main"
ACTION_PRODUCT_SOON = "prod_soon"
ACTION_CONTACTS = "contacts"
ACTION_BACK_SHOES_MENU = "back_shoes" # Новое действие: назад в меню обуви

# Товары для Футзалок JOMA DRIBLING
DRIBLING_PRODUCTS = {
    'DRIS2301IN': "DRIS2301IN",
    'DRIS2303IN': "DRIS2303IN",
    'DRIS2309IN': "DRIS2309IN",
}

# Товары для Футзалок JOMA MUNDIAL
MUNDIAL_PRODUCTS = {
    'MUNS2302IN': "MUNS2302IN",
    'MUNS2328IN': "MUNS2328IN",
    'MUNS2304IN': "MUNS2304IN",
}

# --- Вспомогательные функции для создания Inline-клавиатур ---
def create_callback_data(prefix, value, reply_thread_id=None):
    """Создает JSON-строку для callback_data с учетом reply_thread_id."""
    data = {"p": prefix, "v": value}
    if reply_thread_id:
        data["t"] = reply_thread_id
    return json.dumps(data)

def parse_callback_data(json_data):
    """Парсит JSON-строку callback_data."""
    return json.loads(json_data)

def get_main_inline_markup(reply_thread_id=None):
    """Возвращает InlineKeyboardMarkup для основного меню."""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('Одежда', callback_data=create_callback_data(PREFIX_CATEGORY, "clothes", reply_thread_id)),
        types.InlineKeyboardButton('Обувь', callback_data=create_callback_data(PREFIX_CATEGORY, "shoes", reply_thread_id)),
        types.InlineKeyboardButton('Аксессуары', callback_data=create_callback_data(PREFIX_CATEGORY, "accessories", reply_thread_id)),
        types.InlineKeyboardButton('Контакты', callback_data=create_callback_data(PREFIX_ACTION, ACTION_CONTACTS, reply_thread_id))
    )
    return markup

def get_shoes_inline_markup(reply_thread_id=None):
    """
    Возвращает InlineKeyboardMarkup для подменю обуви.
    Теперь ведет к DRIBLING и MUNDIAL.
    """
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Футзалки JOMA DRIBLING', callback_data=create_callback_data(PREFIX_SUBCATEGORY, "dribling", reply_thread_id)),
        types.InlineKeyboardButton('Футзалки JOMA MUNDIAL', callback_data=create_callback_data(PREFIX_SUBCATEGORY, "mundial", reply_thread_id)),
        types.InlineKeyboardButton('\U0001F519 Назад', callback_data=create_callback_data(PREFIX_ACTION, ACTION_BACK_MAIN_MENU, reply_thread_id))
    )
    return markup

def get_dribling_shoes_inline_markup(reply_thread_id=None):
    """Возвращает InlineKeyboardMarkup для подменю Футзалки JOMA DRIBLING."""
    markup = types.InlineKeyboardMarkup(row_width=2)
    for code_key, code_value in DRIBLING_PRODUCTS.items():
        markup.add(types.InlineKeyboardButton(code_value, callback_data=create_callback_data(PREFIX_PRODUCT, code_key, reply_thread_id)))
    markup.add(types.InlineKeyboardButton('\U0001F519 Назад', callback_data=create_callback_data(PREFIX_ACTION, ACTION_BACK_SHOES_MENU, reply_thread_id)))
    return markup

def get_mundial_shoes_inline_markup(reply_thread_id=None):
    """Возвращает InlineKeyboardMarkup для подменю Футзалки JOMA MUNDIAL."""
    markup = types.InlineKeyboardMarkup(row_width=2)
    for code_key, code_value in MUNDIAL_PRODUCTS.items():
        markup.add(types.InlineKeyboardButton(code_value, callback_data=create_callback_data(PREFIX_PRODUCT, code_key, reply_thread_id)))
    markup.add(types.InlineKeyboardButton('\U0001F519 Назад', callback_data=create_callback_data(PREFIX_ACTION, ACTION_BACK_SHOES_MENU, reply_thread_id)))
    return markup

def get_product_soon_inline_markup(reply_thread_id=None):
    """Возвращает InlineKeyboardMarkup для случая 'Товар скоро появится'."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton('⬅️ Назад в меню', callback_data=create_callback_data(PREFIX_ACTION, ACTION_BACK_MAIN_MENU, reply_thread_id)))
    return markup

# --- Унифицированные функции для отправки/редактирования сообщений и медиа ---
def send_message_unified(chat_id, text, reply_markup=None, parse_mode=None, reply_to_message_id=None):
    """Унифицированная функция для отправки текстовых сообщений."""
    try:
        bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode,
            reply_to_message_id=reply_to_message_id
        )
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Ошибка при отправке сообщения: {e} в чат {chat_id}, reply_to_message_id: {reply_to_message_id}")

def edit_message_text_unified(chat_id, message_id, text, reply_markup=None, parse_mode=None):
    """Редактирует текст и клавиатуру существующего сообщения."""
    try:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Ошибка при редактировании текста сообщения {message_id} в чате {chat_id}: {e}")

def send_media_group_unified(chat_id, media, reply_to_message_id=None):
    """Унифицированная функция для отправки групп медиафайлов."""
    try:
        bot.send_media_group(
            chat_id=chat_id,
            media=media,
            reply_to_message_id=reply_to_message_id
        )
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Ошибка при отправке медиа группы: {e} в чат {chat_id}, reply_to_message_id: {reply_to_message_id}")

# --- ОБРАБОТЧИК ДЛЯ КОМАНДЫ /start ---
@bot.message_handler(commands=['start'])
def handle_start(message):
    """Обрабатывает команду /start."""
    # Определяем ID исходного комментария, если это комментарий канала
    initial_reply_thread_id = None
    if message.reply_to_message and \
       message.reply_to_message.forward_from_chat and \
       message.reply_to_message.forward_from_chat.type == 'channel':
        initial_reply_thread_id = message.message_id # ID самого сообщения /start

    markup = get_main_inline_markup(initial_reply_thread_id) # Передаем thread_id в кнопки
    
    send_message_unified(
        chat_id=message.chat.id,
        text="Привет! Выберите категорию, используя кнопки:",
        reply_markup=markup,
        reply_to_message_id=initial_reply_thread_id # Отвечаем на исходный комментарий
    )

# --- ОБРАБОТЧИК ДЛЯ ТЕКСТОВЫХ СООБЩЕНИЙ, НАЧИНАЮЩИХ РАБОТУ БОТА ---
@bot.message_handler(func=lambda message: any(word in message.text.lower() for word in ['бот', 'одежда', 'обувь', 'аксессуары' 'каталог', 'старт', 'начать']))
def handle_activation_words(message):
    """Обрабатывает активационные слова для запуска бота."""
    initial_reply_thread_id = None
    if message.reply_to_message and \
       message.reply_to_message.forward_from_chat and \
       message.reply_to_message.forward_from_chat.type == 'channel':
        initial_reply_thread_id = message.message_id # ID самого текстового сообщения

    markup = get_main_inline_markup(initial_reply_thread_id) # Передаем thread_id в кнопки
    send_message_unified(
        chat_id=message.chat.id,
        text="Привет! Выберите категорию, используя кнопки:",
        reply_markup=markup,
        reply_to_message_id=initial_reply_thread_id # Отвечаем на исходный текст
    )

# --- ОБРАБОТЧИК ДЛЯ ТЕКСТОВЫХ СООБЩЕНИЙ О ПОКУПКЕ ---
@bot.message_handler(func=lambda message: any(word in message.text.lower() for word in ['купить', 'покупка', 'заказать', 'цена']))
def handle_purchase_inquiry(message):
    """Обрабатывает запросы пользователя, связанные с покупкой."""
    initial_reply_thread_id = None
    if message.reply_to_message and \
       message.reply_to_message.forward_from_chat and \
       message.reply_to_message.forward_from_chat.type == 'channel':
        initial_reply_thread_id = message.message_id

    description = (
        "Контакты менеджеров\n\n"
        "Владислав:\n"
        "Телефон: +7 923 676-33-89\n"
        "Telegram: https://t.me/jomasiberia\n"
    )
    send_message_unified(
        chat_id=message.chat.id,
        text=description,
        reply_to_message_id=initial_reply_thread_id
    )

# --- ОБРАБОТЧИК ДЛЯ ВСЕХ ОСТАЛЬНЫХ ТЕКСТОВЫХ СООБЩЕНИЙ ---
@bot.message_handler(content_types='text')
def handle_unrecognized_text_messages(message):
    """Обрабатывает любые другие текстовые сообщения, на которые бот не должен отвечать автоматически."""
    pass # Бот не будет отвечать на эти сообщения

# --- ОБРАБОТЧИК ДЛЯ INLINE-КНОПОК (CallbackQuery) ---
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    """Обрабатывает нажатия на Inline-кнопки."""
    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id
    message_id_to_edit = call.message.message_id

    # Парсим данные из callback_data
    callback_data_parsed = parse_callback_data(call.data)
    
    # Извлекаем сохраненный reply_thread_id. Если его нет, то None (для приватного чата)
    reply_to_thread_id = callback_data_parsed.get("t")    
    
    prefix = callback_data_parsed["p"]
    value = callback_data_parsed["v"]

    # --- ЛОГИКА ОБРАБОТКИ НАЖАТИЙ КНОПОК ---
    if prefix == PREFIX_CATEGORY:
        if value == "clothes":
            markup = get_product_soon_inline_markup(reply_to_thread_id)
            edit_message_text_unified(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text="Раздел 'Одежда'. Товар скоро появится.",
                reply_markup=markup
            )
        elif value == "shoes":
            markup = get_shoes_inline_markup(reply_to_thread_id) # Теперь ведет к подменю DRIBLING/MUNDIAL
            edit_message_text_unified(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text="Раздел 'Обувь'. Выберите тип футзалок:",
                reply_markup=markup
            )
        elif value == "accessories":
            markup = get_product_soon_inline_markup(reply_to_thread_id)
            edit_message_text_unified(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text="Раздел 'Аксессуары'. Товар скоро появится.",
                reply_markup=markup
            )
    elif prefix == PREFIX_SUBCATEGORY: # Обработка новой подкатегории
        if value == "dribling":
            markup = get_dribling_shoes_inline_markup(reply_to_thread_id)
            edit_message_text_unified(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text="Футзалки JOMA DRIBLING. Выберите модель:",
                reply_markup=markup
            )
        elif value == "mundial":
            markup = get_mundial_shoes_inline_markup(reply_to_thread_id)
            edit_message_text_unified(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text="Футзалки JOMA MUNDIAL. Выберите модель:",
                reply_markup=markup
            )
    elif prefix == PREFIX_ACTION:
        if value == ACTION_CONTACTS:
            description = (
                "Адреса магазинов\n"
                "Санкт-Петербург: 7-я Красноармейская улица, 11\n"
                "Телефон магазина: +7‒950‒008‒10‒46|+7‒960‒990‒11‒55\n\n"
                "Омск: ул. Маршала Жукова, 101/1\n"
                "Телефон магазина: +7 (800) 201-06-19|+7 (923) 678-83-64\n\n"
                "Социальные сети:\n"
                "Вконтакте: https://vk.com/jomaomsk\n"
                "Telegram: https://t.me/jomasiberia\n"
            )
            send_message_unified(
                chat_id=chat_id,
                text=description,
                reply_to_message_id=reply_to_thread_id # Используем сохраненный ID
            )
        elif value == ACTION_BACK_MAIN_MENU:
            markup = get_main_inline_markup(reply_to_thread_id)
            edit_message_text_unified(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text="Возвращаюсь в главное меню. Выберите категорию:",
                reply_markup=markup
            )
        elif value == ACTION_BACK_SHOES_MENU: # Новое действие: назад в меню обуви
            markup = get_shoes_inline_markup(reply_to_thread_id)
            edit_message_text_unified(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text="Возвращаюсь в раздел 'Обувь'. Выберите тип футзалок:",
                reply_markup=markup
            )
        elif value == ACTION_PRODUCT_SOON:
            markup = get_main_inline_markup(reply_to_thread_id)
            edit_message_text_unified(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text="Возвращаюсь в главное меню. Выберите категорию:",
                reply_markup=markup
            )
    elif prefix == PREFIX_PRODUCT:
        product_code = value
        send_product_info(chat_id, product_code, reply_to_thread_id)
    else:
        markup = get_main_inline_markup(reply_to_thread_id)
        edit_message_text_unified(
            chat_id=chat_id,
            message_id=message_id_to_edit,
            text="Неизвестная команда. Пожалуйста, используйте кнопки меню.",
            reply_markup=markup
        )

# --- Функция для отправки информации о товаре ---
def send_product_info(chat_id, product_code, reply_to_message_id):
    """
    Отправляет фотографии и описание товара.
    Получает reply_to_message_id для привязки к нужной ветке.
    """
    photo_paths = []
    description = ""
    
    keyboard_contact = types.InlineKeyboardMarkup()
    keyboard_contact.add(types.InlineKeyboardButton("📨 Написать", url="https://t.me/shyctruk"))

    # Ваша логика для загрузки фото и описания в зависимости от product_code
    if product_code == 'DRIS2301IN':
        photo_paths = ['media/futzalki/DRIS2301IN/1.jpg', 'media/futzalki/DRIS2301IN/2.jpg', 'media/futzalki/DRIS2301IN/3.jpg']
        description = (
            "Футзалки DRIBLING DRIS2301IN\n"
            "Артикул: DRIS2301IN\n"
            "Бренд: Joma\n"
            "Размеры: 39, 40, 40.5, 41, 42, 42.5, 43, 43.5, 44, 44.5, 45\n"
            "\u274CСтарая цена: 4990 руб. \n"
            "\u2714Новая цена: 3990 руб. \n\n"
            "Эта футзальная модель изготовлена ​​из прочных материалов и подходит для любого поля. С этой универсальной обувью любое место может стать футбольным полем. Воздухопроницаемость, устойчивость и сопротивление являются результатом идеального сочетания синтетического материала и сетчатой ​​сетки, из которой сделана верхняя часть.\n\n"
            "📞 Позвонить: +7 923 676-33-89\n"
        )
    elif product_code == 'DRIS2303IN':
        photo_paths = ['media/futzalki/DRIS2303IN/1.jpg', 'media/futzalki/DRIS2303IN/2.jpg', 'media/futzalki/DRIS2303IN/3.jpg']
        description = (
            "Футзалки DRIBLING DRIS2303IN\n"
            "Артикул: DRIS2303IN\n"
            "Бренд: Joma\n"
            "Размеры: 40, 40.5, 41, 42, 42.5, 43 43.5, 44, 44.5\n"
            "\u274CСтарая цена: 4990 руб. \n"
            "\u2714Новая цена: 3990 руб. \n\n"
            "Эта футзальная модель изготовлена ​​из прочных материалов и подходит для любого поля. С этой универсальной обувью любое место может стать футбольным полем. Воздухопроницаемость, устойчивость и сопротивление являются результатом идеального сочетания синтетического материала и сетчатой ​​сетки, из которой сделана верхняя часть.\n\n"
            "📞 Позвонить: +7 923 676-33-89\n"
        )
    elif product_code == 'DRIS2309IN':
        photo_paths = ['media/futzalki/DRIS2309IN/1.jpg', 'media/futzalki/DRIS2309IN/2.jpg', 'media/futzalki/DRIS2309IN/3.jpg']
        description = (
            "Футзалки DRIBLING DRIS2309IN\n"
            "Артикул: DRIS2309IN\n"
            "Бренд: Joma\n"
            "Размеры: 42, 43, 44, 45\n"
            "\u274CСтарая цена: 4990 руб. \n"
            "\u2714Новая цена: 3990 руб. \n\n"
            "Эта футзальная модель изготовлена ​​из прочных материалов и подходит для любого поля. С этой универсальной обувью любое место может стать футбольным полем. Воздухопроницаемость, устойчивость и сопротивление являются результатом идеального сочетания синтетического материала и сетчатой ​​сетки, из которой сделана верхняя часть.\n\n"
            "📞 Позвонить: +7 923 676-33-89\n"
        )
    elif product_code == 'MUNS2302IN':
        photo_paths = ['media/futzalki/MUNS2302IN/1.jpg', 'media/futzalki/MUNS2302IN/2.jpg', 'media/futzalki/MUNS2302IN/3.jpg']
        description = (
            "Футзалки JOMA MUNDIAL MUNS2302IN\n"
            "Артикул: MUNS2302IN\n"
            "Бренд: Joma\n"
            "Размеры: 42.5, 43, 43.5, 44, 44.5\n"
            "\u274CСтарая цена: 4990 руб. \n"
            "\u2714Новая цена: 3990 руб. \n\n"
            "Классическая модель, выполненная из комбинации кожи, замши и синтетических материалов, что обеспечивает лучший контакт с мячом и износостойкость.\n\n"
            "📞 Позвонить: +7 923 676-33-89\n"
        )
    elif product_code == 'MUNS2328IN':
        photo_paths = ['media/futzalki/MUNS2328IN/1.jpg', 'media/futzalki/MUNS2328IN/2.jpg', 'media/futzalki/MUNS2328IN/3.jpg']
        description = (
            "Футзалки MUNDIAL MUNS2328IN\n"
            "Артикул: MUNS2328IN\n"
            "Бренд: Joma\n"
            "Размеры: 40, 40.5, 42, 42.5, 43, 43.5, 44\n"
            "\u274CСтарая цена: 4990 руб. \n"
            "\u2714Новая цена: 3990 руб. \n\n"
            "Классическая модель, выполненная из комбинации кожи, замши и синтетических материалов, что обеспечивает лучший контакт с мячом и износостойкость.\n\n"
            "📞 Позвонить: +7 923 676-33-89\n"
        )
    elif product_code == 'MUNS2304IN':
        photo_paths = ['media/futzalki/MUNS2304IN/1.jpg', 'media/futzalki/MUNS2304IN/2.jpg', 'media/futzalki/MUNS2304IN/3.jpg']
        description = (
            "Футзалки JOMA MUNDIAL MUNS2304IN\n"
            "Артикул: MUNS2304IN\n"
            "Бренд: Joma\n"
            "Размеры: 39, 40, 40.5, 42.5, 43, 43.5, 44, 44.5\n"
            "\u274CСтарая цена: 4990 руб. \n"
            "\u2714Новая цена: 3990 руб. \n\n"
            "Классическая модель, выполненная из комбинации кожи, замши и синтетических материалов, что обеспечивает лучший контакт с мячом и износостойкость.\n\n"
            "📞 Позвонить: +7 923 676-33-89\n"
        )
    elif product_code == 'Футболка Joma Gold VII':
        photo_paths = ['media/t-shorts/gold 7/1.jpg', 'media/t-shorts/gold 7/2.jpg', 'media/t-shorts/gold 7/3.jpg']
        description = (
            "CAMISETA MANGA CORTA GOLD VII NEGRO BLANCO\n"
            "Артикул: 104488.102\n"
            "Размеры: S, M, L, XL, 2XL\n"
            "Цена: 5126 руб. \n\n"
            "Рубашка с короткими рукавами идеально подходит для занятий различными видами спорта, такими как футбол, баскетбол, гандбол, мини-футбол и другими.\n\n"
            "📞 Позвонить: +7 923 676-33-89\n"
        )
    else:
        send_message_unified(
            chat_id=chat_id,
            text="Информация о товаре не найдена.",
            reply_to_message_id=reply_to_message_id
        )
        return

    # Отправка фотографий
    opened_photos = []
    try:
        media = []
        for path in photo_paths:
            photo_file = open(path, 'rb')
            opened_photos.append(photo_file)
            media.append(types.InputMediaPhoto(photo_file))
            
        send_media_group_unified(
            chat_id=chat_id,
            media=media,
            reply_to_message_id=reply_to_message_id
        )

        send_message_unified(
            chat_id=chat_id,
            text=description,
            reply_markup=keyboard_contact,
            parse_mode="Markdown",
            reply_to_message_id=reply_to_message_id
        )
    except Exception as e:
        print(f"Ошибка при отправке медиа или сообщения: {e}")
        send_message_unified(
            chat_id=chat_id,
            text="Произошла ошибка при загрузке информации о товаре.",
            reply_to_message_id=reply_to_message_id
        )
    finally:
        for f in opened_photos:
            f.close()

from flask import Flask
import threading

def run_bot():
    bot.polling(non_stop=True)

def run_web():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Bot is running on Render!'

    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# Запускаем бот и Flask параллельно
if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    run_web()
