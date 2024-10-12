def is_prime(func):
    def wrapper(a, b, c):
        i = func(a, b, c)

        if i < 2: print("Простое")
        for k in range (2, i):
            if i % k == 0:
                print('Составное')
                break
            elif k == (i-1):
                print("Простое")
                break
            else: continue
        return i
    return wrapper
@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    return sum_

result = sum_three(2, 3, 6)
print(result)