from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.button.text import *
from bot.db.main import get_region_list


def region_choise_btn():
    return InlineKeyboardMarkup(inline_keyboard=get_region_list(), row_width=2)
