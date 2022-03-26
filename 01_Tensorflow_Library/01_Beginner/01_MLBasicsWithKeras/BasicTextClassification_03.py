#영화리뷰 텍스트를 긍정 또는 부정으로 분류4.

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

word_index = imdb.get_word_index()

word_index = {k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                        value=word_index["<PAD>"],
                                                        padding='post',
                                                        maxlen=256)

test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                       value=word_index["<PAD>"],
                                                       padding='post',
                                                       maxlen=256)

vocab_size = 10000

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16, input_shape=(None,)))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

x_val = train_data[:10000]
partial_x_train = train_data[10000:]

y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=40,
                    batch_size=512,
                    validation_data=(x_val, y_val),
                    verbose=1)

results = model.evaluate(test_data,  test_labels, verbose=2)
print(results)

''''''
#정확도와 손실 그래프 그리기
#model.fit()은 History 객체를 반환한다.
#여기에는 훈련하는 동안 일어난 모든 정보가 담긴 딕셔너리(dictionary)가 들어 있다.
history_dict = history.history
print(history_dict.keys())
#네 개의 항목이 있다.
#훈련과 검증단계에서 모니터링하는 지표들이다.
#훈련손실과 검증손실을 그래프로 그려보고, 훈련정확도와 검증정확도도 그래프로 그려서 비교해 보자.

acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

# "bo"는 "파란색 점"이다.
plt.plot(epochs, loss, 'bo', label='Training loss')
# b는 "파란 실선"이다.
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

plt.clf()   # 그림을 초기화.

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

#그래프에서 점선은 훈련손실과 훈련정확도를 나타낸다. 실선은 검증손실과 검증정확도이다.

#훈련손실은 에포크마다 감소하고 훈련정확도는 증가한다는 것을 주목하자.
#경사하강법 최적화를 사용할 때 볼 수 있는 현상이다.
#매 반복마다 최적화 대상의 값을 최소화한다.

#하지만 검증손실과 검증정확도에서는 그렇지 못한다.
#약 20번째 에포크 이후가 최적점인 것 같다. 이는 과대적합 때문이다.
#이전에 본 적 없는 데이터보다 훈련 데이터에서 더 잘 동작힌다.
#이 지점부터는 모델이 과도하게 최적화되어 테스트 데이터에서 일반화되기 어려운 훈련데이터의 특정표현을 학습한다.

#여기에서는 과대적합을 막기위해 단순히 20번째 에포크 근처에서 훈련을 멈출 수 있다.
#나중에 콜백(callback)을 사용하여 자동으로 이렇게 하는 방법을 배워 보겠다.
