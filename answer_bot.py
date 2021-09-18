# -*- coding: utf-8 -*-
import json
import random
import vk_api
import config


import datetime as dt

from vk_api.longpoll import VkLongPoll, VkEventType


token = config.token
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def get_button(text, url):
    """Генерация диалоговой кнопки с текстом"""
    return {
        "action": {
            "type": 'open_link',
            "link": url,
            "label": f'{text}'
        }
    }


def random_id():
    """Генерация случайного ID"""
    random_id = 0
    random_id += random.randint(0, 10000000)
    return random_id


def sender(id_user, text, attachment='', keyboard=''):
    """Отправка сообщения пользователю"""
    session_api.messages.send(
        user_id=id_user,
        message=text,
        attachment=attachment,
        keyboard=keyboard,
        random_id=random_id()
    )


for event in longpoll.listen():
    """Получение ивента в Long Poll"""
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        id_user = event.user_id
        if msg == 'начать':
            text = config.messages['hello']
            keyboard = {
                "buttons": [
                    [
                        get_button('KinoPoisk', config.kinopoisk_url),
                        get_button('Shikimori', config.shikimori_url)
                    ]
                ],
                "inline": True
            }
            keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))
            sender(id_user, text, keyboard=keyboard)
        elif msg == 'разработчик':
            text = config.messages['creator']
            sender(id_user, text)
        else:
            text = config.messages['warning']
            sender(id_user, text)
