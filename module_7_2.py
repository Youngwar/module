from pprint import pprint


def custom_write(file_name, string):
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    j = list()
    for i in string:
        j.append(file.tell())
        result = file.write(f'{i}\n')
    file.close()


    file = open(file_name, 'r', encoding='utf-8')
    i = 0
    for n, line in enumerate(file, 1):

        line = line.rstrip('\n')
        m = (n, j[i])
        string_positions[m] = line
        i += 1
    return string_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
