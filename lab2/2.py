x = 4**2020 + 2**2017 - 15
s = ''
while x != 0:
    s += str(x % 2) 
    x //= 2
s = s[::-1]
print(s.count("1"))