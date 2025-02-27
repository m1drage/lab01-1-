#рекурсивный метод
def x(n): 
    if isinstance(n,list) == False:
        return 0
    else:
        t = len(n)
        for u in n:
            t += x(u) 
        return t
print(x([1, 2, [3, 4, [5]]]))

#итеративный метод
def y(k):
    if isinstance(k,list) == False:
        return 0
    stack = [k]
    m = 0
    while stack:
        c = stack.pop()
        if isinstance(c,list):
            m += len(c)
            stack.extend(c)
        else:
            m += 0
    return m
print(y([1, 2, [3, 4, [5]]]))
        
        