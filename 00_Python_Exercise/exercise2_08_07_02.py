#외부에 저장된 파일을 읽어오기
#readline 함수
f = open("C:/Users/ALJP1B901504/Desktop/파이썬/연습파일만들기.txt", 'r', encoding='UTF-8') #'r'읽기모드
line = f.readline()#첫 번째 줄을 읽어온다. #첫 번째 줄을 읽어온 후 빈 문자열을 리턴한다.
print(line)
f.close()

f = open("C:/Users/ALJP1B901504/Desktop/파이썬/연습파일만들기.txt", 'r', encoding='UTF-8') #'r'읽기모드
while True: #무한루프를 돌면서
    line = f.readline() #한줄씩 읽어들인다.
    if not line: break  #더 이상 읽을 줄이 없을 경우 break
    print(line)
f.close()

#readlines 함수
f = open("C:/Users/ALJP1B901504/Desktop/파이썬/연습파일만들기.txt", 'r', encoding='UTF-8') #'r'읽기모드
lines = f.readlines()#파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
for line in lines: #for문으로 한줄씩 출력한다.
    print(line)
f.close()

#read 함수
f = open("C:/Users/ALJP1B901504/Desktop/파이썬/연습파일만들기.txt", 'r', encoding='UTF-8') #'r'읽기모드
data = f.read() #줄과 줄 사이에 공백 없이 받아온다.
print(data)
f.close()