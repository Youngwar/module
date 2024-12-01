from pprint import pprint
import inspect



class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop():
    __file_name = 'products.txt'

    def __init__(self, name, date_of_opening):
        self.name = name
        self.date_of_opening = date_of_opening

    def get_products(self):
        i = open(self.__file_name, 'r')
        k = i.read()
        i.close()
        return k

    def add(self, *products):

        p = products
        list = self.get_products()
        j = open(self.__file_name, 'a')
        for i in p:
            if i.name not in list:
                x = i.__str__()
                l = j.write(f'{x}, \n')
            # else:
            #     print(f'Продукт {i.name} уже есть в магазине')
        j.close()

s1 = Shop('Шестерочка', 2001)
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
s1.get_products()
s1.add(p1, p2, p3)



def introspection_info(obj):
    introspection_info_list = []
    i = f"Тип объекта: {type(obj)}"
    introspection_info_list.append(i)
    attributes = f'Атрибуты класса: {obj.__dict__}'
    introspection_info_list.append(attributes)
    i = inspect.getmembers(obj, inspect.ismethod)
    k = []
    for j in i:
        k.append(j[0])
    introspection_info_list.append(f'Список методов: {k}')
    introspection_info_list.append(f'Модуль объекта: {inspect.getmodule(obj)}')


    return introspection_info_list



number_info = introspection_info(s1)
print(number_info)
