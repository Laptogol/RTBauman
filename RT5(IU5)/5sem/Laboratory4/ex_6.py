#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import argparse
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import unique

def create_Parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-P', '--path', default = 'data_light.json') #путь к источнику
    return parser

#проверка аргументов командной строки
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print('Exception:: Недостаточно параметров командной строки')
        raise SystemExit(1)
    parser = create_Parser()
    namespace = parser.parse_args(sys.argv[1:])

path = namespace.path


with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(unique([i for i in field(arg, 'job-name')], ignore_case = False), key=lambda x:x.lower())


@print_result
def f2(arg):
    return filter(lambda x: "программист" in x, arg)


@print_result
def f3(arg):
    return list(map(lambda x: "{0} с опытом Python".format(x), arg))


@print_result
def f4(arg):
    return ["{0}, зарплата {1} руб.".format(x, y) for x, y in zip(arg, list(gen_random(100000, 200000, len(arg))))]


with timer():
   f4(f3(f2(f1(data))))
