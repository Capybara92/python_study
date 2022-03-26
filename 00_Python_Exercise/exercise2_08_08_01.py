#csv 파일 읽어오기
import csv #파이선에서는 csv파일을 핸들링 할 수 있는 모듈을 제공한다.

'''
with open("C:/Users/ALJP1B901504/Desktop/파이썬/엑셀파일_불러오기.csv", 'r', encoding='UTF-8') as f: #'r' 읽기모드
    reader = csv.reader(f)

    print(reader) #<_csv.reader object at 0x0000025EB5271118>이 출력되면 읽기 성공
    print(type(reader)) #형태를 출력해 준다.
    print(dir(reader)) #사용할 수 있는 메소드를 확인해 준다.
                       #__iter__가 보이면, 우리는 반복문에서 사용 할 수 있다는 것을 알 수 있다.

    for txt in reader:
        print(txt)

with open("C:/Users/ALJP1B901504/Desktop/파이썬/엑셀파일_불러오기.csv", 'r', encoding='utf-8-sig') as f: #utf-8-sig는 출력에 \ufeff 를 빼고 출력해준다.
    reader = csv.reader(f, delimiter='|') #리스트 형태로 가져다 준다

    print(reader) 
    print(type(reader)) 
    print(dir(reader)) 

    for txt in reader:
        print(txt)
'''

with open("C:/Users/ALJP1B901504/Desktop/파이썬/엑셀파일_불러오기.csv", 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f) #딕셔너리 형태로 변환해 출력한다.

    #for txt in reader:
    #    print(txt)

    #key와 value를 나누어서 출력하기
    for c in reader: 
        for k, v in c.items(): #items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 객체로 돌려준다.
            print(k, v) 
        print("===================")