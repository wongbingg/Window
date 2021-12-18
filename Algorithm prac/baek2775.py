import sys
q = int(sys.stdin.readline())
prt=[]
for _ in range(q):
    lst=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for j in range(k): #k층
        lst2=[]
        for i in range(n): #n호 일 때
            lst2.append(sum(lst[j][:(i+1)]))
        lst.append(lst2)
    prt.append(lst[k][n-1])
for k in prt:
    print(k)


