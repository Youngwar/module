calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    print({len(string), string.upper(), string.lower()})
    count_calls()


def is_contains(string, list_to_search = []):
    if string.lower() in list_to_search and string != '':
        print(True)
    else:
        print(False)

    count_calls()


print('Введите строку: ')
string_info(input())

is_contains(input('Введите искомую строку: ',), (input('Введите список строк через пробел: ').lower()).split())

print(calls)
