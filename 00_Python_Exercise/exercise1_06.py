#for반복문 「for 변수이름 in range(범위)」
for count in range(5): #0이상 5미만
    print(count)

for count in range(1, 5): #1이상 5미만
    print(count)

for count in range(1, 5, 2): #1이상 5미만, 2씩증가
    print(count)
#for문의 변수를 따로 초기화 시켜주지 않아도 된다.

#break -> 반복문을 빠져나간다.
#continue -> 반복문 조건으로 돌아간다

#이중 for문
for dan in range(1, 4):
    print("구구단을 외자 ", dan, " 단")
    for i in range(1, 10):
        print(dan, " * ", i, " = ", dan*i)