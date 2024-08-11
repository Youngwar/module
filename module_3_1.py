calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    print({len(string), string.upper(), string.lower()})
    count_calls()


def is_contains(string):
    list_to_search = ((input('Введите список через пробел: ').lower()).split())

    if string.lower() in list_to_search and string != '':
        print(True)
    else:
        print(False)

    count_calls()


print('Введите строку: ')
string_info(input())
print('Введите искомую строку: ')
is_contains(input())

print(calls)
