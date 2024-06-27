# Сервис Задач

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
___

Данный проект представляет собой `сервис` для работы с `задачами`. У сервиса есть 2 типа использования:
- Использовать как `Заказчик(Client)`
- Использовать как `Сотрудник(Employee)`

Перед тем, как начать работать с задачами, требуется `зарегестрироваться` и `авторизоваться` как `Сотрудник`, либо как `Заказчик` (решать вам)

Сервис поддерживает `авторизацию/аутентификацию` с помощью `Refresh и Access` токенов.

После регистрации и авторизации, в зависимости от роли пользователя у вас будут разные права доступа

Для `Заказчика`:
- Создание/редактирование задачи
- Просмотр все сотрудников
- Просмотр всех своих задач
- Просмотр конкретной своей задачи

Для `Сотрудника`:
- Доступ ко всем задачам
- Создать/изменить задачу
- Добавление заказчика
- Добавление сотрудника
- Просмотр всех сотрудников

___
>### Содержание
* [Системные требования](https://github.com/Artuom4ik/service-task?tab=readme-ov-file#системные-требования)
* [Запуск сервиса](https://github.com/Artuom4ik/service-task?tab=readme-ov-file#запуск-сервиса)
* [Запуск сервиса с помощью docker-compose](https://github.com/Artuom4ik/service-task?tab=readme-ov-file#запуск-сервиса-с-помощью-docker-compose)
* [Переменные окружения](https://github.com/Artuom4ik/service-task?tab=readme-ov-file#переменные-окружения)
* [Эндпоинты и их функции](https://github.com/Artuom4ik/service-task?tab=readme-ov-file#эндпоинты-и-их-функции)
* [Примеры использования](https://github.com/Artuom4ik/service-task?tab=readme-ov-file#примеры-использования)
___

>### Системные требования
- `Python` 3.10.12(или выше)
- `Windows`(10, 11) или `Linux`(Ubuntu 22.*)
___
>### Запуск сервиса

- Скачайте код командой
```
git clone https://github.com/Artuom4ik/service-task.git
```
- Перейте в рабочую директорию
```
cd service-task
```
- Создайте виртуальное окружение командой
```
python3 -m venv myvenv
```
- Активируйте виртуальное окружение командой

`Linux`

```
source myvenv/bin/activate
```

`Windows`

```
.\myvenv\Scripts\activate
```
- Перейдите в директорию `service`

- Создайте файл с расширеним `.env` и запишите туда следующие параметры(`ПЕРЕМЕННАЯ=значение`):
    - `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
    - `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`. [Ссылка](https://djecrety.ir) на сайт для генерации `секретного ключа`

- Установите зависимости командой 
```
pip install -r requirements.txt
```
- Выполните миграции базы данных командой


`Для Linux` 

```bash
python3 manage.py migrate
```

`Для Windows`

```bash
python manage.py migrate
```

- Запустите сервер командой


`Для Linux`

```bash
python3 manage.py runserver
```

`Для Windows`

```bash
python manage.py runserver
```

После этого сервис будет запущен и будет доступен по такому адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
___
>### Запуск сервиса с помощью docker-compose

#### Для Windows
* Для того чтобы запустить, `docker-compose` на своем компьютере, вам потребуется установить [Docker Desktop](https://www.docker.com/products/docker-desktop/).
___

#### Для Linux
* Предварительные требования для `linux` систем, для его выполнения вам потребуется следующее:

* Доступ к локальному компьютеру или серверу разработки `Ubuntu 20.04 (или выше)` от имени пользователя без привилегий root с привилегиями sudo. Если вы используете удаленный сервер, рекомендуется установить активный брандмауэр. Для настройки ознакомьтесь с документом [«Руководство по начальной настройке сервера Ubuntu 20.04»](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04).
* Система `Docker`, установленная на сервере или локальном компьютере в соответствии с шагами 1 и 2 документа [«Установка и использование Docker в Ubuntu 20.04»](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04).

* После выполнения ряда требованний, выполните команду для установки `docker-compose`:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Версию выбирайте сами. В ссылке указана версия 1.26.0.

Затем необходимо задать правильные разрешения, чтобы сделать команду `docker-compose` исполняемой:

```
sudo chmod +x /usr/local/bin/docker-compose
```

Чтобы проверить успешность установки, запустите следующую команду:
```
docker-compose --version
```

Вывод будет выглядеть следующим образом:

```
Output
docker-compose version 1.26.0, build 8a1c60f6
```
___

>### Запуск сервера
**Прежде чем запустить `docker-compose` выполните несколько действий**
- Если вы не находитесь в корневой папке проекта, то требуется перейти в неё командой:
```bash
cd service-task
```
- Перейдите в папку `service`:
```bash
cd service
```
- Создайте файл с расширеним `.env` и запишите туда следующие параметры(`ПЕРЕМЕННАЯ=значение`):
    - `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
    - `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`. [Ссылка](https://djecrety.ir) на сайт для генерации `секретного ключа`

#### Для Windows 
* Запустите программу `Docker Dosktop`.
* После запуска `Docker Desktop`, в консоле напишите команду:
```
docker-compose up --build
``` 
#### Для Linux:
* После успешной установки `docker-compose`, в консоли  напишите команду: 
```
docker-compose up --build
```
* Если `docker-compose` не запустился попробуйте добавить префикс `sudo`:
```bash
sudo docker-compose up --build
```
* После образ соберется в контейнер и сервер будет запущен.
___

>### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта требуется указать переменные окружения**.

- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
[Ссылка](https://djecrety.ir) на сайт для генерации `секретного ключа`
___

>### Эндпоинты и их функции

**Для пути http://127.0.0.1:8000/accounts/ имеются такие эндпоинты**

- `api/token/` - этот эндпоинт используется для получения пары токенов доступа и обновления (refresh tokens) при аутентификации пользователя. Он связан с `TokenObtainPairView.as_view()`.

- `api/token/refresh/` - этот эндпоинт используется для обновления токена доступа. Когда токен доступа истекает, его можно обновить, используя этот эндпоинт. Он связан с `TokenRefreshView.as_view()`.

- `api/register/` - этот эндпоинт используется для регистрации новых пользователей. Он связан с `RegisterView.as_view()`.

- `api/login/` - этот эндпоинт используется для входа зарегистрированных пользователей. Он связан с `LoginView.as_view()`.

- `api/logout/` - этот эндпоинт используется для выхода пользователя из системы. Он связан с `LogoutView.as_view()`.

- `api/current_user/` - этот эндпоинт используется для получения информации о текущем пользователе (авторизованном). Он связан с `CurrentUserView.as_view()`.

- `api/employees/` - этот эндпоинт используется для получения списка сотрудников. Он связан с `EmployeeListView.as_view()`.

- `api/clients/` - этот эндпоинт используется для получения списка клиентов. Он связан с `ClientListView.as_view()`.

**Эти эндпоинты представляют API для аутентификации, управления пользователями и получения списка сотрудников и клиентов.**
___

**Для пути http://127.0.0.1:8000/tasks/ имеются такие эндпоинты**

- `''` - этот эндпоинт связан с представлением TaskViewSet и позволяет выполнять два действия:
     - GET: Получение списка всех задач.
     - POST: Создание новой задачи.

- `<int:pk>/` - этот эндпоинт ожидает целочисленный идентификатор (pk) задачи в URL. Он также связан с представлением TaskViewSet и позволяет выполнять следующие действия:
     - GET: Получение информации о конкретной задаче с указанным идентификатором.
     - PUT: Обновление информации о задаче с указанным идентификатором.

**Эти эндпоинты обеспечивают функционал для получения списка задач, создания новых задач, получения информации о конкретной задаче и обновления данных задачи.**

___

>### Примеры использования

#### Регистрация пользователя
**Для регистрации нового пользователя отправьте POST запрос на** `/api/register/` **с данными пользователя.**

```sh
curl -X POST http://127.0.0.1:8000/accounts/api/register/ \
-H "Content-Type: application/json" \
-d '{
    "email": "your_email@example.com",
    "password": "your_password",
    "first_name": "First",
    "last_name": "Last",
    "middle_name": "Middle",
    "phone_number": "+1234567890",
    "role": "employee"
}'
```
#### Аутентификация пользователя (получение токенов)
**Для получения Access и Refresh токенов отправьте POST запрос на** `/api/login/` **с данными пользователя.**

```sh
curl -X POST http://127.0.0.1:8000/accounts/api/login/ \
-H "Content-Type: application/json" \
-d '{
    "email": "your_email@example.com",
    "password": "your_password"
}'
```
**Пример ответа**

```json
{
    "refresh": "refresh_token_here",
    "access": "access_token_here"
}
```

#### Обновление токена
**Для обновления Access токена отправьте POST запрос на** `/api/token/refresh/` **с Refresh токеном.**

```sh
curl -X POST http://127.0.0.1:8000/accounts/api/token/refresh/ \
-H "Content-Type: application/json" \
-d '{
    "refresh": "refresh_token_here"
}'
```
#### Логаут пользователя (аннулирование токена)
**Для аннулирования Refresh токена отправьте POST запрос на** `/api/logout/` **с токеном.**

```sh
curl -X POST http://127.0.0.1:8000/accounts/api/logout/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer access_token_here" \
-d '{
    "refresh": "refresh_token_here"
}'
```

#### Получение информации о текущем пользователе
**Для получения информации о текущем пользователе отправьте GET запрос на** `/api/current_user/`

```sh
curl -X GET http://127.0.0.1:8000/accounts/api/current_user/ \
-H "Authorization: Bearer access_token_here"
```

#### Получение списка сотрудников
**Для получения списка сотрудников отправьте GET запрос на** `/api/employees/`

```sh
curl -X GET http://127.0.0.1:8000/accounts/api/employees/ \
-H "Authorization: Bearer access_token_here"
```

#### Получение списка заказчиков
**Для получения списка заказчиков отправьте GET запрос на** `/api/clients/`.

```sh
curl -X GET http://127.0.0.1:8000/accounts/api/clients/ \
-H "Authorization: Bearer access_token_here"
```

#### Получить список задач
**Эндпоинт**: `/`
```sh
curl -X GET http://127.0.0.1:8000/tasks/ \
-H "Authorization: Bearer access_token_here"
```

#### Создать задачу
**Эндпоинт**: `/`
```sh
curl -X POST http://127.0.0.1:8000/tasks/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer access_token_here" \
-d '{
    "name": "Task Name",
    "description": "Task Description"
}'
```

#### Получить детали задачи
**Эндпоинт**: `/<int:pk>/`

```sh
curl -X GET http://127.0.0.1:8000/tasks/1/ \
-H "Authorization: Bearer access_token_here"
```

#### Обновить задачу
**Эндпоинт**: `/<int:pk>/`

```sh
curl -X PUT http://127.0.0.1:8000/tasks/1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer access_token_here" \
-d '{
    "name": "Updated Task Name",
    "description": "Updated Task Description",
    "report": "Report content if employee"
}'
```
___

**Получить список задач (GET /)**

- Этот запрос доступен как клиентам, так и сотрудникам.
Клиенты увидят только свои задачи, а сотрудники — все задачи.

**Создать задачу (POST /)**

- Этот запрос доступен только клиентам.
Клиенты могут создавать задачи, указывая имя и описание.

**Получить детали задачи (GET /int:pk/)**

- Этот запрос доступен как клиентам, так и сотрудникам.
Клиенты могут видеть только свои задачи, сотрудники могут видеть любую задачу.

**Обновить задачу (PUT /int:pk/)**

- Этот запрос доступен как клиентам, так и сотрудникам.
Клиенты могут обновлять имя и описание задачи.
Сотрудники могут добавлять отчет, что также изменяет статус задачи на "completed" и устанавливает время закрытия.
