import json
from datetime import datetime

temp_list = []
notes_data = {}
file_bd = "notes.json"


def save():
    with open(file_bd, "w", encoding="utf-8") as data:
        data.write(json.dumps(notes_data, ensure_ascii=False))


def load():
    with open(file_bd, "r", encoding="utf-8") as data:
        notes_data = json.load(data)
    return notes_data


def print_menu(array):
    for i in range(len(array)):
        print(''.join(map(str, array[i])))


def print_notes(array):
    print(f"Заголовок: {array[0]}")
    print(f"Заметка: {array[1]}")
    print("--------------------")


def print_note(array):
    print(f"Заголовок: {array[0]}")
    print(f"Заметка: {array[1]}")
    print(f"Дата создания: {array[2]}")
    print(f"Время создания: {array[3]}")
    print("------------")


def add_note(temp_list, notes_data):
    head_note = input('Введите заголовок : ')
    body = input('Введите тело заметки: ')
    temp_list.append(head_note)
    temp_list.append(body)
    now = datetime.now()
    create_date = "{}.{}.{}".format(now.day, now.month,
                                    now.year)
    create_time = "{}:{}:{}".format(now.hour, now.minute,
                                    now.second)
    temp_list.append(create_date)
    temp_list.append(create_time)
    notes_data[id] = temp_list


com_list = ["1 - Создать заметку",
            "2 - Сохранить заметку",
            "3 - Список заметок",
            "4 - Прочитать заявку по номеру",
            "5 - Редактировать заметку",
            "6 - Удалить заметку",
            "7 - Загрузить заметки",
            "8 - Завершение программы"]

print('Программа "Заметки"')
run = True
while run:
    print_menu(com_list)
    command = input("Введите номер команды: ")
    if command == "1":
        id = input('Введите номер заметки: ')
        if id in notes_data:
            print("Taкой номер заявки уже существует!")
        else:
            add_note(temp_list, notes_data)
            temp_list = []
            print('Заметка успешно добавлена!')
    elif command == "2":
        save()
        print('Заметка успешно сохранена!')
    elif command == "3":
        if len(notes_data) == 0:
            print("Список заметок пуст!")
        else:
            print("Текущий список заметок:")
            for key in notes_data:
                print("Заметка № {0}:".format(key))
                print_notes(notes_data.get(key))
    elif command == "4":
        id = input('Введите номер заметки: ')
        if id in notes_data:
            print_note(notes_data.get(id))
        else:
            print("Заметка с таким номером нет!")
    elif command == "5":
        print("Выберете номер заметки для редактирования: ")
        id = input('Введите номер заметки: ')
        if id in notes_data:
            add_note(temp_list, notes_data)
            temp_list = []
            print('Заметка успешно отредактирована!')
            save()
        else:
            print("Заметка с таким номером нет!")
    elif command == "6":
        print("Вы действительно хотите удалить заметку?")
        answer = input("Ведите 'да/y' или 'нет/n': ").lower()
        if answer == "да" or answer == "y":
            id_del = input('Введите номер заметки: ')
            if id_del in notes_data:
                del notes_data[id_del]
                print(f"Заметка с номером {id_del} удалена!")
                save()
            else:
                print("Заметка с таким номером нет!")
        elif answer == "нет" or answer == "n":
            print("Возврат в меню")
    elif command == "7":
        notes_data = load()
        print('Заметки из базы данных успешно загружены!')
    elif command == "8":
        save()
        print("Программа завершила свою роботу.")
        run = False
    else:
        print("Такой команды нет. Введите от 1 до 8!")
