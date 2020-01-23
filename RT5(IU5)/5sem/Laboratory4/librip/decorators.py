def print_result(func):
    def decarted(*args, **kwargs):
        print(func.__name__)
        result = func(*args,**kwargs)
        if type(result) == list:
            for value in result:
                print(value)
        elif type(result) == dict:
            for parameter, value in result.items():
                print(parameter, "=", value)
        else:
            print(result)
        return result
    return decarted
