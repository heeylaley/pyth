# Из задания не очень поняла нужно ли запрашивать ввод x и y поэтому подставила значения в коде
# 1й способ
from functools import reduce

pow_lam = round((lambda x, y: x ** y)(12, -3), 5)


# 2й способ
def pow_func(x, y):
    n = 0
    new_list = []
    while n < abs(y):
        n += 1
        new_list.append(x)
    res = int(reduce(lambda a, b: a * b, new_list))
    return round(1 / res, 5)


print(pow_lam)
print(pow_func(12, -3))
