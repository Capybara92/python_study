#딕셔너리(dictionary)
#연관관계를 나타내는 자료형
#EX) 아이스크림=구구콘, 우유=초코우유
#key와value를 한쌍으로 갖는 자료형 {key : value}

dic = {'마블':'어벤져스', 'DC':'배트맨', '디즈니':'겨울왕국'}
print(dic['DC'])
#value를 얻기 위해서는 key를 이용한다.

#딕셔너리의 추가 삭제
mv = {'마블':'어벤져스', 'DC':'배트맨'}
mv[3] = '조커' #key가3이고 value가 조커인 데이터를 추가
print(mv)

del mv[3] #key가3인 데이터를 삭제
print(mv)

#주의할점 : 동일한key에 여러개의 value는 존재할 수 없다.
#가장 마지막에 설정한 value만이 그 키에 남게된다
dic = {'마블':'어벤져스', '마블':'배트맨', '디즈니':'겨울왕국'}
print(dic['마블']) #배트맨
print(dic) #{'마블': '배트맨', '디즈니': '겨울왕국'}
#key는 고유한 값이므로 동일한 key값이 있으면 Warning이 나온다.

#key에는 변하지 않는 값만 쓸수 있다.(튜플, 문자형, 숫자형)
#리스트는 값이 변하기 때문에 안된다.
#dic1 = {[1, 2, 3]:'숫자형'} -> TypeError unhashable type: 'list'

#딕셔너리 함수 사용하기
#update(딕셔너리 병합)
mv = {'겨울왕국':'엘사', '다크나이트':'배트맨', '어벤져스':'아이언맨'}
ch = {'EBS':'펭수', 'MBC':'유산슬'}
mv.update(ch) #mv끝에ch가 병합된다.
print(mv)

#keys(key의 리스트 얻기)
mv = {'겨울왕국':'엘사', '다크나이트':'배트맨', '어벤져스':'아이언맨'}
print(mv.keys()) #key만을 모아서 객체로 돌려준다.

#values(value의 리스트 얻기)
mv = {'겨울왕국':'엘사', '다크나이트':'배트맨', '어벤져스':'아이언맨'}
print(mv.values()) #value만을 모아서 객체로 돌려준다.

#itmes(key:value의 리스트 얻기)
mv = {'겨울왕국':'엘사', '다크나이트':'배트맨', '어벤져스':'아이언맨'}
print(mv.items()) #key:value쌍을 튜플로 묶어서 객체로 돌려준다.