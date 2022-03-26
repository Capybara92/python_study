'''
#파일에 새로운 내용 추가하기
f = open("C:/Users/ALJP1B901504/Desktop/파이썬/연습파일만들기.txt", 'a', encoding='UTF-8') #'a' 추가모드
for i in range(11, 20, 1):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

#with문과 함께 사용하기
#파일을 열면 close()함수로 닫아줘야 해서 너무 귀찮다.
#하지만, with함수를 쓰면 close()함수로 닫아주지 않아도 저절로 닫힌다.
with open("foo.txt", "w") as f: #with블록을 벗어나는 순간 자동으로 close된다.
    f.write("Life is too short, you need python")