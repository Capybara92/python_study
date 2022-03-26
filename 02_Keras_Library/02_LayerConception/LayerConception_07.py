#컨볼루션 신경망 모델 만들어보기2

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

np.random.seed(3)

#데이터셋 생성하기
#케라스에서는 이미지 파일을 쉽게 학습시킬 수 있도록 ImageDataGenerator 클래스를 제공한다.
#ImageDataGenerator 클래스는 데이터 증강 (data augmentation)을 위해 막강한 기능을 제공하는데,
#여기서는 특정 폴더에 이미지를 분류 해놓았을 때 이를 학습시키기 위한 데이터셋으로 만들어주는 기능을 사용해보겠다.

#먼저 ImageDataGenerator 클래스를 이용하여 객체를 생성한 뒤 flow_from_directory() 함수를 호출하여 제네레이터(generator)를 생성한다.
#flow_from_directory() 함수의 주요인자는 다음과 같다.
#   - 첫번재 인자  : 이미지 경로를 지정한다.
#   - target_size : 패치 이미지 크기를 지정한다. 폴더에 있는 원본 이미지 크기가 다르더라도 target_size에 지정된 크기로 자동 조절된다.
#   - batch_size  : 배치 크기를 지정한다.
#   - class_mode  : 분류 방식에 대해서 지정한다.
#   - categorical : 2D one-hot 부호화된 라벨이 반환된다.
#               binary (1D 이진 라벨이 반환된다.)
#               sparse (1D 정수 라벨이 반환된다.)
#               None   (라벨이 반환되지 않는다.)

#패치 이미지 크기를 200x200픽셀로 하였으니 target_size도 (200, 200)으로 셋팅하였다. 
#훈련 데이터 수가 클래스당 15개이니 배치 크기를 3으로 지정하여 총 5번 배치를 수행하면 하나의 epoch가 수행될 수 있도록 하였다.
#다중 클래스 문제이므로 class_mode는 ‘categorical’로 지정하였다.
#그리고 제네레이터는 훈련용과 검증용으로 두 개를 만들었다.
train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'handwriting_shape/train',
        target_size=(200, 200),
        batch_size=3,
        class_mode='categorical')

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        'handwriting_shape/test',
        target_size=(200, 200),    
        batch_size=3,
        class_mode='categorical')


''''''
#모델 구성하기
#영상분류에 높은 성능을 보이고 있는 컨볼루션 신경망 모델을 구성해보자.
#   - 컨볼루션 레이어 : 입력 이미지 크기 200 x 200, 입력 이미지 채널 3개, 필터 크기 3 x 3, 필터 수 32개, 활성화 함수 ‘relu’
#   - 컨볼루션 레이어 : 필터 크기 3 x 3, 필터 수 64개, 활성화 함수 ‘relu’
#   - 맥스풀링 레이어 : 풀 크기 2 x 2
#   - 플래튼 레이어
#   - 댄스 레이어 : 출력 뉴런 수 128개, 활성화 함수 ‘relu’
#   - 댄스 레이어 : 출력 뉴런 수 3개, 활성화 함수 ‘softmax’
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(200,200,3)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='softmax'))


''''''
#모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])