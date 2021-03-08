def lenght(func):
    def surogate(*args):
        counter = 0
        result = func(*args)
        for arg in args:
            if arg:
                counter += 1
        print(f'Количествоэлементов функции - {counter}')
        return result
    return surogate

@lenght
def sumory(*args):
    total = 0
    for arg in args:
        total += arg
    return total
res = sumory(32, 5, 3)
print(res)

