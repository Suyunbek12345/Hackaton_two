
from views import *
# import json

class Car(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ZakazMixin):
    def start(self):
        choice = input('Привет Красавчик!\nХотите начать работу? Да/Нет: ')
        while choice.lower() == 'да':
            print('Enter operatioon! - (1 - CREATE, 2 - LISTING, 3 - RETRIEVE, 4 - UPDATE, 5 - DELETE, 6 - ORDER, 7 - EXIT)')
            a = int(input('Enter operation: (1,2,3,4,5,6,7): '))
            if a == 1: print(super().create_product())
            elif a == 2: print(super().listing_products())
            elif a == 3: print(super().retrieve_data())
            elif a == 4: print(super().update_data())
            elif a == 5: print(super().delete_product())
            elif a == 6: print(super().order_car())
            elif a == 7: 
                print('Молодец!')
                break
            else: print('Такого действия нет!')

a = Car()
a.start()
