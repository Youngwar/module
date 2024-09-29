class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_numbers(self.__numbers)
        self.__is_valid_vin(self.__vin)

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                True
            elif len(numbers) < 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if  1000000 <= vin_number < 9999999:
                True
            elif 1000000 > vin_number > 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            else:
                raise IncorrectVinNumber('Некорректный тип vin номер')
class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

