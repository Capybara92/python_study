#영화리뷰 텍스트를 긍정 또는 부정으로 분류2.

import tensorflow as tf
from tensorflow import keras
import numpy as np

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

''''''
#데이터 준비
#리뷰(정수 배열)는 신경망에 주입하기 전에 텐서로 변환되어야 한다.
#변환하는 방법에는 몇 가지가 있다.
#   1. 원-핫 인코딩(one-hot encoding)은 정수배열을 0과 1로 이루어진 벡터로 변환한다.
#      예를 들어 배열 [3, 5]을 인덱스 3과 5만 1이고 나머지는 모두 0인 10,000차원 벡터로 변환할 수 있다.
#      그다음 실수 벡터 데이터를 다룰 수 있는 층(Dense)을 신경망의 첫 번째 층으로 사용한다.
#      이 방법은 num_words * num_reviews 크기의 행렬이 필요하기 때문에 메모리를 많이 사용힌다.
#   2. 다른 방법으로는, 정수 배열의 길이가 모두 같도록 패딩(padding)을 추가해 max_length * num_reviews 크기의 정수 텐서를 만든다.
#      이런 형태의 텐서를 다룰 수 있는 임베딩(embedding)층을 신경망의 첫 번째 층으로 사용할 수 있다.
#이 튜토리얼에서는 두 번째 방식을 사용한다.

#영화 리뷰의 길이가 같아야 하므로 pad_sequences함수를 사용해 길이를 맞춘다.
train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                        value=word_index["<PAD>"],
                                                        padding='post',
                                                        maxlen=256)

test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                       value=word_index["<PAD>"],
                                                       padding='post',
                                                       maxlen=256)

#샘플의 길이를 확인
print(len(train_data[0]), len(train_data[1]))

#(패딩된) 첫 번째 리뷰 내용을 확인
print(train_data[0])

''''''
#모델 구성
#신경망은 층(layer)을 쌓아서 만든다.
#이 구조에서는 두 가지를 결정해야 한다.
#   1. 모델에서 얼마나 많은 층을 사용할 것인가?
#   2. 각 층에서 얼마나 많은 은닉 유닛(hidden unit)을 사용할 것인가?

#이 예제의 입력 데이터는 단어 인덱스의 배열이다.
#예측할 레이블은 0 또는 1이다.
#이 문제에 맞는 모델을 구성해 보자.
#   입력크기는 영화리뷰 데이터셋에 적용된 어휘 사전의 크기이다. (10,000개의 단어)
vocab_size = 10000

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16, input_shape=(None,)))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()

#층을 순서대로 쌓아 분류기(classifier)를 만든다.
#   1. 첫 번째 층은 Embedding 층이다.
#      이 층은 정수로 인코딩된 단어를 입력받고 각 단어 인덱스에 해당하는 임베딩 벡터를 찾는다.
#      이 벡터는 모델이 훈련되면서 학습된다.
#      이 벡터는 출력 배열에 새로운 차원으로 추가된다.
#      최종차원은 (batch, sequence, embedding)이 된다.
#   2. 그다음 GlobalAveragePooling1D 층은 sequence 차원에 대해 평균을 계산하여 각 샘플에 대해 고정된 길이의 출력 벡터를 반환한다.
#      이는 길이가 다른입력을 다루는 가장 간단한 방법이다.
#   3. 이 고정길이의 출력벡터는 16개의 은닉유닛을 가진 완전연결(fully-connected) 층(Dense)을 거친다.
#   4. 마지막 층은 하나의 출력노드(node)를 가진 완전연결 층이다.
#      sigmoid 활성화함수를 사용하여 0과 1사이의 실수를 출력한다. 
#      이 값은 확률 또는 신뢰도를 나타낸다.

''''''
#은닉유닛
#위 모델에는 입력과 출력사이에 두 개의 중간 또는 "은닉" 층이 있다. 
#출력(유닛, 노드, 뉴런)의 개수는 층이 가진 표현공간(representational space)의 차원이 된다.
#다른말로 하면, 내부표현을 학습할 때 허용되는 네트워크 자유도의 양이다.

#모델에 많은 은닉유닛(고차원의 표현 공간)과 층이 있다면 네트워크는 더 복잡한 표현을 학습할 수 있다.
#하지만 네트워크의 계산비용이 많이 들고 원치않는 패턴을 학습할 수도 있다.
#이런 표현은 훈련데이터의 성능을 향상시키지만 테스트 데이터에서는 그렇지 못한다.
#이를 과대적합(overfitting)이라고 부른다.
