#문장(시계열수치)입력 이진분류 모델 레시피5

#순환 컨볼루션 신경망 모델
#컨볼루션 레이어에서 나온 특징벡터들을 맥스풀링(MaxPooling1D)를 통해 1/4로 줄여준 다음 LSTM의 입력으로 넣어주는 모델이다. 
#이때 맥스풀링은 특징벡터 크기를 줄여주는 것이 아니라 특징벡터 수를 줄여준다. 
#즉 200개 단어가 컨볼루션 레이어를 통과하면 256 크기를 갖는 특징벡터가 198개가 생성되고, 맥스풀링은 특징벡터 198개 중 49개를 골라준다. 
#따라서 LSTM 레이어의 timesteps는 49개가 된다. 
#참고로 input_dim은 그대로 256이다.

#순환 신경망 모델과 순환 컨볼루션 신경망 모델 구성에서 LSTM의 입력 비교하면 다음과 같습니다
#   -순환 신경망 모델         : LSTM에 입력되는 타임스텝은 Embedding 출력 타임스텝으로 200이고, 특징 크기는 Embedding에서 인코딩된 128이다.
#   -순환 컨볼루션 신경망 모델 : LSTM에 입력되는 타임스텝은 49, 속성은 256이다. 
#                              타임스텝이 49인 이유는 Conv1D에서 200단어를 받아 198개를 반환하고, 이를 다시 MaxPooling1D에 의해 1/4배로 줄어들어 49가 된 것이다. 
#                              속성이 256인 이유는 Conv1D가 Embedding 출력인 128 벡터를 입력받아 256으로 반환되기 때문이다.

# 0. 사용할 패키지 불러오기
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.layers import Flatten, Dropout
from keras.layers import Conv1D, MaxPooling1D

max_features = 20000
text_max_words = 200

# 1. 데이터셋 생성하기

# 훈련셋과 시험셋 불러오기
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

# 훈련셋과 검증셋 분리
x_val = x_train[20000:]
y_val = y_train[20000:]
x_train = x_train[:20000]
y_train = y_train[:20000]

# 데이터셋 전처리 : 문장 길이 맞추기
x_train = sequence.pad_sequences(x_train, maxlen=text_max_words)
x_val = sequence.pad_sequences(x_val, maxlen=text_max_words)
x_test = sequence.pad_sequences(x_test, maxlen=text_max_words)

# 2. 모델 구성하기
model = Sequential()
model.add(Embedding(max_features, 128, input_length=text_max_words))
model.add(Dropout(0.2))
model.add(Conv1D(256,
                 3,
                 padding='valid',
                 activation='relu',
                 strides=1))
model.add(MaxPooling1D(pool_size=4))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

# 3. 모델 학습과정 설정하기
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4. 모델 학습시키기
hist = model.fit(x_train, y_train, epochs=2, batch_size=64, validation_data=(x_val, y_val))

# 5. 학습과정 살펴보기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')
loss_ax.set_ylim([-0.2, 1.2])

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')
acc_ax.set_ylim([-0.2, 1.2])

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# 6. 모델 평가하기
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=64)
print('## evaluation loss and_metrics ##')
print(loss_and_metrics)

'''
학습결과 비교
단순한 다층퍼셉트론 신경망 모델보다는 순환 레이어나 컨볼루션 레이어를 이용한 모델의 성능이 더 높았습니다.

요약
문장을 입력하여 이진분류할 수 있는 여러가지 모델을 살펴보고, 그 성능을 비교해봤습니다. 
시계열 데이터를 처리하기 위한 모델은 다층퍼셉트론 신경망 모델부터 컨볼루션 신경망, 순환 신경망 모델 등 다양하게 구성할 수 있습니다. 
복잡한 모델일수록 정확도가 높은 것은 아니지만 여러 모델과 파라미터로 적절한 모델을 개발해야 합니다.
'''
