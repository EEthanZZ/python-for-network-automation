import random


def MAC_add():
    a = list(range(0,10))
    b = ["A", 'B', 'C', 'D', 'E', 'F']
    c = a + b
    d = str(c[random.randint(0, 15)]) + str(c[random.randint(0, 15)])
    return d


print(f'{MAC_add()}:{MAC_add()}:{MAC_add()}:{MAC_add()}:{MAC_add()}:{MAC_add()}')