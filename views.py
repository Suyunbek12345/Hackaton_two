import json

FILE_PATH = 'data.json'

class InfoMixin:
    def get_data(self):
        with open(FILE_PATH) as file:
            return json.load(file)

    def get_id(self):
        with open('id.txt','r') as file:
            id = int(file.read())
            id += 1
        with open('id.txt', 'w') as f:
            f.write(str(id))
        return id

class CreateMixin(InfoMixin):
    def create_product(self):
        data = super().get_data()
        try:
            new_product = {
                'id': super().get_id(),
                'marka': input('Enter cars mark: '), 
                'model': input('Enter model: '), 
                'year': int(input('Enter year: ')), 
                'decimal': round(float(input('Введите объем двигателя: ')),1), 
                'color': input('Enter cars color: '),
                'kuzov': input('Выберите тип кузова: (sedan, universal, kupe, hetchback, miniven, vnedorojnik, pickup): '),
                'probeg': int(input('Enter probeg cars: ')),
                'price': round(float(input('Enter cars price: ')),2)
            }
        except ValueError:
            print('Введите корректные данные!')
            self.create_product()
        else:
            data.append(new_product)
            with open(FILE_PATH,'w') as file:
                json.dump(data, file)
            return 'CREATED!'
class ListingMixin(InfoMixin):
    def listing_products(self):
        print('LISTING!!!')
        data = super().get_data()
        print(data)
        return 'End'

class RetrieveMixin(InfoMixin):
    def retrieve_data(self):
        data = super().get_data()
        try:
            id = int(input('Enter ID product: '))
        except ValueError:
            print('Введите корректные данные!')
            return self.retrieve_data()
        else:
            one_car = list(filter(lambda x: x['id'] == id, data))
            if not one_car: return 'No such product!'
            else: return one_car[0]

class UpdateMixin(InfoMixin):
    def update_data(self):
        data = super().get_data()
        flag = False
        try:
            id = int(input('Enter ID product: '))

        except ValueError:
            print('Введите корректное id!')
            return self.update_data()
        else: 
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product: return 'No such product!'
            product = data.index(one_product[0])
            choice = int(input('Что хотите изменить? (1 - marka, 2 - model, 3 - year, 4 - decimal, 5 - color, 6 - kuzov, 7 - probeg, 8 - price):'))
            if choice == 1: 
                data[product]['marka'] = input('Введите новую марку машины: ')
                flag = True
            elif choice == 2:
                data[product]['model'] = input('Введите новую модель машины: ')
                flag = True
            elif choice == 3:
                try:
                    data[product]['year'] = int(input('Введите новый год выпуска машины: '))
                except ValueError: 
                    return 'Введите корректные данные!'
                else:
                    flag = True
            elif choice == 4:
                try:
                    data[product]['decimal'] = input('Введите новый объем двигателя: ')
                except ValueError: 
                    return 'Введите корректные данные!'
                else:
                    flag = True
            elif choice == 5:
                data[product]['color'] = input('Введите новый цвет машины: ')
                flag = True
            elif choice == 6:
                data[product]['kuzov'] = input('Введите новый тип кузова машины (sedan, universal, kupe, hetchback, miniven, vnedorojnik, pickup): ')
                flag = True
            elif choice == 7:
                try:
                    data[product]['probeg'] = int(input('Введите новый пробег машины: '))
                except ValueError: 
                    return 'Введите корректные данные!'
                else:
                    flag = True
            elif choice == 8:
                try:
                    data[product]['price'] = round(float(input('Введите новую цену машины: ')),2)
                except ValueError: 
                    return 'Введите корректные данные!'
                else:
                    flag = True
            else:
                print('Такого поля нет!')
            with open(FILE_PATH,'w') as file:
                json.dump(data, file)
        if flag: return 'UPDATED'
        else: return 'NO such product!'
class DeleteMixin(InfoMixin):
    def delete_product(self):
        data = super().get_data()
        try:
            id = int(input('Enter ID product: '))
        except ValueError:
            print('Введите корректное id!')
            return self.delete_product()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
        if not one_product: 
            return 'No such product!'
        product = data.index(one_product[0])
        data.pop(product)
        
        
        with open(FILE_PATH,'w') as file:
            json.dump(data, file)
        return 'DELETED!'

class ZakazMixin(InfoMixin):
    def order_car(self):
        data = super().get_data()
        # list_of_orders = []
        try:
            id = int(input('Enter ID product: '))
        except ValueError:
            print('Введите корректное id!')
            self.order()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))[0]
        if not one_product: 
            return 'No such product!'
        product = one_product
        print(f'Ваш заказ: {one_product["marka"]} {one_product["model"]}')

        with open(FILE_PATH,'w') as file:
            json.dump(data, file)
        return 'Ожидайте заказ!'










