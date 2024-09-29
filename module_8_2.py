def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:

        try:
            result = result + i
        except TypeError as ext:
            print(f'В numbers записан некорректный тип данных - {i}')
            incorrect_data += 1

        finally:
            data = [result, incorrect_data]

    return data

def calculate_average(numbers):
    i = 0
    try:
        i = personal_sum(numbers)
        i = i[0]/(len(numbers)-i[1])

    except TypeError:
        print('В numbers записан некорректный тип данных')
        i = None
    except ZeroDivisionError as ext:
        i = 0
    finally: return i




print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать






