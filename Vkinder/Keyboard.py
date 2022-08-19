import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from Vkinder.config import group_token


vk_session = vk_api.VkApi(token=group_token)
vk = vk_session.get_api()


def start(user_id: int, message):
    start_keyboard = VkKeyboard(one_time=True)
    start_keyboard.add_button('Start', color=VkKeyboardColor.POSITIVE)
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        keyboard=start_keyboard.get_keyboard(),
        message=message
    )


def search_button(user_id: int, message):
    search_buttons = VkKeyboard(one_time=False)
    search_buttons.add_button('Search', color=VkKeyboardColor.POSITIVE)
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        keyboard=search_buttons.get_keyboard(),
        message=message
    )


def next_button(user_id: int):
    next_buttons = VkKeyboard(one_time=False)
    next_buttons.add_button('Next', color=VkKeyboardColor.PRIMARY)
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        keyboard=next_buttons.get_keyboard(),
        message='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    )
