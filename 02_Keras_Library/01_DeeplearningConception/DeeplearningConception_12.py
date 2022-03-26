#학습모델 보기, 저장하기, 불러오기5

#학습된 모델 불러오기
#「mnist_mlp_model.h5」에는 모델 아키텍처와 학습된 모델 가중치가 저장되어 있으니, 이를 불러와서 사용해보자. 
#코드 흐름은 다음과 같습니다.
#   1. 모델 불러오는 함수를 이용하여 앞서 저장한 모델 파일로부터 모델을 재형성한다.
#   2. 실제 데이터로 모델을 사용한다. 
#      이때 주로 사용되는 함수가 predict()함수이지만 Sequential기반의 분류모델을 사용할 경우 좀 더 편리하게 사용할 수 있도록 predict_classes()함수를 제공한다.
#      이 함수를 이용하면 가장 확률이 높은 클래스 인덱스를 알려준다.


''''''
# 0. 사용할 패키지 불러오기
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax

# 1. 실무에 사용할 데이터 준비하기
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(10000, 784).astype('float32') / 255.0
y_test = np_utils.to_categorical(y_test)
xhat_idx = np.random.choice(x_test.shape[0], 5)
xhat = x_test[xhat_idx]

# 2. 모델 불러오기
from keras.models import load_model
model = load_model('mnist_mlp_model.h5') #h5py버전이 3.1.0이면 AttributeError 'str' object has no attribute 'decode' 라는 에러가 난다.
                                         #h5py버전을 2.10.0으로 변경해준다.
# 3. 모델 사용하기
yhat = model.predict_classes(xhat)

for i in range(5):
    print('True : ' + str(argmax(y_test[xhat_idx[i]])) + ', Predict : ' + str(yhat[i]))

'''
Q & A
Q1) 모델 아키텍처와 모델 가중치를 따로 저장할 수는 없나요?
A1) 있습니다. 모델 아키텍처는 model.to_json() 함수와 model.to_yaml() 함수를 이용하면 json 혹은 yaml 형식의 파일로 저장할 수 있습니다. 
    가중치는 model.save_weights() 함수로 파일 경로를 인자로 입력하면 h5 형식의 가중치 파일이 생성됩니다. 
    따로 저장한 경우에는 구성 시에도 따로 해야 합니다. 
    모델 아키텍처를 먼저 구성한 뒤 가중치를 불러와서 모델에 셋팅하면 됩니다.

            from models import model_from_json
            json_string = model.to_json()        # 모델 아키텍처를 json 형식으로 저장
            model = model_from_json(json_string) # json 파일에서 모델 아키텍처 재구성

            from models import model_from_yaml
            yaml_string = model.to_yaml()        # 모델 아키텍처를 yaml 형식으로 저장
            model = model_from_yaml(yaml_string) # yaml 파일에서 모델 아키텍처 재구성

Q2) predict_classes() 함수는 Sequential 기반 모델에서만 사용가능한지요?
A2) 네, 맞습니다. functional API 기반 모델은 다수개의 입출력으로 구성된 다양한 모델을 구성할 수 있기 때문에 예측함수의 출력 형태 또한 다양합니다. 
    따라서 클랙스 인덱스를 알려주는 간단한 예측함수는 제공하지 않습니다.
'''

#요약
#학습한 모델을 저장하고 불러오는 방법에 대해서 알아보았다.
#저장된 파일에는 모델 성 및 가중치 정보외에도 학습설정 및 상태가 저장되므로 모델을 불러온 후 재학습을 시킬 수 있다.
#신규 데이터셋이 계속 발생하는 경우에는 재학습 및 평가가 빈번하게 일어날 수 있다.
#또한 일반적인 딥러닝 시스템에서는 학습 처리시간을 단축시키기 위해 GPU나 클러스터 장비에서 학습과정이 이루어지나,
#판정과정은 학습된 모델 결과파일을 이용하여 일반 PC 및 모바일, 임베디드 등에서 이루어진다. 
#이처럼 도메인, 사용목적 등에 따라 운영 시나리오 및 환경이 다양하기 때문에, 딥러닝 모델에 대한 연구도 중요하지만, 
#실무에 적용하기 위해서는 목표시스템에 대한 설계도 중요하다.
