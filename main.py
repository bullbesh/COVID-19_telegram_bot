from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

import datetime
import os

# ПЕРЕМЕННЫЕ ДЛЯ КЛАВИАТУРЫ

button_options = "Опции 💡"
button_info = "О боте 📕"
button_date = "Дата 🕘"
button_help = "Помощь ⚙"
button_vaccine = "Вакцина 💉"

# ФУНКЦИИ ДЛЯ КЛАВИАТУРЫ


def info(update: Updater, context: CallbackContext):
    from variable import info

    update.message.reply_text(text=info)


def date(update: Updater, context: CallbackContext):
    update.message.reply_text(
        text="Дата на данный момент:\n\n"
        + datetime.datetime.now().strftime("%d/%m/%Y"),
    )


def hlp(update: Updater, context: CallbackContext):
    from variable import hlp

    update.message.reply_text(text=hlp)


def options(update: Updater, context: CallbackContext):
    from variable import options

    update.message.reply_text(text=options)


# КОМАНДНЫЕ ФУНЦКИИ


def mask(update: Updater, context: CallbackContext):
    from variable import wearing_mask

    update.message.reply_text(text=wearing_mask)


def protect(update: Updater, context: CallbackContext):
    from variable import protect

    update.message.reply_text(text=protect)


def how(update: Updater, context: CallbackContext):
    from variable import how

    update.message.reply_text(text=how)


def risk(update: Updater, context: CallbackContext):
    photo = open("images/statistics.png", "rb")
    update.message.reply_photo(photo=photo)


def vaccine(update: Updater, context: CallbackContext):
    from variable import vaccine

    update.message.reply_text(text=vaccine)


def most_using_vaccine(update: Updater, context: CallbackContext):
    photo = open("images/top_countries.png", "rb")
    update.message.reply_photo(photo=photo)


def approved_vaccines(update: Updater, context: CallbackContext):
    photo = open("images/country_vaccine.jpg", "rb")
    update.message.reply_photo(photo=photo)


def vaccine_makers(update: Updater, context: CallbackContext):
    from variable import vaccine_makers

    update.message.reply_text(text=vaccine_makers)


def uk(update: Updater, context: CallbackContext):
    from variable import vaccine_uk

    photo = open("images/united_kingdom.png", "rb")
    update.message.reply_photo(photo=photo, caption=vaccine_uk)


def de(update: Updater, context: CallbackContext):
    from variable import vaccine_de

    photo = open("images/germany.png", "rb")
    update.message.reply_photo(photo=photo, caption=vaccine_de)


def ru(update: Updater, context: CallbackContext):
    from variable import vaccine_ru

    photo = open("images/russia.png", "rb")
    update.message.reply_photo(photo=photo, caption=vaccine_ru)


def us(update: Updater, context: CallbackContext):
    from variable import vaccine_us

    photo = open("images/usa.png", "rb")
    update.message.reply_photo(photo=photo, caption=vaccine_us)


def cn(update: Updater, context: CallbackContext):
    from variable import vaccine_cn

    photo = open("images/china.png", "rb")
    update.message.reply_photo(photo=photo, caption=vaccine_cn)


def ind(update: Updater, context: CallbackContext):
    from variable import vaccine_ind

    photo = open("images/india.png", "rb")
    update.message.reply_photo(photo=photo, caption=vaccine_ind)


# ФУНКЦИЯ ОБРАБОТКИ СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ И ДАЛЬНЕЙШИЙ ОТВЕТ


def msg_send(update: Updater, context: CallbackContext):
    text = update.message.text
    if text == button_info:
        return info(update=update, context=context)
    if text == button_date:
        return date(update=update, context=context)
    if text == button_options:
        return options(update=update, context=context)
    if text == button_help:
        return hlp(update=update, context=context)
    if text == button_vaccine:
        return vaccine(update=update, context=context)

    if text == "/mask":
        return mask(update=update, context=context)
    if text == "/how":
        return how(update=update, context=context)
    if text == "/protect":
        return protect(update=update, context=context)
    if text == "/risk":
        return risk(update=update, context=context)
    if text == "/most_using_vaccine":
        return most_using_vaccine(update=update, context=context)
    if text == "/approved_vaccines":
        return approved_vaccines(update=update, context=context)

    if text == "/vaccine_makers":
        return vaccine_makers(update=update, context=context)
    if text == "/vaccine_uk":
        return uk(update=update, context=context)
    if text == "/vaccine_de":
        return de(update=update, context=context)
    if text == "/vaccine_ru":
        return ru(update=update, context=context)
    if text == "/vaccine_us":
        return us(update=update, context=context)
    if text == "/vaccine_cn":
        return cn(update=update, context=context)
    if text == "/vaccine_ind":
        return ind(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=button_options), KeyboardButton(text=button_vaccine)],
            [
                KeyboardButton(text=button_date),
                KeyboardButton(text=button_info),
                KeyboardButton(text=button_help),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text="Используй навигационные кнопки ниже!", reply_markup=reply_markup
    )


# ОСНОВНАЯ ФУНКЦИЯ ДЛЯ ОТПРАВКИ СООБЩЕНИЙ БОТОМ


def main():
    updater = Updater(token=os.getenv("TOKEN"), use_context=True,)

    updater.dispatcher.add_handler(
        MessageHandler(filters=Filters.all, callback=msg_send)
    )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()


def main_print():
    print("Bot started")
