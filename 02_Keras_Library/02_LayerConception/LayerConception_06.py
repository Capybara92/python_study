#컨볼루션 신경망 모델 만들어보기1

#간단한 컨볼루션 신경망 모델을 만들어보자. 다음과 같은 순서로 진행한다.
#   1. 문제 정의하기
#   2. 데이터 준비하기
#   3. 데이터셋 생성하기
#   4. 모델 구성하기
#   5. 모델 학습과정 설정하기
#   6. 모델 학습시키기
#   7. 모델 평가하기

''''''
#문제 정의하기
#좋은 예제와 그와 관련된 데이터셋도 공개된 것이 많이 있지만, 직접 문제를 정의하고 데이터를 만들어보는 것도 처럼 딥러닝을 접하시는 분들에게는 크게 도움이 될 것 같다.
#컨볼루션 신경망 모델에 적합한 문제는 이미지 기반의 분류이다.
#따라서 우리는 직접 손으로 삼각형, 사각형, 원을 그려 이미지로 저장한 다음 이를 분류해보는 모델을 만들어보겠다.
#문제 형태와 입출력을 다음과 같이 정의해본다.
#   - 문제 형태 : 다중 클래스 분류
#   - 입력      : 손으로 그린 삼각형, 사각형, 원 이미지
#   - 출력      : 삼각형, 사각형, 원일 확률을 나타내는 벡터

#가장 처음 필요한 패키지를 불러오고, 매번 실행 시마다 결과가 달라지지 않도록 랜덤 시드를 명시적으로 지정한다.
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

'''
ModuleNotFoundError: No module named 'numpy.core._multiarray_umath'
ImportError: numpy.core.multiarray failed to import

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<frozen importlib._bootstrap>", line 968, in _find_and_load
SystemError: <class '_frozen_importlib._ModuleLockManager'> returned a result with an error set
ImportError: numpy.core._multiarray_umath failed to import
ImportError: numpy.core.umath failed to import
라는 에러가 발생한다. 
pip install scikit-image==0.14.2미만의 버전에서 발생한다.
  -> 이것을 다운로드 해주면 numpy는 최선버전으로 바뀐다.
'''
# 랜덤시드 고정시키기
np.random.seed(3)


''''''
#데이터 준비하기
#손으로 그린 삼각형, 사각형, 원 이미지를 만들기 위해서는 여러가지 방법이 있다.
#테블릿을 이용할 수도 있고, 종이에 그려서 사진으로 찍을 수도 있다.
#이미지 사이즈는 24 x 24 정도로 해본다.

#모양별로 20개 정도를 만들어서 15개를 훈련에 사용하고, 5개를 테스트에 사용해보겠다.
#이미지는 png나 jpg로 저장한다.
#실제로 데이터셋이 어떻게 구성되어 있는 지 모른 체 튜토리얼을 따라하거나 예제 코드를 실행시키다보면 결과는 잘 나오지만 막상 실제 문제에 적용할 때 막막해질 때가 있다.
#간단한 예제로 직접 데이터셋을 만들어봄으로써 실제 문제에 접근할 때 시행착오를 줄이는 것이 중요하다.
#ex) train(circle, triangle, rectangle), test(circle, triangle, rectangle) 폴더를 만듬
