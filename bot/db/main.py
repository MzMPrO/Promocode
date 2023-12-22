from bot.db.api import user_list, user_detail, promocode_detail, promocode_update, user_create, user_update, \
    region_list, history_create
from aiogram.types import InlineKeyboardButton

def check_user(chat_id):
    for i in user_list():
        if i.get("chat_id") == str(chat_id):
            return True
    return False


def register_user(user_id, full_name, phone_number, region):
    data = {
        "chat_id": user_id,
        "full_name": full_name,
        "phone_number": phone_number,
        "region": region
    }
    return user_create(data)


def get_balance(chat_id):
    data = user_detail(chat_id)
    return data.get('balance')


def check_promocode(promocode: str):
    if not promocode_detail(promocode).get("is_active"):
        return False
    return True


def activated_promocode(promocode: str, chat_id: str):
    promocode_update({"is_active": False}, promocode)
    history_create({"promocode": promocode, "user": chat_id})
    summa = float(promocode_detail(promocode).get('price')) + user_detail(chat_id).get('balance')
    user_update(chat_id, data={"balance": float(summa)})


def get_region_list():
    l = []
    for i in region_list():
        l.append([InlineKeyboardButton(i.get('name'), callback_data=i.get('name'))])
    return l
