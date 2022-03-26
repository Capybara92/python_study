#관계연산자
a = 10
b = 20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#논리연산자
a = True
b = False
print()
print(a and a)
print(a and b)
print(b and b)
print(a or a)
print(a or b)
print(b or b)

#조건문 if
a = 10
b = 20
print()
if a>b:
    print("큰 수 : ", a)
else:
    print("큰 수 : ", b)
#if문에서는 들여쓰기를 안해주면 에러(IndentationError: expected an indented block)가 난다. 1칸(X) 2칸이상(O) Tap(O)

#조건문 if elif
a = int(input("숫자 : "))
if a>10:
    print("10보다 크다")
elif a>5:
    print("10보다 작고 5보다 크다, 혹은 10이다")
else:
    print("5보다 작거나 같다")