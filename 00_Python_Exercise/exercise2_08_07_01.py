#파일다루기

#파일 생성하기
#파일객체 = open(파일 이름, 파일 열기 모드)
f = open("연습파일만들기.txt", 'w') #현재 폴더에 생성된다.
f.close() #파일을 열고나면 닫아주는 것이 좋다.
#파일 열기 모드
#'r' 읽기모드(파일을 읽기만 할 때 사용)
#'w' 쓰기모드(파일에 내용을 쓸 때 사용)
#'a' 추가모드(파일의 마지막에 새로운 내용을 추가 시킬 때 사용)
#'x' 새로운 파일을 생성함(존재하면 예외발생)
#'+' 읽고 쓰기용으로 열기
#'b' binary Mode로 열기
#'t' text Mode로 열기

#파일을 쓰기모드로 열면 해당파일이 이미 존재할 경우 원래있던 내용이 모드 사라지고,
#해당 파일이 존재하지 않으면 새로운 파일이 생성된다.

f = open("C:/Users/ALJP1B901504/Desktop/파이썬/연습파일만들기.txt", 'w', encoding='UTF-8') #설정한 경로에 파일을 만들어준다.
for i in range(1, 11, 1):
    data = "%d번째 줄입니다.\n" % i #파이썬도 c언어처럼 이런게 가능하구나.
    f.write(data) #파일에 결과값을 적는다.
f.close()

#f = open("C:/Users/ALJP1B901504/Desktop/파이썬/연습파일만들기.txt", 'w') -> UnicodeEncodeError 에러발생.
#인코딩을 UTF-8로 지정해 주지 않으면 「UnicodeEncodeError 'cp932' codec can't encode character」에러가 발생한다.

#인코딩을 지정해주던지
#f = open('파일명', 'w', encoding='UTF-8') 
#에러를 무시하는 명령을 한다.
#f = open('파일명', 'w', errors='replace') 
#f = open('파일명', 'w', errors='ignore') 