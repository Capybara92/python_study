#리스트
#변수 하나의 데이터만 선언하지 않고 여러개를 선언함(배열)

list1 = []
list2 = [1, 1, 2, 2, "리", "리"]
list3 = [1, 2, 11e-1, -3.4, 8.8]
list4 = ['hi', 'flow', 'coding']
list5 = ['리스트는', 2, '렇게', [4, '용']]
#list1처럼 데이터가 포함되지 않아도 리스트 자료형이다.
#리스트 자료형은 숫자형, 문자열 모두 포함 가능하다.
#중복되는 데이터가 있어도 그 자체로 리스트가 형성된다.

#리스트 인덱싱
#리스트 자료형도 순서를 가지고 있기때문에 문자열처럼 인덱싱 가능
li = ['hi', 'flow', 'coding', 8, 114]
st = [3, ['파', 2, 'sun'], 'good']

#[3, ['파', 2, 'sun'], 'good']
# 0         1             2
#-3        -2            -1

print(li[0], li[2])
print(st[1])
print(st[1][-3])

#인덱싱을 이용한 리스트 수정
li = ['hi', 'flow', 'coding', 8, 114]
li[-1] = 'python'
print(li)

#리스트 슬라이싱(인덱스 번호를 이용해서 리스트를 잘라내는 것)
li = ['hi', 'flow', 'coding', 8, 114]
st = [3, ['파', 2, 'sun'], 'good']

#리스트[시작:끝]
print(li[ :3])
print(st[1: ])
print(st[1][ :-1])
#시작번호부터 끝번호-1 까지만 출력한다.

#del함수(인덱싱과 슬라이싱을 이용하여 삭제 가능)
li = [1, 2, 3, 4, 56, 7]
del li[4] #인덱싱 이용
print(li)

st = [45, 6, 23, 1, 2, 3]
del st[ :3]
print(st)
print()

#리스트 연산 (덧셈 곱셉 연산자 이용하여 반복할 수 있다.)
s = [1, 2, 3]
t = [4, 5, 6]
print(s + t)
print(s*3)

#리스트 관련함수(split, append, sort, reverse)
#split(문자열 나누기)
li = "문자열을 split으로 리스트로 만둘 수 있지"
print(li.split()) #공백이나 띄어쓰기로 나눈다

st = "99:09:01"
print(st.split(':')) #지정한 문자를 기준으로 나눈다.

#append(데이터 추가)
ls = [1, 2, 3, 4]
ls.append(5)
ls.append('육')
print(ls)

#sort(리스트 정렬 : 숫자 혹은 문자가 순서대로 정렬된다.)
lss = [4, 2, 9, 1, 7]
stt = ['c', 'e', 'a', 'b', 'd', 'f']
lss.sort()
stt.sort()
print(lss)
print(stt)

#reverse(리스트 역순정렬)
LR = ['로', '으', '순', '역', '가', '서', '순']
LR.reverse()
print(LR)