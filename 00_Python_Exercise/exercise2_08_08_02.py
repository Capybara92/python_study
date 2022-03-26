#엑셀 파일 읽어오기
#엑셀파일은 xsl, xlsx가 있고, 엑셀을 읽을 수 있는 많은 오픈소스가 있다.
#여러 오픈소스 모듈들이 있지만 그 중에서 가장 많이 사용하는 것은 pandas 이다.

#pandas뿐만 아니라 xlrd도 다운로드 받아야한다.
#xlrd 버전은 2.0.1은 XLRDError Excel xlsx file 에러가 발생하기에 1.2.0버전으로 한다.

import pandas as pd

#xlsx = pd.read_excel("파일경로", sheetname = '시트명 or 숫자' , header = 숫자, skiprows=[], usecols=[], pares_cols="", encoding="")
xlsx = pd.read_excel("C:/Users/ALJP1B901504/Desktop/파이썬/엑셀파일_불러오기.xlsx", skiprows=[2], usecols=[3,4,5])
#아무 오류가 나지 않으면, pandas를 이용해 엑셀을 열기에 성공한 것이다.
#sheetname : 해당하는 시트의 정보를 가져온다.
#header    : 헤더로 설정 할 숫자 ex) header=2 -> 2열의 값을 행 머리글로 이용
#skiprows  : 특정 행만 이용 안 하겠다는 의미 
#usecols   : 특정 열만 이용하겠다는 의미
#pares_cols: 특정 열만 이용하겠다는 의미
#encoding  : "utf-8"은 파일 내 한글이 있을 경우, 한글을 깨지지 않게 하기 위해

#상위 데이터 확인 
print(xlsx.head()) #위의 일부 데이터를 출력
print() 
print(xlsx.tail()) #아래의 일부 데이터를 출력
print() 
print(xlsx.shape) #행, 열 수를 출력한다.
print()
print(xlsx) #모든 정보를 출력한다. #NaN, Unnamed으로 출력되는 것은 공백이라는 뜻이다.