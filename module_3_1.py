calls = 0


def count_calls():
     global calls
     calls += 1
     return calls

def string_info():
    string = input('Введите строку: ')
    print({len(string), string.upper(), string.lower()})
    count_calls()

def is_contains ():
    string = input('Введите искомую строку: ')
    list_to_search = ((input('Введите список через пробел: ').lower()).split())


    if string.lower() in list_to_search and string != '':
        print(True)
    else: print(False)

    count_calls()
string_info()
is_contains()


print(calls)
