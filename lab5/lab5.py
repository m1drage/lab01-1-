from functools import reduce


def prostoe(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generator(limit):
    for num in range(2, limit +1):
        if prostoe(num):
            yield num
            
def calc(limit):
    p = list(generator(limit))
    sum = reduce(lambda x,y: x+y, p)
    return sum

limit = 100
result = calc(limit)
print(f'Для лимита:', limit, f'сумма равна:', result)




        