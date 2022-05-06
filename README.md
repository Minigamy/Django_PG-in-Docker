# Django_PG-in-Docker

Данный проект заключается в демонстрации работы связки проекта на Django и базы данных Postgresql, развернутой в контейнере Docker.
Для удобства так же в контейнере запускается pgAdmin.

### Реализован(a):
 - REST API со стороны сервера, который принимает POST-запросы с данными типа {"questions_num": integer}.
 - Запрос данных с публичного API https://jservice.io/api/random?count=1
 - Запись полученных ответов в БД PostgreSQL, развернутой в docker-контейнере
 - Проверка полученных данных на уникальность (все записи в БД будут уникальными)
 - Ответ на POST-запрос в виде текста вопроса из ранее полученных данных


# Запуск

1) Скачиваем/клонируем репозиторий `https://github.com/Minigamy/Django_PG-in-Docker.git`
2) Устанавливаем зависимости из файла requirements.txt командой в терминале `pip install -r requirements.txt`
3) Запускаем контейнер с Postgresql и pgAdmin командой в терминале `docker-compose.yaml up -d` (Обязательно должен быть установлен и запущен Docker)
4) Запускаем миграцию командами: `python manage.py makemigrations` и `python manage.py migrate`
5) Запускаем сервер `python manage.py runserver`

Все, база данных и сервер полностью готовы к работе. Сервер принимает только POST-запросы, поэтому для отправки запроса можно воспользоваться программой Postman или скриптом `request.py`, расположенным в корне проекта. Далее идет описание варианта со скриптом.
***
## `request.py`

```
import requests

r = requests.post('http://127.0.0.1:8000/', data={"question_num": <ваше значение>})

print(r.text)

```
В аргументе `data={"question_num": <ваше значение>}` можно изменить значение на необходимое положительное целое число.
После выполнения данного скрипта в терминале будет выведен текст последнего вопроса из БД или, если БД пустая, то вернется объект None.
***
## `pgAdmin`

Для подключения к pgAdmin потребуется выполнить следующие действия:
1) В браузере открыть страничку `http://127.0.0.1:5050/`
2) Ввести логин и пароль: 
 *     Логин: myemail@email.com
 *     Пароль: root
![Скриншот](https://github.com/Minigamy/Django_PG-in-Docker/blob/0abcb081a973670c7acaea74a0c0b810a2e85b8f/media/pgadmin_start.png)
<p align="center">pgAdmin - Вход</p> 

3) Во вкладке General заполняем поле Name. Можно выбрать любое имя.
4) Во вкладке Connection необходимо заполнить следующие поля:
 *     Host name/address: pg_db
 *     Port: 5432
 *     Username: root
 *     Password: root
![Скриншот](https://github.com/Minigamy/Django_PG-in-Docker/blob/0abcb081a973670c7acaea74a0c0b810a2e85b8f/media/pgadmin_connect.png)
<p align="right">pgAdmin - Подключение</p> 

5) Сохраняем на кнопку `Save`
