import itertools
s = "тимофей"
ar = itertools.product(s, repeat=5) 
# a = []
# for i in ar:
#     a.append(list(i))
count = 0
for e in ar:
    flag = True
    for i in range(len(e) - 1):
        if e.count('й') > 1 or e[0] == 'й' or e[-1] == 'й' or (e[i] == 'й' and e[i + 1] == 'и') or (e[i + 1] == 'й' and e[i] == 'и'):
            flag = False
    if flag == True: count += 1
print(count)