from _datetime import datetime
from random import randrange


import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from Vkinder import botVk
from Vkinder.database.function_db import user_data
from Vkinder.config import group_token, user_token
from vk_api.exceptions import ApiError



class BotVk:
    def __init__(self):
        print('Bot was created')
        self.token = group_token
        self.user_token = user_token
        self.vk = vk_api.VkApi(token=self.token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_session = vk_api.VkApi(token=self.user_token)
        self.vk_app = self.vk_session.get_api()

    def write_msg(self, id_to_send, message, photo):
        self.vk.method('messages.send', {
            'user_id': id_to_send,
            'message': message,
            'attachment': f'photo{photo}',
            'random_id': randrange(10 ** 9)
        })

    def write_to_chat(self, id_to_send, message, photo):
        self.vk.method('messages.send', {
            'chat_id': id_to_send,
            'message': message,
            'attachment': f'photo{photo}',
            'random_id': randrange(10 ** 9),
        })

    def viewed_chat(self):
        try:
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    print(event.user_id, event.text)
                    info_user = self.vk_app.users.get(user_ids=event.user_id,
                                                      fields=['bdate', 'city', 'sex', 'relation'])
                    user_data.uid = info_user[0]['id']
                    user_data.name = f"{info_user[0]['first_name']} {info_user[0]['last_name']}"
                    year = datetime.date(datetime.today()).year
                    user_data.age = year - int(info_user[0]['bdate'][-4:])
                    user_data.sex = info_user[0]['sex']
                    user_data.city = info_user[0]['city']['title']
                    user_data.relation = info_user[0]['relation']
                    user_data.create_data_dict()
                    select_data = botVk.Choice(event.user_id)

                    if event.to_me:
                        user = self.vk.method('users.get', {'user_ids': event.user_id})
                        if event.from_chat:
                            self.write_to_chat(event.chat_id, f'{user[0]["first_name"]}, '
                                                              f'Ответил в личные сообщения!', None)
                        request = select_data.request(event.text, user[0]['first_name'], user_data.uid)
                        answer = request[0]
                        photo = request[1]
                        if answer is not None and answer != '':
                            print(answer)
                            self.write_msg(event.user_id, answer, photo)
        except ValueError:
            print('No answer')
            self.viewed_chat()

    def find_person(self, uid):
        select_data = botVk.Choice(uid)
        find_user = self.vk_app.users.search(count=user_data.quant_query,
                                             hometown=user_data.search_city,
                                             sex=user_data.search_sex,
                                             status=user_data.search_relation,
                                             age_from=user_data.search_age_min,
                                             age_to=user_data.search_age_max,
                                             is_closed=False,
                                             fields=['is_closed', 'bdate', 'status', 'photo_max_orig', 'photo_id'])

        for dict_user in find_user['items']:
            if not dict_user['is_closed']:
                print(dict_user['id'], 'Пользователь добавлен в базу данных!')
                likes = 0
                comments = 0
                try:
                    photo = dict_user['photo_id']
                    likes = self.vk_app.likes.getList(
                        type='photo',
                        owner_id=dict_user['id'],
                        item_id=photo[-9:],
                    )['count']
                    try:
                        comments = self.vk_app.photos.getComments(
                            owner_id=dict_user['id'],
                            photo_id=photo[-9:],
                        )['count']
                    except ApiError:
                        comments = 0
                except ApiError:
                    photo = 'Нет фотографий'
                photo_rating = likes + comments
                select_data.save_data(dict_user, photo_rating, photo)
            else:
                print(dict_user['id'], ' - Закрытый профиль!')
        info_user = select_data.sampling_of_people()
        if info_user == ['Нет подходящих пар по критериям!', None]:
            info_user = self.find_person(uid)
            user_data.quant_query += 10

        return info_user

    def get_city(self, name_city):
        city_data = self.vk_app.database.getCities(country_id=1, q=name_city, need_all=1, count=15)
        user_data.city_count = city_data["count"]
        user_data.city_input_list = [i['title'] for i in city_data["items"]]


bot = BotVk()

if __name__ == '__main__':
    bot.viewed_chat()