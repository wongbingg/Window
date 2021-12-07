#적의 숫자
import random

rn = [0,0,0]
rn[0] = random.randrange(1,9,1)
rn[1] = random.randrange(1,9,1)
rn[2] = random.randrange(1,9,1)
while rn[0] == rn[1]:
    rn[1] = random.randrange(1,9,1)
while rn[1] == rn[2] or rn[0] == rn[2] :
    rn[2] = random.randrange(1,9,1)

#기본값
s_cnt = 0
t_cnt = 0
b_cnt = 0

#게임시작
print("------------------")
print('게임을 시작합니다!!')

while s_cnt < 3:    
    s_cnt = 0
    b_cnt = 0 

    #숫자입력
    my_num =[0,0,0] 
    mn_in= input("3자리 숫자를 입력하시오: ")
    a=mn_in.split(",")
    my_num[0] = int(a[0])
    my_num[1] = int(a[1])
    my_num[2] = int(a[2])

    #중복숫자 입력시!
    while my_num[0] == my_num[1] or my_num[0] == my_num[2] or my_num[1] == my_num[2] :
        print("중복되는 숫자는 입력 불가능 합니다")
        mn_in= input("3자리 숫자를 입력하시오: ")
        a=mn_in.split(",")
        my_num[0] = int(a[0])
        my_num[1] = int(a[1])
        my_num[2] = int(a[2])
        if my_num[0] != my_num[1] and my_num[0] != my_num[2] and my_num[1] != my_num[2]:
            break
        

    #숫자 S,B 판별과정    
    for i in range(0,3):
        for j in range(0,3):
            if rn[i] == my_num[j] and i == j:
                s_cnt += 1
            elif rn[i] == my_num[j] and i != j:
                b_cnt += 1

    #입력값에 대한 출력값            
    print("%d 스트라이크 %d 볼!!" % (s_cnt,b_cnt))

    #시도횟수 늘어남
    t_cnt += 1

#정답일 시 
print("-----------------------------------")
print("%d 번의 시도 끝에 정답을 맞추셨습니다~" %t_cnt)



    




    
        

    
    

