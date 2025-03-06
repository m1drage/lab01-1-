def count(operation, initial=0):
    def calc(value):
        nonlocal initial
        if operation == '+':
            initial += value
        if operation == '-':
            initial -= value
        if operation == '*':
            initial *= value
        if operation == '/':
            if value != 0:
                initial /= value
            else:
                raise ValueError("нельзя делить на 0")
        return initial
    return calc

calc = count("/", initial=1)
print(calc(5))  
print(calc(2))  


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


def f(memy):
    return f"{memy}!"
print(f("mama"))
   





        