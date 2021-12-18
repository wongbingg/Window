import sys
q = int(sys.stdin.readline())
lst=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]

for _ in range(q):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for j in range(k): #k층
        lst2=[]
        for i in range(n): #n호 일 때
            lst2.append(sum(lst[j][:(i+1)]))
    lst.append(lst2)
print(lst[k-1][n-1])
print(lst[k][n-1])


