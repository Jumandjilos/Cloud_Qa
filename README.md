# Cloud_Qa
Cloud.ru Test task for Qa

Структура тестового задания

```text
Cloud_Qa/
├── task1/
│   └── algorithm.py
├── task2/
│   ├── pages/
│   │   ├── base_page.py
│   │   └── example_page.py
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py
│       └── test_main.py
├── README.md
└── requirements.txt
```

1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале
```bash
git clone https://github.com/Jumandjilos/Cloud_Qa.git
```
Или скачайте [zip](https://github.com/Jumandjilos/Cloud_Qa/archive/refs/heads/main.zip) архив и распакуйте его

2. Убедитесь, что на Вашем компьютере установлен Python. В командной строке/терминале выполните команду
```bash
python -v
```
Если он не установлен, то установите с официального сайта Python, выбрав подходящую версию для Вашей операционной системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". Иначе, у Вас не будет корректно отображаться версия Python

3. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду
```bash
cd /Cloud_Qa
```
4. Установите необходимые зависимости из файла requirements.txt, выполнив команду
```bash
pip install -r requirements
```
если она не выполняется, то попробуйте
```bash
pip3 install -r requirements
```
5. Запустите скрипт Algorithm и введите свои цифры для проверки работы скрипта
```bash
python task_1\algorithm.py
```

6. Наконец, запустите тест сайта, выполнив команду
```bash
pytest -v
```
