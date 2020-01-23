class Gist:
    # данные гистаграммы

    def __init__(self, ages):

        self._data_sorting = dict()
        for number in ages:
            self._data_sorting.update(
                {number: self._data_sorting.get(number, 0) + 1})

    def print_hist(self):

        str_out = ""
        for age, stat in self._data_sorting.items():
            str_out += str(age).ljust(3) + str().ljust(stat, '#') + '\n'
        print(str_out)
