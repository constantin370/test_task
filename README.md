### Как запустить проект:
Логин и пароль от админ панели Джанго

```
login: admin
admin@gmail.com
password: admin

```

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/constantin370/test_task.git
```

```
cd test_task
```

Aктивировать виртуальное окружение:

Windows
```
source venv/Scripts/activate
```
Linux/macOS
```
source venv/bin/activate
```

Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустить проект:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```