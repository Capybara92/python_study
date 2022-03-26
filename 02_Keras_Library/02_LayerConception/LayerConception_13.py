#순환 신경망 모델 만들어보기2

code2idx = {'c4':0, 'd4':1, 'e4':2, 'f4':3, 'g4':4, 'a4':5, 'b4':6,
            'c8':7, 'd8':8, 'e8':9, 'f8':10, 'g8':11, 'a8':12, 'b8':13}

idx2code = {0:'c4', 1:'d4', 2:'e4', 3:'f4', 4:'g4', 5:'a4', 6:'b4',
            7:'c8', 8:'d8', 9:'e8', 10:'f8', 11:'g8', 12:'a8', 13:'b8'}

import numpy as np

def seq2dataset(seq, window_size):
    dataset = []
    for i in range(len(seq)-window_size):
        subset = seq[i:(i+window_size+1)]
        dataset.append([code2idx[item] for item in subset])
    return np.array(dataset)

seq = ['g8', 'e8', 'e4', 'f8', 'd8', 'd4', 'c8', 'd8', 'e8', 'f8', 'g8', 'g8', 'g4',
       'g8', 'e8', 'e8', 'e8', 'f8', 'd8', 'd4', 'c8', 'e8', 'g8', 'g8', 'e8', 'e8', 'e4',
       'd8', 'd8', 'd8', 'd8', 'd8', 'e8', 'f4', 'e8', 'e8', 'e8', 'e8', 'e8', 'f8', 'g4',
       'g8', 'e8', 'e4', 'f8', 'd8', 'd4', 'c8', 'e8', 'g8', 'g8', 'e8', 'e8', 'e4'] #악보

dataset = seq2dataset(seq, window_size = 4)

print(dataset.shape)
print(dataset)

#예측과정
#예측은 두 가지 방법으로 해보겠다.
#한 스텝 예측과 곡 전체 예측이다.

#한 스텝 예측
#한 스텝 예측이란 실제 음표 4개를 입력하여 다음 음표 1개를 예측하는 것을 반복하는 것이다.
#이 방법에서는 모델의 입력값으로는 항상 실제 음표가 들어간다.
#   - 모델에 t0, t1, t2, t3를 입력하면 y0 출력이 나온다.
#   - 모델에 t1, t2, t3, t4를 입력하면 y1 출력이 나온다.
#   - 모델에 t2, t3, t4, t5를 입력하면 y2 출력이 나온다.
#   - 이 과정을 y49 출력까지 반복한다.

#곡 전체 예측
#곡 전체 예측이란 입력된 초가 4개 음표만을 입력으로 곡 전체를 예측하는 것이다.
#초반부가 지나면, 예측값만으로 모델에 입력되어 다음 예측값이 나오는 식이다.
#만약 중간에 틀린 부분이 생긴다면, 이후 음정, 박자는 모두 이상하게 될 가능성이 많다.
#예측 오류가 누적되는 것이다.
#   - 모델에 t0, t1, t2, t3를 입력하면 y0 출력이 나온다.
#   - 예측값인 y0를 t4라고 가정하고, 모델에 t1, t2, t3, t4(예측값)을 입력하면 y1 출력이 나온다.
#   - 예측값인 y1을 t5라고 가정하고, 모델에 t2, t3, t4(예측값), t5(예측값)을 입력하면 y2 출력이 나온다.
#   - 이 과정을 y49 출력까지 반복한다.


''''''
#다층 퍼셉트론 모델
#앞서 생성한 데이터셋으로 먼저 다층 퍼셉트론 모델을 학습시켜보겠다. 
#Dense 레이어 3개로 구성하였고, 입력 속성이 4개이고 출력이 12개(one_hot_vec_size=12)으로 설정했다.
model = Sequential()
model.add(Dense(128, input_dim=4, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(one_hot_vec_size, activation='softmax'))
