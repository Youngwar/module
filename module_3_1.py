calls = 0


def count_calls():
     global calls
     calls += 1
     return calls

def string_info(string_):
    
    count_calls()
    return ({len(string_), string_.upper(), string_.lower()})

def is_contains (str_, list_):
    
    k = False
    for i in range (0, len(list_)):

        if str_.lower() in list_[i].lower():
            k = True
    count_calls()
    return (k)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
