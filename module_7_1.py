

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')




class Shop():
    __file_name = 'products.txt'

    def get_products(self):

        i = open(self.__file_name, 'r')
        k = i.read()
        i.close()
        return k

    def add(self, *products):

        p = products
        list = self.get_products()
        print(list)
        j = open(self.__file_name, 'w')
        for i in p:
            if i.name not in list:
                x = i.__str__()
                l = j.write(f'{x}, \n')
            else:
                print(f'Продукт {i.name} уже есть в магазине')
        j.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.get_products()
s1.add(p1, p2, p3)
print(s1.get_products())



