# simple_solutions_test

Этот проект Django интегрирует функционал оплаты через Stripe для упрощения онлайн-покупок. Он включает в себя простую модель товара, представление для отображения деталей товара и процесс оформления заказа с использованием Stripe API.

# Установка
## Клонируйте репозиторий:

```
git clone https://github.com/ваше-имя-пользователя/ваш-репозиторий.git
cd ваш-репозиторий
```




## Установите зависимости:

```pip install -r requirements.txt
```

## Примените миграции базы данных:
```
python manage.py makemigrations --settings=config.settings.local

python manage.py migrate --settings=config.settings.local
```

## Загрузите фикстуры:

```
python manage.py loaddata fixtures/Item_01.json --settings=config.settings.local
```

## Запустите сервер разработки:
```
python manage.py runserver --settings=config.settings.local
```

Перейдите по адресу http://127.0.0.1:8000/ в вашем веб-браузере.

Исследуйте доступные конечные точки:

* /buy/<int:pk>/: Начинает процесс оформления заказа для указанного товара.
* /item/<int:pk>/: Отображает детали выбранного товара.
* /success/: Указывает на успешную покупку.

# Настройка Stripe
Для включения оплаты через Stripe, вам необходимо настроить ваш ключ API Stripe и домен. Обновите следующие настройки в views.py:

```
stripe.api_key = 'ваш_секретный_ключ_stripe'
domain = 'ваш_домен'
``` 

Автор: Роман Егоров