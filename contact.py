import csv
import json

class Contact:
    def __init__(self, name='', phone='', email='', flag_create=0):
        if flag_create:
            self.id = max([contact['id'] for contact in self.load_contact()], default=0) + 1
            self.name = name
            self.phone = phone
            self.email = email

            self.create_contact()

    def create_contact(self):
        try:
            data_contact = self.load_contact()
            data_contact.append({'id': self.id, 'name': self.name, 'phone': self.phone, 'email': self.email})
            with open('contacts.json', 'w', encoding='utf-8') as file:
                json.dump(data_contact, file, ensure_ascii=False, indent=4)
            print('Контакт создан')
        except:
            print('Произошла ошибка при сохранение')

    def find_contact(self, word: str):
        data_contact = self.load_contact()
        flag = 0
        for contact in data_contact:
            if (word.lower() == contact['name'].lower()) or (word == contact['phone']):
                print(f'{contact["name"]}\n{contact["phone"]}\n{contact["email"]}')
                flag = 1
                break
        if flag == 0:
            print('Такого контакта нет')

    def edit_contact(self, id: int, name: str, phone: str, email: str):
        try:
            flag = 0
            data_contact = self.load_contact()
            for contact in data_contact:
                if contact['id'] == id:
                    contact['name'] = name
                    contact['phone'] = phone
                    contact['email'] = email
                    flag = 1
                    break
            if flag == 0:
                print('Такого контакта нет')
            else:
                print('Контакт изменен')
            with open('contacts.json', 'w', encoding='utf-8') as file:
                json.dump(data_contact, file, ensure_ascii=False, indent=4)
        except:
            print('Произошла ошибка при редактировании')

    def delete_contact(self, id: int):
        try:
            data_contact = self.load_contact()
            new_data_contact = [contact for contact in data_contact if contact['id'] != id]
            with open('contacts.json', 'w', encoding='utf-8') as file:
                json.dump(new_data_contact, file, ensure_ascii=False, indent=4)
            print('Контакт удален')
        except:
            print('Произошла ошибка при удаление')

    def import_contact_to_csv(self, filename: str):
        try:
            data_contact = self.load_contact()
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                     data_contact.append({
                            'id': max([contact['id'] for contact in data_contact], default=0) + 1,
                            'name': row['name'],
                            'phone': row['phone'],
                            'email': row['email']
                        })
            with open('contacts.json', 'w', encoding='utf-8') as file:
                json.dump(data_contact, file, ensure_ascii=False, indent=4)
            print('Контакты импортированы')
        except:
            print('Произошла ошибка при импорте')

    def export_to_csv(self):
        try:
            data_contact = self.load_contact()
            with open('contacts_export.csv', 'w', encoding='utf-8') as file:
                fieldnames = ['id', 'name', 'phone', 'email']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for contact in data_contact:
                    writer.writerow({'id': contact['id'], 'name': contact['name'], 'phone': contact['phone'], 'email': contact['email']})
                print('Заметки сохранены в contacts_export.csv')
        except:
            print('Произошла ошибка при экспорте')

    def load_contact(self):
        try:
            with open('contacts.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except:
            return []