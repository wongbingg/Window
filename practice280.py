per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print("0은 입력 불가능 합니다")
    else:
        print("성공")
    finally:
        print("다음단계로")