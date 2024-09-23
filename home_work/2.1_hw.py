from typing import Tuple


def task_1() -> Tuple[type, type, type, type, type, type]:
    a = 20
    b = 20.5
    c = "Анальгин"
    d = [1,2,3,4]
    i = True
    return type(a), type(b), type(c), type(d), type(i)

result = task_1()
print(result)