#순환 신경망 모델 만들어보기8

#입력 속성이 여러 개인 모델 구성
#입력 속성이 여러 개인 경우에 대해서 알아보자.
#예를 들어 ‘기온’라는 것을 예측하기 위해서 입력으로 ‘기온’뿐만아니라 ‘습도’, ‘기압’, ‘풍향’, ‘풍속’ 등 다양한 속성이 있을 수 있다.
#상태유지 LSTM 모델에서 입력형태를 batch_input_shape=(배치사이즈, 타임스텝, 속성)으로 설정하는데, 마지막 인자를 통해 속성의 개수를 지정할 수 있다.
#‘나비야’ 예제에서는 현재 입력값이 ‘c4, e4, g8’등으로 되어 있는 데, 이를 음정과 음길이로 나누어서 2개의 속성으로 입력해보겠다.
#즉 ‘c4’는 ‘(c, 4)’로 나누어서 입력하게 되는 것이다.
#이를 위해 데이터셋 만드는 함수를 아래와 같이 수정하였다.
def code2features(code):
    features = []
    features.append(code2scale[code[0]]/float(max_scale_value))
    features.append(code2length[code[1]])
    return features

#LSTM 모델 생성 시 batch_input_shape 인자의 마지막 값을 ‘1’에서 ‘2’로 수정한다.
model = Sequential()
model.add(LSTM(128, batch_input_shape = (1, 4, 2), stateful=True))
model.add(Dense(one_hot_vec_size, activation='softmax'))

#방식은 ‘c8’이니 ‘d4’처럼 코드 자체를 학습하는 것이 아니라 음정과 음길이를 나누어서 학습하는 효과를 볼 수 있다.
#사람이 악보를 읽을 때도 이 둘은 나누어서 인지를 하니 좀 더 사람에 가까운 학습이라고 보실 수 있다.
