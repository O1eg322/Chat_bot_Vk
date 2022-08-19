# Данные от базы данных VK:
DATABASE = 'postgresql'
DRIVER = 'psycopg2'
PORT = 5432
HOST = 'localhost'
NAME = 'nl_vkk'
OWNER = 'test_oleg'
PASSWORD = '12345'


# Токены группы и пользователя:
group_token = 'vk1.a._i7QmX8C_1xqKl_-IzacnoFPVDSc1dL1K6UsZjUVQI-1r63LKABGeK38FFtUihguzcknOg2AluIioNKjLw5qx4c4OlxcA6iTBM7_EW81psFJZE_GAysljMYtj1b9DxKrJDprod_9iVslrsj8rtbiO6PzDKUAnYBjx3MhKPRzPaJ-sOpWrWLgJ9XbtmMdlZ6d'
user_token = 'vk1.a.ET3ykTe61g5Uv5N3Vpq-Ozl1pj3XCYPUV8YHQxoeYSoc_mrSk0R2wbaEUf3BYMbHnkIPwqeatyvsYJyykS0-vMuY52Q4NBzEwqRPK_7uAGH9VegsjaYTrfliu9-0ySBGVxmoNm2R92GZ_0HymH9xDmkddL3Q2a-BhtsABP5vH34oBgBjHbKeM5VbqvZjP5H2'


def get_token(group_token, user_token):
    if group_token == '':
        group_token = input('Введите токен вашей группы в ВК: ')
    if user_token == '':
        user_token = input('Введите токен пользователя: ')
    return {'group_token': group_token, 'user_token': user_token}


token = get_token(group_token, user_token)
group_token = token['group_token']
user_token = token['user_token']
