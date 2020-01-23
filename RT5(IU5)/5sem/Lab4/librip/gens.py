
import random

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for value in items:
            temp = value.get(args[0])
            if temp is not None:
                yield temp
    else:
        for value in items:
            temp = {key: value.get(key) for key in args if value.get(key) is not None}
            if len(temp) != 0:
                yield temp
    # Необходимо реализовать генератор

def gen_random_one_string(begin, end, num_count):
    return list(random.randint(begin, end) for n in range(num_count))

def gen_random(begin, end, num_count):
    mass = list()
    while num_count != 0:
        mass.append(random.randint(begin, end))
        num_count -= 1
    return mass

