def print_params(a = 1, b = 'string', c = True):
    print (a, b, c)

print_params()
print_params(1, False, 'Text')
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Something', 1.25, 100]
values_dict = dict (a = 23, b = 'Str', c = True)
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 321]
print_params(*values_list_2, 42)


