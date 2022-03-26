'''
케라스란?

케라스는 파이썬으로 구현된 쉽고 간결한 딥러닝 라이브러리이다.
딥러닝 비전문가라도 각자 분야에서 손쉽게 딥러닝 모델을 개발하고 활용할 수 있도록 케라스는 직관적인 API를 제공하고 있다.
내부적으로는 텐서플로우(TensorFlow), 티아노(Theano), CNTK 등의 딥러닝 전용엔진이 구동되지만 케라스 사용자는 복잡한 내부엔진을 알 필요는 없다. 
직관적인 API로 쉽게 「다층퍼셉트론 모델」, 「컨볼루션 신경망 모델」, 「순환 신경망 모델」 또는 「이를 조합한 모델」은 물론 「다중입력」 또는 「다중출력」 등 다양한 구성을 할 수 있다.

케라스(κέρας)는 그리스어로 뿔을 의미한다.
'''

'''
케라스 주요특징(4가지)

1. 모듈화 (Modularity)
    케라스에서 제공하는 모듈은 독립적이고 설정 가능하며, 가능한 최소한의 제약사항으로 서로 연결될 수 있다.
    모델은 시퀀스 또는 그래프로 이러한 모듈들을 구성한 것이다.
    특히 신경망 층, 비용함수, 최적화기, 초기화기법, 활성화함수, 정규화기법은 모두 독립적인 모듈이며, 새로운 모델을 만들기 위해 이러한 모듈을 조합할 수 있다.

2. 최소주의 (Minimalism)
    각 모듈은 짥고 간결하다.
    모든코드는 한 번 훏어보는 것으로도 이해가 가능해야 한다.
    단, 반복속도와 혁신성에는 다소 떨어질 수가 있다.

3. 쉬운 확장성
    새로운 클래스나 함수로 모듈을 아주 쉽게 추가할 수 있다.
    따라서 고급연구에 필요한 다양한 표현을 할 수 있다.

4. 파이썬 기반
    Caffe처럼 별도의 모델 설정 파일이 필요없으며 파이썬 코드로 모델들이 정의된다.

#케라스를 개발하고 유지보수하고 있는 사람은 구글 엔지니어인 프랑소와 쏠레(François Chollet)이다.
'''