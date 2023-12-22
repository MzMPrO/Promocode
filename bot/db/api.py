import requests

from bot.utils import WEB_URL


def region_list():
    return requests.get(f'{WEB_URL}/api/region-list/').json()


def user_list():
    return requests.get(f'{WEB_URL}/api/user-list/').json()


def user_create(data):
    return requests.post(f'{WEB_URL}/api/user-create/', data=data).status_code


def user_detail(chat_id):
    return requests.get(f'{WEB_URL}/api/user-detail-update/{chat_id}').json()


def user_update(chat_id, data):
    return requests.patch(url=f'{WEB_URL}/api/user-detail-update/{chat_id}/', data=data).status_code


def promocode_list():
    return requests.get(f'{WEB_URL}/api/promocode-list').json()


def promocode_update(data, promocode):
    return requests.patch(f'{WEB_URL}/api/promocode-update/{promocode}', data=data).status_code


def promocode_detail(promocode):
    return requests.get(f'{WEB_URL}/api/promocode-detail/{promocode}').json()


def history_create(data):
    return requests.post(f'{WEB_URL}/api/history-create/', data=data).status_code
