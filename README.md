# Техническое задание 

# Vkinder 

### 
Все слышали про известное приложение для знакомств - Tinder. Приложение предоставляет простой интерфейс для выбора понравившегося человека. Сейчас в Google Play более 100 миллионов установок.
###
Используя данные из VK, нужно сделать сервис намного лучше, чем Tinder, а именно: чат-бота "VKinder". Бот должен искать людей, подходящих под условия, на основании информации о пользователе из VK:

- Возраст;
- Пол;
- Город;
- Семейное положение;

У тех людей, которые подошли по требованиям пользователю, получать топ-3 популярных фотографии профиля и отправлять их пользователю в чат вместе со ссылкой на найденного человека.
Популярность определяется по количеству лайков и комментариев.

## Входные данные

### 
Id пользователя в Вконтакте, для которого мы ищем пару;

## Работа чат-бота:
###
1. При запуске кода, функция get_token заправшивает токен сообщества и токен пользователя:

```python
def get_token(group_token, user_token):
    if group_token == '':
        group_token = input('Введите токен вашей группы в ВК: ')
    if user_token == '':
        user_token = input('Введите токен пользователя: ')
    return {'group_token': group_token, 'user_token': user_token}
```
2. Переходим в сообщество и пишем в диалог с сообществом: "Привет".
3. Следуем инструкциям бота.



# Требование к сервису:

1. Код программы удовлетворяетPEP8.
2. Получать токен от пользователя с нужными правами.
3. Программа декомпозирована на функции/классы/модули/пакеты.
4. Результат программы записывать в БД.
5. Люди не должны повторяться при повторном поиске.
6. Не запрещается использовать внешние библиотеки для vk.
