import csv
import json

class Task:
    def __init__(self, title='', description='', priority='', due_date='', flag_create=0):
        if flag_create:
            self.id = max([note['id'] for note in self.load_tasks()], default=0) + 1
            self.title = title
            self.description = description
            self.done = False
            self.priority = priority
            self.due_date = due_date

            self.create_task()


    def create_task(self):
        try:
            data_tasks = self.load_tasks()
            data_tasks.append({'id': self.id, 'title': self.title, 'description': self.description, 'done': self.done, 'priority': self.priority, 'due_date': self.due_date})
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(data_tasks, file, ensure_ascii=False, indent=4)
            print('Задача создана')
        except:
            print('Произошла ошибка при сохранение')

    def load_tasks(self):
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except:
            return []

    def task_done(self, id: int):
        try:
            flag = 0
            data_tasks = self.load_tasks()
            for task in data_tasks:
                if task['id'] == id:
                    task['done'] = True
                    flag = 1
                    break
            if flag == 0:
                print('Задачи такой нет')
            else:
                print('Задача выполнена')
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(data_tasks, file, ensure_ascii=False, indent=4)
        except:
            print('Произошла ошибка при редактировании')

    def edit_task(self, id, title, description, priority, due_date):
        try:
            flag = 0
            data_tasks = self.load_tasks()
            for task in data_tasks:
                if task['id'] == id:
                    task['title'] = title
                    task['description'] = description
                    task['priority'] = priority
                    task['due_date'] = due_date
                    flag = 1
                    break
            if flag == 0:
                print('Задачи такой нет')
            else:
                print('Задача изменена')
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(data_tasks, file, ensure_ascii=False, indent=4)
        except:
            print('Произошла ошибка при редактировании')

    def delete_task(self, id):
        try:
            data_tasks = self.load_tasks()
            new_data_tasks = [task for task in data_tasks if task['id'] != id]
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(new_data_tasks, file, ensure_ascii=False, indent=4)
            print('Задача удалена')
        except:
            print('Произошла ошибка при удаление')

    def import_tasks_to_csv(self, filename: str):
        try:
            data_tasks = self.load_tasks()
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                     data_tasks.append({
                            'id': max([task['id'] for task in self.load_tasks()], default=0) + 1,
                            'title': row['title'],
                            'description': row['description'],
                            'done': False,
                            'priority': row['priority'],
                            'due_date': row['due_date']
                        })
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(data_tasks, file, ensure_ascii=False, indent=4)
            print('Задачи импортированы')
        except:
            print('Произошла ошибка при импорте')

    def export_to_csv(self):
        try:
            data_tasks = self.load_tasks()
            with open('tasks_export.csv', 'w', encoding='utf-8') as file:
                fieldnames = ['id', 'title', 'description', 'done', 'priority', 'due_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for task in data_tasks:
                    writer.writerow({'id': task['id'], 'title': task['title'], 'description': task['description'], 'done': str(task['done']), 'priority': task['priority'], 'due_date' : task['due_date']})
                print('Задачи сохранены в tasks_export.csv')
        except:
            print('Произошла ошибка при экспорте')


