#raise(예외 발생시키기)
#일부러 예외를 발생시키기.
#이 경우 에러 메세지는 생략이 가능하다.
try:
    x = int(input("숫자 입력 : "))
    if(x!=4):
        raise Exception("원하는 숫자가 아님")
    print(x)
except Exception as e:
    print(e)