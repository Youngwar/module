calls = 0


def count_calls():
     global calls
     calls += 1
     return calls

def string_info():
    string_ = input('Введите строку: ')
    print({len(string_), string_.upper(), string_.lower()})
    count_calls()

def is_contains ():
    str_ = input('Введите искомую строку: ')
    list_ = input('Введите список через пробел: ').split()
    k = False
    for i in range (0, len(list_)):

        if str_.lower() in list_[i].lower():
            k = True
    count_calls()
    print(k)
string_info()
is_contains()
string_info()
is_contains()

print(calls)
