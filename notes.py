import csv
import json
from datetime import datetime

class Note:
    def __init__(self, title='', content='', flag_create=0):
        if flag_create:
            self.id = max([note['id'] for note in self.load_notes()], default=0) + 1
            self.title = title
            self.content = content
            self.timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            self.create_note()

    def create_note(self):
        try:
            data_note = self.load_notes()
            data_note.append({'id': self.id, 'title': self.title, 'content': self.content, 'timestamp': self.timestamp})
            with open('note.json', 'w') as file:
                json.dump(data_note, file, ensure_ascii=False, indent=4)
            print('Заметка создана')
        except:
            print('Произошла ошибка при сохранение')

    def view_deatil(self, id: int):
        data_note = self.load_notes()
        flag = 0
        for note in data_note:
            if note['id'] == id:
                print(f'{note["title"]}\n{note["content"]}')
                flag = 1
                break
        if flag == 0:
            print('Такой заметки нет')

    def edit_note(self, id: int, title: str, content: str):
        try:
            flag = 0
            data_note = self.load_notes()
            for note in data_note:
                if note['id'] == id:
                    note['title'] = title
                    note['content'] = content
                    flag = 1
                    break
            if flag == 0:
                print('Заметки такой нет')
            else:
                print('Заметка изменена')
            with open('note.json', 'w') as file:
                json.dump(data_note, file, ensure_ascii=False, indent=4)
        except:
            print('Произошла ошибка при редактировании')

    def delete_note(self, id: int):
        try:
            data_note = self.load_notes()
            new_data_note = [note for note in data_note if note['id'] != id]
            with open('note.json', 'w') as file:
                json.dump(new_data_note, file, ensure_ascii=False, indent=4)
            print('Заметка удалена')
        except:
            print('Произошла ошибка при удаление')
    def import_notes_to_csv(self, filename: str):
        try:
            data_note = self.load_notes()
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                     data_note.append({
                            'id': max([note['id'] for note in self.load_notes()], default=0) + 1,
                            'title': row['title'],
                            'content': row['content'],
                            'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                        })
            with open('note.json', 'w') as file:
                json.dump(data_note, file, ensure_ascii=False, indent=4)
            print('Заметки импортированы')
        except:
            print('Произошла ошибка при импорте')

    def export_to_csv(self):
        try:
            data_note = self.load_notes()
            with open('notes_export.csv', 'w', encoding='utf-8') as file:
                fieldnames = ['id', 'title', 'content', 'timestamp']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for note in data_note:
                    writer.writerow({'id': note['id'], 'title': note['title'], 'content': note['content'], 'timestamp': note['timestamp']})
                print('Заметки сохранены в notes_export.csv')
        except:
            print('Произошла ошибка при экспорте')

    def load_notes(self):
        try:
            with open('note.json', 'r') as file:
                return json.load(file)
        except:
            print('Пустой список')
            return []

