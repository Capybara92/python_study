#집합(set)
#수학에서 배운 집합이 파이썬에서도 존재한다.
#중괄호({})를 이용하고 콤마(,)로 구분

sett = {'사빠딸', '민초', '슈팅스타', '쿠앤크', '엄마는외계인', '사빠딸', '쿠앤크'}
print(sett)
#출력을 해보면 할때마다 결과가 달라진다. (집합 자료형의 특징)
#집합은 중복을 허용하지 않는다.
#집합은 순서가 없는 자료형이다.
#인덱싱 슬라이싱 불가능

ps = ['선배님', '도와주세요', '선배님', '떤배님', '엣헴', '신이나', '신이나', 1, 1, 12, 3] #리스트 생성

ss = set(ps) #집합으로 중복데이터를 제거
print(ss) #순서가 뒤바뀐 결과가 나옴

tu = tuple(ss) #집합을 튜플로 만듬
print(tu)      #튜플 출력
print(tu[0])   #튜플은 인덱싱이 가능함
#집합을 인덱식 혹은 슬라이싱을 하려면 가능한 자료형으로 변환 후 해야한다.

#합집합, 차집합, 교집합
set1 = {'사랑에빠진딸기', '민트초코칩', '슈팅스타', '레인보우샤베트', '엄마는외계인'}
set2 = {'뉴욕치즈케이크', '사랑에빠진딸기', '엄마는외계인', '쿠키앤크림'}
print(set1 & set2) #교집합 : set1, set2에 모두 포함되어 있는 데이터
print(set1 | set2) #합집합 : set1, set2의 합쳐진 결과
print(set1 - set2) #차집합 : set1, set2에 모두 포함된 데이터를 제외한 set1데이터
#집합이기에 데이터의 순서가 매번 다르게 나온다