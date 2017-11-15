# Сайт агенства недвижимости

Данное веб-приложение - это доска объявлений для риэлторского агенства.

Пример выгрузки данных: [файл ads.json](https://devman.org/fshare/1503424990/3/)

Для того, чтобы выгрузить данные из json-файла, находящегося в той же директории, в БД, необходимо ввести в консоль команду:
```bash
python3 update_db.py json
```
В данной команде json - это обязательный аргумент, на месте которого указывается имя json-файла.
Для просмотра справки по данной команде - введите в консоль: 
```bash
python3 image_resize.py json
```

Если файл базы данных не был создан ранее, то он появится в текущей папке.

Для запуска веб-приложения на localhost - введите в консоль:
```bash
python3 server.py
```

После этого доска объявлений будет доступна по [данной ссылке](http://localhost:5000/)

# Цели проекта

Код написан в учебных целях. Обучающие курсы для веб-разработчиков - [DEVMAN.org](https://devman.org)
