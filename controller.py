from jsonchik import (read_file, write_file)
from view import (show_menu, no_note_show, show_list_note, 
                no_note_error, show_note_info, no_index_search, info)
from model import (filtr_note_by_date, find_note, add_note,
                del_note, update)

def run_work():
    while True:
        choice = show_menu()
        if choice == 1:             # Посмотреть Все
            notes = read_file()
            if not notes:
                no_note_show()
            else:
                show_list_note(notes)
        elif choice == 2:           # Просмотреть по дате
            notes = read_file()
            result = filtr_note_by_date(notes)
            if not result:
                no_note_error()
            else:
                show_list_note(result)            
        elif choice == 3:           # Найти заметку
            notes = read_file()
            result = find_note(notes)
            if not result:
                no_note_error()
            else:
                show_note_info(result)
        elif choice == 4:           # Добавить заметку
            notes = read_file()
            add_note(notes)
            info()
            write_file(notes)
        elif choice == 5:           # Удалить заметку
            notes = read_file()
            result = find_note(notes)
            if not result:
                no_note_error()
            else:
                del_note(notes, result)
                info()
                write_file(notes)
        elif choice == 6:           # Изменить заметку
            notes = read_file()
            result = update(notes)
            if not result:
                no_note_error()
            else:
                info()
                write_file(notes)
        elif choice == 7:           # Завершить
            break
        else:
            no_index_search()