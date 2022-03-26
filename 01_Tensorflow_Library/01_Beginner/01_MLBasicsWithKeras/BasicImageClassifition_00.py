#기본 이미지 분류

#운동화나 셔츠같은 옷 이미지를 분류하는 신경망 모델을 훈련1
#텐서플로 모델을 만들고 훈련할 수 있는 고수준 API인 tf.keras를 사용한다.

''''''
#tensorflow와 tf.keras를 임포트합니다
import tensorflow as tf
from tensorflow import keras

#헬퍼(helper) 라이브러리를 임포트합니다
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

''''''
#패션 MNIST는 컴퓨터 비전 분야의 "Hello, World" 프로그램격인 고전 MNIST데이터셋을 대신해서 자주 사용된다.
#MNIST데이터셋은 손글씨 숫자(0, 1, 2 등)의 이미지로 이루어져 있다.
#여기서 사용하려는 옷 이미지와 동일한 포맷이다.

#패션 MNIST는 일반적인 MNIST 보다 조금 더 어려운 문제이고 다양한 예제를 만들기 위해 선택했다.
#두 데이터셋은 비교적 작기 때문에 알고리즘의 작동여부를 확인하기 위해 사용되곤 한다.
#코드를 테스트하고 디버깅하는 용도로 좋다.

#네트워크를 훈련하는데 60,000개의 이미지를 사용한다.
#그 다음 네트워크가 얼마나 정확하게 이미지를 분류하는지 10,000개의 이미지로 평가한다.
#패션 MNIST데이터셋은 텐서플로에서 바로 import하여 적재할 수 있다.
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() #4개의 파일[(train_images, train_labels), (test_images, test_labels)]을 다 다운로드 해줘야 한다.

#(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data(path='train-labels-idx1-ubyte')
#load_data()함수를 호출하면 네 개의 넘파이(NumPy)배열이 반환된다.
#train_images와 train_labels 배열은 모델 학습에 사용되는 훈련 세트이다.
#test_images와 test_labels 배열은 모델 테스트에 사용되는 테스트 세트이다.
#이미지는 28x28 크기의 Numpy배열이고 픽셀값은 0과 255사이이다.
#레이블(label)은 0에서 9까지의 정수 배열이다.
#이 값은 이미지에 있는 옷의 클래스(class)를 나타낸다.
'''
레이블	클래스
0	    T-shirt/top
1	    Trouser
2	    Pullover
3	    Dress
4	    Coat
5	    Sandal
6	    Shirt
7	    Sneaker
8	    Bag
9	    Ankle boot
'''

''''''
#각 이미지는 하나의 레이블에 매핑되어 있다.
#데이터셋에 클래스 이름이 들어있지 않기 때문에 나중에 이미지를 출력할 때 사용하기 위해 별도의 변수를 만들어 저장한다.
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

''''''
#모델을 훈련하기 전에 데이터셋 구조를 살펴보자.

#다음 코드는 훈련세트에 60,000개의 이미지가 있다는 것을 보여준다.
#각 이미지는 28x28 픽셀로 표현된다.
print(train_images.shape)

#훈련 세트에는 60,000개의 레이블이 있다.
print(len(train_labels))

#각 레이블은 0과 9사이의 정수이다.
print(train_labels)

#테스트 세트에는 10,000개의 이미지가 있다.
#이 이미지도 28x28 픽셀로 표현된다.
print(test_images.shape)

#테스트 세트는 10,000개의 이미지에 대한 레이블을 가지고 있다.
print(len(test_labels))

''''''
#데이터 전처리
#네트워크를 훈련하기 전에 데이터를 전처리 해야한다.
#훈련 세트에 있는 첫 번째 이미지를 보면 픽셀 값의 범위가 0~255 사이라는 것을 알 수 있다.
plt.figure()
plt.imshow(train_images[0]) #2D 데이터를 수치정도에 따라 색으로 표현
plt.colorbar()
plt.grid(False)
plt.show()

#신경망 모델에 주입하기 전에 이 값의 범위를 0~1 사이로 조정하겠다.
#이렇게 하려면 255로 나누어야 합니다.
#훈련 세트와 테스트 세트를 동일한 방식으로 전처리하는 것이 중요하다.
train_images = train_images / 255.0
test_images = test_images / 255.0

#훈련 세트에서 처음 25개 이미지와 그 아래 클래스 이름을 출력해 보자.
#데이터 포맷이 올바른지 확인하고 네트워크 구성과 훈련할 준비를 마친다.
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.get_cmap('binary')) #binary 스케일 컬러 맵
    #cmap : colorMap #plt.cm.binary은 에러가 난다.
    #plt.cm을 꼭 쓰고싶으면 -> cmap=plt.cm.get_cmap(plt.get_cmap('binary')) 로 한다.
    plt.xlabel(class_names[train_labels[i]])
plt.show()
