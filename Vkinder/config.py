# Данные от базы данных VK:
DATABASE = 'postgresql'
DRIVER = 'psycopg2'
PORT = 5432
HOST = 'localhost'
NAME = 'nl_vkk'
OWNER = 'test_oleg'
PASSWORD = ''


# Токены группы и пользователя:
group_token = ''
user_token = ''


def get_token(group_token, user_token):
    if group_token == '':
        group_token = input('Введите токен вашей группы в ВК: ')
    if user_token == '':
        user_token = input('Введите токен пользователя: ')
    return {'group_token': group_token, 'user_token': user_token}


token = get_token(group_token, user_token)
group_token = token['group_token']
user_token = token['user_token']
