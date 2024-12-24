import csv
from notes import Note
from tasks import Task
from contact import Contact
from finance import FinanceRecord


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
            contact_menu()
        elif ans == '4':
            finance_menu()
        elif ans == '5':
            calculate()
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


def contact_menu():
    while True:
        print(
            'Выберите действие:\n1. Создание нового контакта\n2. Поиск контакта\n3. Редактирование контакта\n4. Удаление контакта\n5. Импорт контактов\n6. Экспорт контактов\n7. Назад')
        ans = input()
        if ans == '1':
            name = input('Введите имя контакта: ')
            if name == '':
                print('Обязательное поле')
            else:
                phone = input('Введите номер контакта: ')
                email = input('Введите почту контакта: ')
                contact = Contact(name=name, phone=phone, email=email, flag_create=1)
        elif ans == '2':
            contact = Contact()
            name = input('Введите имя или номер телефона контакта: ')
            contact.find_contact(name)
        elif ans == '3':
            try:
                id_contact = int(input('Введите id контакта: '))
                name = input('Введите новое имя контакта: ')
                if name == '':
                    print('Обязательное поле')
                else:
                    phone = input('Введите новый номер телефона контакта: ')
                    email = input('Введите новую почту контакта: ')
                    contact = Contact()
                    contact.edit_contact(id_contact, name=name, phone=phone, email=email)
            except:
                print('Неправильный ввод')
        elif ans == '4':
            try:
                id_contact = int(input('Введите id контакта: '))
                contact = Contact()
                contact.delete_contact(id_contact)
            except:
                print('Неправильный ввод')
        elif ans == '5':
            file_name = input('Введите название файла: ')
            contact = Contact()
            contact.import_contact_to_csv(file_name)
        elif ans == '6':
            contact = Contact()
            contact.export_to_csv()
        elif ans == '7':
            break
        else:
            print('Повторите ввод, я вас не понял')


def finance_menu():
    while True:
        print(
            'Выберите действие:\n1. Добавить новую запись\n2. Просмотреть все записи\n3. Генерация отчёта\n4. Удалить запись\n5. Импорт финансовых записей из CSV\n6. Экспорт финансовых записей в CSV\n7. Назад')
        ans = input()
        if ans == '1':
            try:
                amount = int(input('Введите сумму операции: '))
                category = input('Введите категорию: ')
                date = input('Введите дату(ДД-ММ-ГГГГ): ')
                description = input('Введите описание: ')
                record = FinanceRecord(amount=amount, category=category, date=date, description=description,
                                       flag_create=1)
            except:
                print('Неправильный ввод')
        elif ans == '2':
            record = FinanceRecord()
            ans2 = input('Фильтрация: 1. категория 2. по дате')
            if ans2 == '1':
                category = input('Введите категорию: ')
                record.filtered_record(category=category)
            elif ans2 == '2':
                start_date = input('Введите начальную дату(ДД-ММ-ГГГГ): ')
                end_date = input('Введите конечную дату(ДД-ММ-ГГГГ): ')
                record.filtered_record(date_start=start_date, date_end=end_date)
            else:
                print('Я вас не понял')
        elif ans == '3':
            try:
                start_date = input('Введите начальную дату(ДД-ММ-ГГГГ): ')
                end_date = input('Введите конечную дату(ДД-ММ-ГГГГ): ')
                record = FinanceRecord()
                record.generate_record(start_date=start_date, end_date=end_date)
            except:
                print('Неправильный ввод')
        elif ans == '4':
            try:
                id_record = int(input('Введите id записи: '))
                record = FinanceRecord()
                record.delete_record(id_record)
            except:
                print('Неправильный ввод')
        elif ans == '5':
            file_name = input('Введите название файла: ')
            record = FinanceRecord()
            record.import_record_to_csv(file_name)
        elif ans == '6':
            record = FinanceRecord()
            record.export_to_csv()
        elif ans == '7':
            break
        else:
            print('Повторите ввод, я вас не понял')

def calculate():
    x = input("Введите выражение: ")
    try:
        ans = eval(x)
        print(f'Результат: {ans}')
    except ZeroDivisionError:
        print('На 0 делить нельзя')
    except Exception as error:
        print(f'Ошибка в выражении')

if __name__ == '__main__':
    main()
