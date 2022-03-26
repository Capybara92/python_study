from exercise2_07_01 import bae as b, ap as a, main as m
#모듈뿐만이 아니라 요소들의 이름도 지정이 가능하다.

print(b)               #bae 대신 b
print()
a("샐러드", "스프")     #ap 대신 a
m("파스타", "스테이크") #main 대신 m

#변수   가져오기 : from 모듈명 import 변수 as 이름
#함수   가져오기 : from 모듈명 import 함수 as 이름
#클래스 가져오기 : from 모듈명 import 클래스 as 이름