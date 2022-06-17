import json
from settings import settings
import requests

class Cars:


    def get_id_list(self):
        read_item = requests.get(url=settings.get_url(), headers=settings.TOKEN).json()
        got_id = [i['fields']['record_id'] for i in read_item['records']]
        return got_id

    # def check_id(self, id_):
    #     self.id_ = id_
    #     while self.id_ not in self.get_id_list():
    #         res = input(f'Wrong ID. Choose ID from the list:\n{self.get_id_list()}\n')
    #         if res in self.get_id_list():
    #             return self.id_ # работает, но при вызове retreive, update и delete не выводится айтем (проблема с <self.check_id(id_)>). Пока вставил проверку id в каждую функцию

    def create(self):
        print('Creating a car...')
        car_data = {'fields': {
                            'brand': input('Enter car brand: '),
                            'model': input('Enter its model: '),
                            'year': int(input('Enter year of issue: ')),
                            'volume': float(input('Enter car volume: ')),
                            'color': input('Enter color: '),
                            'type': input(f'Select body type from the list: {settings.BODY_TYPE}\n'),
                            'mileage': int(input('Enter mileage: ')),
                            'price': float(input('Enter price: '))
                            }, 'typecast': True }
        car_data = json.dumps(car_data)
        create_item = requests.post(settings.get_url(), headers=settings.TOKEN, data = car_data)
        return f'Added new item:\n{create_item.text}'

    def listing(self):
        print('listing records...')
        read_all = requests.get(url=settings.get_url(), headers=settings.TOKEN)
        return read_all.text

    def retreive(self):
        id_ = input(f'Choose ID from the list:\n{self.get_id_list()}\n')
        while id_ not in self.get_id_list():
            id_ = input(f'Wrong ID. Choose ID from the list:\n{self.get_id_list()}\n')
        else: 
            read_item = requests.get(settings.get_url() + id_, headers=settings.TOKEN)
            return f'Retreived item by ID:\n{read_item.text}'

    def update(self):
        id_ = input(f'Choose ID from the list:\n{self.get_id_list()}\n')
        while id_ not in self.get_id_list():
            id_ = input(f'Wrong ID. Choose ID from the list:\n{self.get_id_list()}\n')
        else: 
            read_item = requests.get(settings.get_url()+id_, headers=settings.TOKEN).json()

            car_data = {'fields': {
                                'brand': input('Enter car brand: ') or read_item['brand'],
                                'model': input('Enter its model: ') or read_item['model'],
                                'year': int(input('Enter year of issue: ')) or read_item['year'],
                                'volume': float(input('Enter car volume: ')) or read_item['volume'],
                                'color': input('Enter color: ') or read_item['color'],
                                'type': input(f'Select body type from the list: {settings.BODY_TYPE}\n') or read_item['type'],
                                'mileage': int(input('Enter mileage: ')) or read_item['mileage'],
                                'price': float(input('Enter price: ')) or read_item['price']
                                }, 'typecast': True }
            car_data = json.dumps(car_data)

            update_item = requests.patch(settings.get_url()+id_, headers=settings.TOKEN, data=car_data) #put id again
            return f'Updated item:\n{update_item.text}'

    def delete(self):
        id_ = input(f'Choose ID from the list:\n{self.get_id_list()}\n')
        while id_ not in self.get_id_list():
            id_ = input(f'Wrong ID. Choose ID from the list:\n{self.get_id_list()}\n')
        else: 
            verify = input('Are you sure? (yes/no) ').lower()
            if verify == 'yes':
                delete_item = requests.delete(settings.get_url()+id_, headers=settings.TOKEN)
                return delete_item.text
            else:
                return 'The operation is cancelled'

    def menu(self):
        commands = {
                'create': self.create, 
                'list': self.listing, 
                'retreive': self.retreive, 
                'update' : self.update, 
                'delete': self.delete
                }
        while True:
            print('''
                create - to create an item
                list - to see the full list of items
                retreive - to see an item
                update - to change/update
                delete - to delete
                ''')
            command = input('Type a command from the list above or "exit" to exit: ').lower()
            if command in commands:
                print(commands[command]())
            elif command == 'exit':
                break
            else:
                print('\nThere is no such command in the list. Choose from the list below:')


car = Cars()

car.menu()