def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()
#inner_function()
# При попытке вызова функции которая находится внутри другой функции выдает ошибку, функция не обнаружена, что свидетельствует о том что данная функция находится в другой области видимости.
# inner_function()
# ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?