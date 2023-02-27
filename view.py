import time
import uuid
from datetime import datetime

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Просмотреть все")
    print("2. Просмотреть по дате")
    print("3. Найти заметку")
    print("4. Добавить заметку")
    print("5. Удалить заметку")
    print("6. Изменить заметку")
    print("7. Завершить")
    return int(input("Выберите необходимое действие: "))

def show_search_menu() -> int:
    print("\n" + "=" * 20)
    print("1.  Найти по ID")
    print("2.  Найти по заголовку")
    return int(input("Выберите действие: "))

def show_update_menu() -> int:
    print("\n" + "=" * 20)
    print("1.  Изменить по ID")
    print("2.  Изменить по заголовку")
    return int(input("Выберите действия: "))

def get_note() -> dict:
    result = {}
    result["id"] = get_id()
    result["title_note"] = get_title_note()
    result["text_note"] = get_text_note()
    result["data_note"] = get_data_note()
    return result  

def get_id() -> int:
    return  str(uuid.uuid4())[0:3]


def get_title_note() -> str:
    return input("Введите заголовок заметки: ")


def get_text_note() -> str:
    return input("Введите текст заметки: ")


def get_data_note() -> str:
    return str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

def get_search_id() -> str:
    return input("Введите ID для поиска заметки: ") 

def get_changes() -> int:
    print("\nВыберите что необходимо изменить:")
    print("1. Заголовок заметки")
    print("2. Текст заметки")
    return int(input("Выберите действие: "))

def check_data():
    while True:
        date = input('Введите дату в формате: dd.mm.yyyy: ')
        temp = date
        try:
            temp = time.strptime(date, '%d.%m.%Y')
            break
        except ValueError:
            print('(^__*) Неправильный ввод даты! (^__*)')
            continue
    return date

def no_note_error():
    print(" (*_*) Такой заметки нет (*_*) ")

def no_note_show():
    print(" (^_^) Заметки не найдены (^_^) ")

def no_index_search():
    print("(o-_-o) Неверный ввод, попробуйте еще раз (o-_-o)")

def info():
    print(" (¬‿¬ ) Операция выполнена успешно (¬‿¬ )")

def show_note_info(note: dict):
    for k, v in note.items():
        print(f'{k}: {v}')

def show_list_note(notes: list):
    for item in notes:
        print("\n" + "=" * 20)
        show_note_info(item)