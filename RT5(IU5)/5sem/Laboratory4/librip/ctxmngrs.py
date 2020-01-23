# -*- coding: utf-8 -*-

import time

# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

class timer:
    start = 0
    def __enter__(self):
        self._start = time.time()
    def __exit__(self, exp_type, exp_value, traceback):
         print("время:",round(time.time() - self._start,3))
