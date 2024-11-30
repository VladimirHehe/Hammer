# User Authentication API

Этот проект представляет собой API для аутентификации пользователей с использованием Django и Django REST Framework. API поддерживает функциональность входа, верификации номера телефона и активации инвайт-кодов. Кроме того, он использует шаблоны для отображения страниц.

## Установка

### Требования

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL

### Установка зависимостей
1. Склонируйте репозиторий:

   ```
   git clone https://github.com/VladimirHehe/Hammer.git
   cd referral_system
   ```
2. Установите зависимости
    ```
   pip install -r requirements.txt
   ```
### Настройки базы данных
Для настройки базы данных в вашем проекте выполните следующие шаги:

1. Убедитесь, что у вас установлен сервер базы данных PostgreSQL.
2. Создайте базу данных для вашего проекта.

3. Создайте файл .env в корневой директории проекта и добавьте туда следующие переменные:
   
```
NAME_DB=your_database_name
USER_DB=your_database_user
PASS_DB=your_database_password
HOST_DB=localhost
PORT_DB=5432
   ```

4. Обновите файл settings.py, чтобы использовать переменные окружения:
   
```
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME_DB'),
        'USER': os.environ.get('USER_DB'),
        'PASSWORD': os.environ.get('PASS_DB'),
        'HOST': os.environ.get('HOST_DB'),
        'PORT': os.environ.get('PORT_DB'),
    }
}
```

### Миграции

Выполните миграции базы данных:
```
   python manage.py migrate
   ```
 Запустите сервер:
   ```
   python manage.py runserver
   ```

Теперь вы можете подключиться к API по адресу http://127.0.0.1:8000/
## Эндпоинты API

### Вход
URL: /users/login/

Method: POST

Тело запроса: 

```
{
  "phone_number": "Ваш номер телефона"
}
```

#### Ответ:

status: 200 OK
```
{
  "message": "Verification code sent."
}
```

### Верификация

URL: /users/verify/

Method: POST

Тело запроса: 
```
{
  "code": "Код верификации"
}
```

#### Ответ:

status: 200 OK 
```
{
  "user_id": "ID пользователя"
}
```

status: 400 Bad Request

```
{
  "error": "Invalid verification code!"
}
```

### Профиль пользователя

URL: /users/profile/<int:pk>/ 

Method: GET

#### Ответ: 

status: 200 OK 

```
{
  "id": "ID пользователя",
  "phone_number": "Номер телефона",
  "activated_invite_code": "Код инвайта",
  "invite_code": "Код инвайта"
}
```

### Активация инвайта

URL: /users/activate-invite/<int:pk>/

Method: POST

Тело запроса: 

```
{
  "invite_code": "Код инвайта"
}
```

#### Ответ:

status: 200 OK 

```
{
  "success": "Invite code activated successfully!"
}
```

status: 400 Bad Request

```
{
  "error": "Invite code already activated!"
}
```

## Шаблоны 

Проект также включает в себя шаблоны для отображения страниц входа и верификации. Вы можете получить доступ к ним по следующим URL:

- Вход: /users/login/
- Верификация: /users/verify/
- Профиль: /users/profile/<user_id>/