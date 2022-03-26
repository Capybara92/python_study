#컨볼루션 신경망 모델 만들어보기3

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

np.random.seed(3)

train_datagen = ImageDataGenerator(rescale=1./255)

'''
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
'''

train_generator = train_datagen.flow_from_directory(
        'handwriting_shape2/train',
        target_size=(24, 24),
        batch_size=3,
        class_mode='categorical')

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        'handwriting_shape2/test',
        target_size=(24, 24),    
        batch_size=3,
        class_mode='categorical')

model = Sequential()
'''
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(200,200,3)))
'''
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(24,24,3)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


''''''
#모델 학습시키기
#케라스에서는 모델을 학습시킬 때 주로 fit() 함수를 사용하지만 제네레이터로 생성된 배치로 학습시킬 경우에는 fit_generator() 함수를 사용한다.
#본 예제에서는 ImageDataGenerator라는 제네레이터로 이미지를 담고있는 배치로 학습시키기 때문에 fit_generator() 함수를 사용하겠다.
#   - 첫번째 인자       : 훈련데이터셋을 제공할 제네레이터를 지정한다. 앞서 생성한 train_generator으로 지정한다.
#   - steps_per_epoch  : 한 epoch에 사용한 스텝 수를 지정한다. 총 45개의 훈련 샘플이 있고 배치사이즈가 3이므로 15 스텝으로 지정한다.
#   - epochs           : 전체 훈련 데이터셋에 대해 학습 반복 횟수를 지정한다. 100번을 반복적으로 학습시켜 보겠다.
#   - validation_data  : 검증데이터셋을 제공할 제네레이터를 지정한다. 앞서 생성한 validation_generator으로 지정한다.
#   - validation_steps : 한 epoch 종료 시 마다 검증할 때 사용되는 검증 스텝 수를 지정한다. 총 15개의 검증 샘플이 있고 배치사이즈가 3이므로 5 스텝으로 지정한다.
model.fit_generator(
        train_generator,
        steps_per_epoch=15,
        epochs=50,
        validation_data=test_generator,
        validation_steps=5)


''''''
#모델 평가하기
#학습한 모델을 평가해본다. 제네레이터에서 제공되는 샘플로 평가할 때는 evaluate_generator 함수를 사용한다.
print("-- Evaluate --")
scores = model.evaluate_generator(test_generator, steps=5)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))


''''''
#모델 사용하기
#모델 사용 시에 제네레이터에서 제공되는 샘플을 입력할 때는 predict_generator 함수를 사용한다.
#예측 결과는 클래스별 확률 벡터로 출력되며, 클래스에 해당하는 열을 알기 위해서는 제네레이터의 ‘class_indices’를 출력하면 해당 열의 클래스명을 알려준다.
print("-- Predict --")
output = model.predict_generator(test_generator, steps=5)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
print(test_generator.class_indices)
print(output)


''''''
#이미지 분류 문제에 높은 성능을 보이고 있는 컨볼루션 신경망 모델을 이용하여 직접 만든 데이터셋으로 학습 및 평가를 해보았다.
#학습 결과는 좋게 나왔지만 이 모델은 한 사람이 그린 것에 대해서만 학습이 되어 있어 다른 사람에 그린 모양은 분류를 잘 하지 못한다.
#이를 해결하기 위한 방안으로 ‘데이터 부풀리기’ 기법이 있다.
