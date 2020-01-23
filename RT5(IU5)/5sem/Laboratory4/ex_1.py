
from librip.gens import field
from librip.gens import gen_random
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
]


test = field(goods,'title')
print("field1:")
for string in test:
    print(string)


test = field(goods,'title', 'price')
print("field2:")
for string in test:
    print(string)


print("\nGenRandom:")
print(gen_random(1, 3, 5))
