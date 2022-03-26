#예외처리
#예외 상황에 대해서 프로그램을 멈추지 않고 원하는 코드를 실행하도록 하는 것.

#에러종류
#ZeroDivisionError(숫자를 0으로 나눌 경우)
#print(5/0)

#IndexError(인덱싱을 할 때 얻을 수 없는 인덱스를 가르키는 경우)
#st = [1, 2, 3]
#print(st[3])

#ValueError(값의 형식이 잘못된 경우)
#TypeError(연산 중 자료형이 다른 경우)
#KeyError(사전에서 없는 키를 입력한 경우)
#FileNotFoundError(존재하지 않는 파일을 불러올 경우)

#try, except
try:
    x = int(input("숫자 입력 : "))
    result = 5 / x
    print(result)
except:
    print("예외가 발생했습니다.")
    #어떤 오류가 발생하든 "예외가 발생했습니다"가 출력된다.