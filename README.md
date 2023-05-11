<h1>telegram_weather_bot</h1>

<h2>Описание</h2> 
Телеграмм бот, который показывает погоду в указанном городе. 

<h2>Зачем это?</h2> 

Данный бот рассматривался как практическая работа для изучения основ:
* фреймворка telebot
* простая работа с API и токенами
* работа с зависимостями

<h2>Установка и запуск</h2> 

<p>Для работы с ботом нужно установить интерпретатор Python, IDE, клонировать репозиторий и установить зависимости.</p> 
<p>Установить интерпретатор: https://www.python.org/downloads/</p>
<p>Выбрать IDE: https://habr.com/ru/companies/skillfactory/articles/521838/</p>
<p>Адрес репозитория: https://github.com/KorytkoSergey/telegram_weather_bot</p>
<p>Создать виртуальное окружение в командной строке. Для это перейдите в дерикторию проекта при помощи строки и введите: <code>python -m venv <название окружения></code></p>
<p>Затем активируем <code>source myenv/bin/activate</code></p>
<p>Установить зависимости <code>pip install -r requirements.txt</code> и доустанавливаем <code>pip install requests</code> при необходимости</p>

В директории проекта создаем файл .env, внего вносим токены:
* токен для погоды мы берем с https://openweathermap.org/api
* токен для бота берем с https://core.telegram.org/
Запускаем или внутри IDE, или в командной строке <code>python main.py</code>
<p>**Ваш ПК будет сервером. И пока работает ваш ПК, работает и ваш бот.** </p>
  
