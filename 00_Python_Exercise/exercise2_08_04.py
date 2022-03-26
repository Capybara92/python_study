#try, except, else
#예외가 발생하지 않는 경우 실행되는 코드를 한눈에 보기 위하여.
#예외가 발행하지 않는 경우 실행할 코드를 따로 지정하는 방법.
try:
    x = int(input("숫자 입력 : "))
    result = 5 / x
except ZeroDivisionError as e:
    print("예외가 발생했습니다.", e)
else:
    print(result)
#예외가 발생하지 않는 경우 else문의 코드가 실행된다.