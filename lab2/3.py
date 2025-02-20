for x in range(174457,174506):
    k=0
    s=[]
    for d in range(2,x//2+1):
        if x%d==0:
            k+=1
            s.append(d)
            if k>2:
                break
    if k==2:
        print(*s)