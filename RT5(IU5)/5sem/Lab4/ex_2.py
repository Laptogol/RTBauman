#!/usr/bin/env python3
from librip.gens import gen_random
from librip.gens import gen_random_one_string
from librip.iterators import unique

data1 = list(i for i in unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2], ignore_case=True))
data2 = list(i for i in unique(gen_random(1, 3, 10),ignore_case=True))

data4 = list(i for i in unique(['a', 'A', 'b', 'B'], ignore_case=True))
data5 = list(i for i in unique(['a', 'A', 'b', 'B'], ignore_case=False))
print(data1)
print(data2)
print(data4)
print(data5)
 #Реализация задания 2
