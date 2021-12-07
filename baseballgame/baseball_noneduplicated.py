import random
rn = [0,0,0]
rn[0] = random.randrange(1,9,1)
rn[1] = random.randrange(1,9,1)
while rn[0] == rn[1]:
    rn[1] = random.randrange(1,9,1)

rn[2] = random.randrange(1,9,1)
while rn[1] == rn[2] or rn[0] == rn[2]:
    rn[2] = random.randrange(1,9,1)


while rn[0] != rn[1] and rn[1] != rn[2] and rn[0] != rn[2]:
    rn = [0,0,0]
    rn[0] = random.randrange(1,9,1)
    rn[1] = random.randrange(1,9,1)
    while rn[0] == rn[1]:
        rn[1] = random.randrange(1,9,1)
  
    rn[2] = random.randrange(1,9,1)
    while rn[1] == rn[2] or rn[0] == rn[2]:
        rn[2] = random.randrange(1,9,1)
    print(rn)
  
