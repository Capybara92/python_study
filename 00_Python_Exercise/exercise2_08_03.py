#에러 메세지 받기
listt = [10, 20, 30]

try:
    index = int(input("인덱스 입력 : "))
    a = int(input("숫자입력 : "))
    print(listt[index] / a)
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

#예외 종류를 지정하지 않고 
#except Exception as 변수:
#를 쓰면 모든 예외의 에러 메세지를 출력한다.
