#try, except, else, finally
#예외의 발생여부에 상관없이 항상 실행되도록 하는 코드(finally)
try:
    x = int(input("숫자 입력 : "))
    result = 5 / x
except ZeroDivisionError as e:
    print("예외가 발생했습니다.", e)
else:
    print(result)
finally:
    print("코드실행 완료") #항상 실행