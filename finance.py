import json
import csv
from datetime import datetime

class FinanceRecord:
    def __init__(self, amount=0, category='', date='', description='', flag_create=0):
        if flag_create:
            self.id = max([record['id'] for record in self.load_record()], default=0) + 1
            self.amount = amount
            self.category = category
            self.date = date
            self.description = description

            self.create_record()

    def load_record(self):
        try:
            with open('finance.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except:
            return []

    def filtered_record(self, category='', date_start='', date_end=''):
        try:
            data_record = self.load_record()
            if category != '':
                for record in data_record:
                    if record['category'].lower() == category.lower():
                        print(record['amount'], record['category'], record['date'], record['description'])
            elif date_start != '' and date_end != '':
                date_start = datetime.strptime(date_start, '%d-%m-%Y')
                date_end = datetime.strptime(date_end, '%d-%m-%Y')
                for record in data_record:
                    if date_start <= datetime.strptime(record['date'], '%d-%m-%Y') <= date_end:
                        print(record['amount'], record['category'], record['date'], record['description'])
            else:
                print(data_record)
        except:
            print('Произошла ошибка при фильтрации')


    def create_record(self):
        try:
            data_record = self.load_record()
            data_record.append({'id': self.id, 'amount': self.amount, 'category': self.category, 'date': self.date, 'description': self.description})
            with open('finance.json', 'w', encoding='utf-8') as file:
                json.dump(data_record, file, ensure_ascii=False, indent=4)
            print('Запись создана')
        except:
            print('Произошла ошибка при сохранение')

    def generate_record(self, start_date='', end_date=''):
        try:
            start_date_str = datetime.strptime(start_date, '%d-%m-%Y')
            end_date_str = datetime.strptime(end_date, '%d-%m-%Y')
            data_record = self.load_record()
            data_record = [record for record in data_record if (start_date_str <= datetime.strptime(record['date'], '%d-%m-%Y')) and \
                           (datetime.strptime(record['date'], '%d-%m-%Y') <= end_date_str)]
            income = sum([record['amount'] for record in data_record if record['amount'] > 0])
            expense = sum([record['amount'] for record in data_record if record['amount'] < 0])
            balance = income + expense
            print(f'Финансовый отчёт за период с {start_date} по {end_date}')
            print(f'- Общий доход: {income} руб.')
            print(f'- Общий расход: {expense} руб.')
            print(f'- Баланс: {balance} руб.')
            with open(f'report_{start_date}_{end_date}.csv', 'w', encoding='utf-8') as file:
                fieldnames = ['id', 'amount', 'category', 'date', 'description']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for record in data_record:
                    writer.writerow({'id': record['id'], 'amount': record['amount'], 'category': record['category'], 'date': record['date'], 'description': record['description']})
            print(f'Подробная информация сохранена в файле report_{start_date}_{end_date}.csv')
        except:
            print('Произошла ошибка при генерации отчета')

    def delete_record(self, id: int):
        try:
            data_records = self.load_record()
            new_data_records = [record for record in data_records if record['id'] != id]
            with open('finance.json', 'w', encoding='utf-8') as file:
                json.dump(new_data_records, file, ensure_ascii=False, indent=4)
            print('Запись удалена')
        except:
            print('Произошла ошибка при удаление')

    def import_record_to_csv(self, filename: str):
        try:
            data_record = self.load_record()
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                     data_record.append({
                            'id': max([record['id'] for record in data_record], default=0) + 1,
                            'amount': int(row['amount']),
                            'category': row['category'],
                            'date': row['date'],
                            'description': row['description']
                        })
            with open('finance.json', 'w', encoding='utf-8') as file:
                json.dump(data_record, file, ensure_ascii=False, indent=4)
            print('Записи импортированы')
        except:
            print('Произошла ошибка при импорте')

    def export_to_csv(self):
        try:
            data_record = self.load_record()
            with open('records_export.csv', 'w', encoding='utf-8') as file:
                fieldnames = ['id', 'amount', 'category', 'date', 'description']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for record in data_record:
                    writer.writerow({'id': record['id'], 'amount': record['amount'], 'category': record['category'], 'date': record['date'], 'description': record['description']})
                print('Записи сохранены в records_export.csv')
        except:
            print('Произошла ошибка при экспорте')


