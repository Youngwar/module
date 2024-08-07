
def get_multiplied_digits(number):
    i = 0
    str_number = str(number)

    while i < len(str_number):

        if int(str_number[i]) == 0:
            i += 1
            continue
        else:
            first = int(str_number[i])
            if len(str_number) > 1:

                return first * get_multiplied_digits(int(str_number[1:]))
        
            else:
                return first
result = get_multiplied_digits('00123456')
print(result)

