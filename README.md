<img alt="Logotype" height="256" src="./docs/food.svg" width="256" align="right"/>

# UI for [Restaurant business system](https://github.com/Kumbbar/Restaurant)
Система для автоматизации основных бизнес процессов ресторанов
<!--Блок информации о репозитории в бейджах-->
![Static Badge](https://img.shields.io/badge/Author-Kumbbar-green)
<a href="https://github.com/Kumbbar/Restaurant">![Static Badge](https://img.shields.io/badge/SERVER-link-red)</a>

## Установка
1. Запуск сервера
<pre>
Инструкция по запуску <a href="https://github.com/Kumbbar/Restaurant/blob/master/README.md">здесь</a>
</pre>

2. Клонирование репозитория 

```git clone https://github.com/Kumbbar/RestaurantUI```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

Linux
```source venv/bin/activate```

Windows
```.\venv\Scripts\activate```

5. Установка зависимостей

```pip install -r requirements.txt```

6. Создание переменных окружения

```cp .env.sample .env```

7. Запуск

```python main.py```

## Вход

Логин - Boss

Пароль - 123

## Доступ к разделам

Доступ к разделам зависит от определнных прав пользователя
- admin_permission
- food_permission
- client_service_permission
- cooking_permission

Данные права дают доступ к одноименным разделам. 
Права выдаются администратором через редактирование 
пользователя. Можно комбинировать права в группы и
присваивать пользователю группу с необходимыми правами. 
Также пользователя можно сделать 
супер пользователем со всеми правами сразу.

## Поддержка
Если у вас возникли сложности или вопросы по использованию системы, создайте 
[обсуждение](https://github.com/Kumbbar/RestaurantUI/issues/new) в данном репозитории или напишите в [телеграмм](https://t.me/sudo098).

## Зависимости
Эта программа зависит от интепретатора Python версии 3.12 или выше, PIP 23.2.1 или выше.