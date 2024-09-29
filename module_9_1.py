def apply_all_func(int_list, *functions):
    dict_ = {}
    for i in functions:
        x = i(int_list)
        dict_[i.__name__] = x
    return dict_


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))