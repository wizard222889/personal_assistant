import csv
from notes import Note
from tasks import Task

def main():
    while True:
        print(
            'Добро пожаловать в Персональный помощник!\nВыберите действие:\n1. Управление заметками\n2. Управление задачами\n3. Управление контактами\n4. Управление финансовыми записями\n5. Калькулятор\n6. Выход')
        ans = input()
        if ans == '1':
            note_menu()
        elif ans == '2':
            task_menu()
        elif ans == '3':
            pass
        elif ans == '4':
            pass
        elif ans == '5':
            pass
        elif ans == '6':
            print('Пока!')
            break
        else:
            print('Повторите ввод, я вас не понял')

def note_menu():
    while True:
        print(
            'Выберите действие:\n1. Создание новой заметки\n2. Просмотр списка заметок\n3. Просмотр подробностей заметки\n4. Редактирование заметки\n5. Удаление заметки\n6. Импорт заметок\n7. Экспорт заметок\n8. Назад')
        ans = input()
        if ans == '1':
            title = input('Введите название заметки: ')
            if title == '':
                print('Обязательное поле')
            else:
                content = input('Введите подробности заметки: ')
                note = Note(title=title, content=content, flag_create=1)
        elif ans == '2':
            note = Note()
            print(note.load_notes())
        elif ans == '3':
            try:
                id_note = int(input('Введите id заметки: '))
                note = Note()
                note.view_deatil(id_note)
            except:
                print('Неправильный ввод')
        elif ans == '4':
            try:
                id_note = int(input('Введите id заметки: '))
                title = input('Введите новый заголовок: ')
                if title == '':
                    print('Обязательное поле')
                else:
                    content = input('Введите новое описание: ')
                    note = Note()
                    note.edit_note(id_note, title=title, content=content)
            except:
                print('Неправильный ввод')
        elif ans == '5':
            try:
                id_note = int(input('Введите id заметки: '))
                note = Note()
                note.delete_note(id_note)
            except:
                print('Неправильный ввод')
        elif ans == '6':
            file_name = input('Введите название файла: ')
            note = Note()
            note.import_notes_to_csv(file_name)
        elif ans == '7':
            note = Note()
            note.export_to_csv()
        elif ans == '8':
            break
        else:
            print('Повторите ввод, я вас не понял')

def task_menu():
    while True:
        print(
            'Выберите действие:\n1. Создание новой задачи\n2. Просмотр списка задач\n3. Отметка задачи как выполненной\n4. Редактирование задачи\n5. Удаление задачи\n6. Импорт задачи\n7. Экспорт задач\n8. Назад')
        ans = input()
        if ans == '1':
            title = input('Введите название задачи: ')
            if title == '':
                print('Обязательное поле')
            else:
                description = input('Введите подробности задачи: ')
                priority = input('Введите приоритет(высокий, средний, низкий): ')
                due_date = input('Введите срок: ')
                task = Task(title=title, description=description, priority=priority, due_date=due_date, flag_create=1)
        elif ans == '2':
            task = Task()
            print(task.load_tasks())
        elif ans == '3':
            try:
                id_task = int(input('Введите id задачи: '))
                task = Task()
                task.task_done(id_task)
            except:
                print('Неправильный ввод')
        elif ans == '4':
            try:
                id_task = int(input('Введите id задачи: '))
                title = input('Введите новый заголовок: ')
                if title == '':
                    print('Обязательное поле')
                else:
                    description = input('Введите подробности задачи: ')
                    priority = input('Введите приоритет(высокий, средний, низкий): ')
                    due_date = input('Введите срок: ')
                    task = Task()
                    task.edit_task(id_task, title=title, description=description, priority=priority, due_date=due_date)
            except:
                print('Неправильный ввод')
        elif ans == '5':
            try:
                id_task = int(input('Введите id задачи: '))
                task = Task()
                task.delete_task(id_task)
            except:
                print('Неправильный ввод')
        elif ans == '6':
            file_name = input('Введите название файла: ')
            task = Task()
            task.import_tasks_to_csv(file_name)
        elif ans == '7':
            task = Task()
            task.export_to_csv()
        elif ans == '8':
            break
        else:
            print('Повторите ввод, я вас не понял')




if __name__ == '__main__':
    main()
