from encodings import utf_8
import json

class Car():
    
    FILE = 'jsondb/data.json'
    id = 0

    def __init__(self, mark, model, year, volume, color, body_type, mileage, price):
        self.mark = mark 
        self.model = model 
        self.year = year 
        self.volume = volume 
        self.color = color 
        self.body_type = body_type 
        self.mileage = mileage 
        self.price = price
        self.sent_product_to_json()


    @classmethod        
    def get_id(cls):
        cls.id += 1
        return cls.id


    @classmethod
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)
    

    

    def sent_product_to_json(self):
        data = Car.get_data()
        product = {'id': Car.get_id(),
            'mark': self.mark,
            'model': self.model,
            'year': self.year,
            'volume': self.volume,
            'color': self.color,
            'body_type': self.body_type,
            'mileage': self.mileage,
            'price': self.price 
        }
            

        data.append(product)

        with open(Car.FILE, 'w') as file:
            json.dump(data, file)
        
        
        return {'status': '201', 'msg': product}
    
    @classmethod
    def sent_data_to_json(cls, data):
        
        with open (cls.FILE, 'w') as file:
            json.dump(data, file)



    @classmethod
    def retrieve_data(cls, id):
        data = cls.get_data()
        product = cls.get_one_product(data, id)
        return product

    @staticmethod
    def get_one_product(data, id):
        product = list(filter(lambda x: x['id']==id, data))
        if  not product:
            return 'Нет такой машины'
        return product[0]
    
    @classmethod
    def update_data(cls, id, **kwargs):
        data =cls.get_data()
        product = cls.get_one_product(data, id)
        if type(product) != dict:
            return product
        index = data.index(product)
        data[index].update(**kwargs)
        cls.sent_data_to_json(data)
        return {'status':'200', 'msg':'updated'}
    
    @classmethod
    def delete_data(cls, id):
        data = cls.get_data()
        product = cls.get_one_product(data, id)
        if type(product) != dict:
            return product

        index = data.index(product)
        data.pop(index)
        cls.sent_data_to_json(data)
        return {'status':'204', 'msg':'deleted'}        
    
with open (Car.FILE, 'w')as file:
    json.dump([], file)
bmw1 = Car('BMW', 'M5', 2005, 4, 'Black', 'Sedan', 457, 10000)
merc = Car('Mercedez-Benz', 'G-class G 63 AMG', 2003, 4, 'White', 'Pika[', 378, 35000)
bmw2 = Car('BMW', 'M3', 1996, 3.5, 'Black', 'Sedan', 350, 5000) 
print('Все машины:\n', Car.get_data())
print('\n', Car.retrieve_data(3))
print('\n', Car.update_data(1, year = 2003))
print('\n', Car.retrieve_data(1))
print(Car.delete_data(3))
print('Все машины:\n', Car.get_data())
    
