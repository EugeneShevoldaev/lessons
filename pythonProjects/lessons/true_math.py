from  math import  inf
# first =int(input('введите  делимое: '))
# second =int(input('введите  делитель: '))

first = 49
second = 7
def divide(first, second):
    if second == 0:
       return inf
    else:
        resolt = round(first / second, 2)
    return  resolt

print(divide(first, second))