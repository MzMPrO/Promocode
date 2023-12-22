from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.button.text import *


def menu_rkm_button():
    desing = [
        ['Promocode kiritish', 'Balansingizni korish'],
    ]
    return ReplyKeyboardMarkup(keyboard=desing, one_time_keyboard=True, resize_keyboard=True)


def phone_btn():
    desing = [[KeyboardButton(text='Telefon nomeringizni yuborish', request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard=desing, one_time_keyboard=True, resize_keyboard=True)

def back_btn():
    desing = [['Back']]
    return ReplyKeyboardMarkup(keyboard=desing, one_time_keyboard=True, resize_keyboard=True)