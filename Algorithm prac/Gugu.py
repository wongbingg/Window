import sys
n = int(sys.stdin.readline())
rn=0
for i in range(1,10000):
    rn += i
    if n<=rn:
        apart=rn-n
        if i ==1 or i%2==0:
            print(i-apart,'/',apart+1,sep='')
            
            
            break
        else:
            print(apart+1,'/',i-apart,sep='')
            break


