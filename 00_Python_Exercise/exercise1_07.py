#함수정의, 함수호출
def yes(): #yes라는 이름의 함수정의
    print("Yes I can!")

yes()      #yes라는 이름의 함수호출
#함수정의와 함수호출의 순서가 바뀌면 에러가 난다

#return 함수
def joker1():
    return "Why so serious?"

print(joker1())
joker1() #return은 받았지만 출력을 해주지 않았기에 아무런 일이 발생하지 않는다.

#함수의 입력값(매개변수, 인수)
def joker2(say):
    print("웃으며", say)

joker2("Why so serious?")

def add(x, y):
    return x+y

print(add(1, 3))

def minus(a, b):
    return a-b

print(minus(3, 3))