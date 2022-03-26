#다층 퍼셉트론 레이어 이야기

#Dense사용예제
#Dense(8, input_dim=4, init='uniform', activation='relu'))

#주요 인자는 다음과 같습니다.
#   - 첫번째 인자 : 출력 뉴런의 수를 설정한다.
#   - input_dim : 입력 뉴런의 수를 설정한다.
#   - init : 가중치 초기화 방법 설정한다.
#           ‘uniform’ : 균일 분포
#           ‘normal’  : 가우시안 분포
#   - activation : 활성화 함수 설정한다.
#           ‘linear’  : 디폴트 값, 입력뉴런과 가중치로 계산된 결과값이 그대로 출력으로 나온다.
#           ‘relu’    : rectifier 함수, 은익층에 주로 쓰인다.
#           ‘sigmoid’ : 시그모이드 함수, 이진 분류 문제에서 출력층에 주로 쓰인다.
#           ‘softmax’ : 소프트맥스 함수, 다중 클래스 분류 문제에서 출력층에 주로 쓰인다.

#Dense 레이어는 입력과 출력을 모두 연결해준다.
#예를 들어 입력 뉴런이 4개, 출력 뉴런이 8개있다면 총 연결선은 32개(4*8=32)이다.
#각 연결선에는 가중치(weight)를 포함하고 있는데, 이 가중치가 나타내는 의미는 연결강도라고 보면된다.
#현재 연결선이 32개이므로 가중치도 32개이다.

#Dense 레이어는 보통 출력층 이전의 은닉층으로도 많이 쓰이고, 영상이 아닌 수치자료 입력 시에는 입력층으로도 많이 쓰안다.
#이 때 활성화 함수로 ‘relu’가 주로 사용된다.
#‘relu’는 학습과정에서 역전파 시에 좋은 성능이 나는 것으로 알려져 있다.

#입력층이 아닐 때에는 이전층의 출력 뉴런 수를 알 수 있기 때문에 input_dim을 지정하지 않아도 된다.
#아래 코드를 보면, 입력층에만 input_dim을 정의하였고, 이후 층에서는 input_dim을 지정하지 않았다.
'''
model.add(Dense(8, input_dim=4, init='uniform', activation='relu'))
model.add(Dense(6, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
'''
