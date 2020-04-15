# Задача: Умный сервис прогноза погоды
**Уровень сложности: Задача со звездочкой**

**Проектирование сервиса:**

1) Для написания данного сервиса потребуются знания языка программирования Python и библиотек: pyowm 2.10.0(для получения информации о погоде), pyTelegramBotAPI 3.6.7(непосредственно для создания бота в Telegram). Чтобы запустить данного бота на удаленном сервере были использованы сервисы Github и Heroku.

2) В качетсве интерфейса взаимодейсвия был выброн чат-бот в Telegram.

3) Формат ответа: Данные о погоде, температуре, влажности, и скорости ветра, полученные с API подставляются в текстовый шаблон и отправляются в виде сообщений в зависимости от запроса пользователя.

Демонстрация работы сервиса доступна по ссылке: ...

**Процесс работы сервиса:**
1) **Сервис - чат-бот, который по заданному запросу пользователя, высылает ему ответ**

Данные приходят от пользователя через интерфейс мессенджера

 → формируется и отправляется запрос в базу данных

 → полученный ответ из базы используется для формирования ответа пользователю

 → ответ отправляется
