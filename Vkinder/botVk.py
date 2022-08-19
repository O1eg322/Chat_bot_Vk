from Vkinder.main import bot
from Vkinder.database.function_db import user_data, Ones, found_data
from Vkinder import Keyboard


class Choice:
    def __init__(self, my_id):
        self.my_id = my_id
        self.dict_data = user_data.data_user_dict[my_id]
        self.reverse_sex = [0, 2, 1]

    def main_data(self):
        user_data.uid = self.my_id
        user_data.name = self.dict_data['name']
        Ones.add_user(user_data)

    def auto_search(self):
        user_data.uid = self.my_id
        user_data.name = self.dict_data['name']
        user_data.search_city = self.dict_data['city']
        user_data.search_sex = self.reverse_sex[self.dict_data['sex']]
        user_data.search_relation = self.dict_data['relation']
        user_data.search_age_min = self.dict_data['age'] - 2
        user_data.search_age_max = self.dict_data['age'] + 2
        Ones.add_user(user_data)

    def sampling_of_people(self):
        get_f = Ones.get_found()
        if get_f == 0:
            return ['Нет подходящих пар по критериям!', None]
        info_found = [
            f'{found_data.name}' 
            f'\n{found_data.person_date}'
            f'\nhttps://vk.com/id{found_data.person_id}'
            f'\n{found_data.person_status}',
            found_data.person_photo_id]

        return info_found

    def save_data(self, dict_user, rating_photo, photo):
        found_data.name = f'{dict_user["first_name"]} {dict_user["last_name"]}'
        found_data.user_id = self.my_id
        found_data.person_id = dict_user['id']
        try:
            if len(dict_user['bdate'].split('.')) == 3:
                found_data.person_date = dict_user['bdate']
        except ValueError:
            pass
        found_data.person_photo_id = photo
        found_data.person_status = dict_user['status']
        found_data.rating_ph = rating_photo
        Ones.add_found_info(found_data)

    def request(self, request, user_name, uid):
        if user_data.step == 0:
            if request.lower() in ['привет']:
                Keyboard.start(uid, f'Доброго времени суток, {user_name}, я готов тебе помочь!)')
                return ['Для поиска своей второй половинки кликни \"Start\"', None]
            elif request.lower() in ['начать', 'start']:
                user_data.step = 1
                Keyboard.search_button(uid, f'\n Жми на кнопку \"Search\"')
                return ['Помни о правилах поведения в чате!', None]
        elif user_data.step == 1:
            if request.lower() in ['поиск', 'search']:
                user_data.step = 3
                bot.write_msg(uid, 'Поиск половинки... \n Просматриваю подходящие варианты...', None)
                self.auto_search()
                Keyboard.next_button(uid)
                return bot.find_person(uid)
        elif user_data.step == 3:
            if request.lower() in ['дальше', 'далее', 'next']:
                Keyboard.next_button(uid)
                nn = self.sampling_of_people()
                if nn == ['К сожалению мне ничего не удалось подобрать для вас! :(', None]:
                    bot.write_msg(uid, "Пожалуйста, подождите... ", None)
                    return bot.find_person(uid)
                return nn
            else:
                return ['К сожалению я вас не понимаю! :(', None]