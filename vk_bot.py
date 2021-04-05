import random
import vk_api
import vk_access

import datetime as dt

from vk_api.longpoll import VkLongPoll, VkEventType


main_token = vk_access.token
vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


"""Генерация случайного ID"""


def random_id():
    random_id = 0
    random_id += random.randint(0, 10000000)
    return random_id


"""Отправка сообщения пользователю"""


def sender(id_user, text, attachment='', keyboard=''):
    session_api.messages.send(
        user_id=id_user,
        message=text,
        attachment=attachment,
        keyboard=keyboard,
        random_id=random_id()
    )


"""Получение ивента в Long Poll"""


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        id_user = event.user_id
        if msg == 'начать':
            text = 'Hello World'
            sender(id_user, text)