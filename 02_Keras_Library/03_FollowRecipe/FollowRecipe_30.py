#문장(시계열수치)입력 이진분류 모델 레시피2

#모델 준비
#   - 다층퍼셉트론 신경망 모델
#   - 순환 신경망 모델
#   - 컨볼루션 신경망 모델
#   - 순환 컨볼루션 신경망 모델

#다층퍼셉트론 신경망 모델
#먼저 임베딩(Embedding) 레이어에 대해서 알아보겠다.
#임베딩(Embedding) 레이어의 인자 의미는 다음과 같다.
#   - 첫번째 인자(input_dim)  : 단어 사전의 크기를 말하며 총 20,000개의 단어 종류가 있다는 의미이다. 
#                              이 값은 앞서 imdb.load_data() 함수의 num_words 인자값과 동일해야 한다.
#   - 두번째 인자(output_dim) : 단어를 인코딩 한 후 나오는 벡터크기 이다. 
#                              이 값이 128이라면 단어를 128차원의 의미론적 기하공간에 나타낸다는 의미이다. 
#                              단순하게 빈도수만으로 단어를 표시한다면, 10과 11은 빈도수는 비슷하지만 단어로 볼 때는 전혀 다른 의미를 가지고 있다. 
#                              하지만 의미론적 기하공간에서는 거리가 가까운 두 단어는 의미도 유사하다. 
#                              즉 임베딩 레이어는 입력되는 단어를 의미론적으로 잘 설계된 공간에 위치시켜 벡터로 수치화 시킨다고 볼 수 있다.
#   - input_length           : 단어의 수 즉 문장의 길이를 나타낸다.
#                              임베딩 레이어의 출력 크기는 (샘플 수) * (output_dim) * (input_lenth)가 된다. 
#                              임베딩 레이어 다음에 Flatten 레이어가 온다면 반드시 input_lenth를 지정해야 한다.
#                              플래튼 레이어인 경우 입력 크기가 알아야 이를 1차원으로 만들어서 Dense 레이어에 전달할 수 있기 때문이다.

#아래는 임베딩 레이어로 인코딩한 후 Dense 레이어를 통해 분류하는 다층퍼셉트론 신경망 모델이다.
#model = Sequential()
#model.add(Embedding(20000, 128, input_length=200))
#model.add(Flatten())
#model.add(Dense(256, activation='relu'))
#model.add(Dense(1, activation='sigmoid'))

# 0. 사용할 패키지 불러오기
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import Flatten

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
model.add(Flatten())
model.add(Dense(256, activation='relu'))
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
