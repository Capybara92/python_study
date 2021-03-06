#문자열
#문자열 인덱싱(문자열의 글자에 번호를 지정)
h1 = "파이썬 공부는 즐거워!"

#파   이   썬      공  부  는      즐  거  워   !
#0    1    2   3   4   5   6   7   8   9  10  11
#-12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

print(h1[2])  #썬
print(h1[6])  #는
print(h1[-1]) #!

#문자열 슬라이싱(번호를 이용하여 문자열을 잘라냄)
#문자열[시작:끝]
print(h1[4:7]) 
print(h1[-4: ]) #끝   번호가 없으면 마지막 문자까지 출력
print(h1[ :4])  #시작 번호가 없으면 첫번째 문자부터 출력
print(h1[4:-1])
#시작번호부터 끝번호-1 까지만 출력한다.
#순서대로의 인덱스 번호와 역순의 인덱스 번호의 혼용 가능.

#문자 개수 함수「문자열.count(문자)」
cod = "flow coding"
print()
print(cod.count("o"))

#문자열 길이 함수「len(문자열)」
cod = "코딩은 너무 즐거워!"
print(len(cod))

#인덱스 번호 알려주기「문자열.index(문자)」
cod = "I love coding :)"
print(cod.index("o"))
#처음으로 나오는 위치 인덱스를 반환한다.
#찾으려고 하는 문자가 없다면 오류를 출력한다.

#문자열 바꾸기「문자열.replace(바꿀문자1, 적용문자2)」
cod = "파이썬은 너무 즐거워!"
print(cod.replace("파이썬", "코딩"))
#바꿀 문자가 없으면 그대로 출력한다