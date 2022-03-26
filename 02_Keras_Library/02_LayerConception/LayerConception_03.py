#다층 퍼셉트론 만들어보기3

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(5)

dataset = np.loadtxt("./warehouse/pima-indians-diabetes.data", delimiter=",")

x_train = dataset[:700,0:8]
y_train = dataset[:700,8]
x_test = dataset[700:,0:8]
y_test = dataset[700:,8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#모델 학습시키기
#모델을 학습시키기 위해서 fit() 함수를 사용한다.
#   - 첫번째 인자 : 입력 변수입니다. 8개의 속성 값을 담고 있는 X를 입력합니다.
#   - 두번째 인자 : 출력 변수 즉 라벨값입니다. 결과 값을 담고 았는 Y를 입력합니다.
#   - epochs     : 전체 훈련 데이터셋에 대해 학습 반복 횟수를 지정합니다. 1500번을 반복적으로 학습시켜 보겠습니다.
#   - batch_size : 가중치를 업데이트할 배치 크기를 의미하며, 64개로 지정했습니다.
model.fit(x_train, y_train, epochs=1500, batch_size=64)

#아래 model.fit의 파라미터가 더 존재한다.
#   - verbose               :
#   - callbacks             :
#   - validation_split      :
#   - validation_data       :
#   - shuffle               :
#   - class_weight          :
#   - sample_weight         :
#   - initial_epoch         :
#   - steps_per_epoch       :
#   - validation_steps      :
#   - validation_batch_size :
#   - validation_freq       :
#   - max_queue_size        :
#   - workers               :
#   - use_multiprocessing   :


''''''
#모델 평가하기
#시험셋으로 학습한 모델을 평가한다.
scores = model.evaluate(x_test, y_test)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

'''
다층 퍼셉트론 모델을 만들어보고 실제 데이터셋을 사용하여 학습시켜보았다.
수치로 된 데이터를 불러오는 법과 모델에 학습시키기 위해서 간단히 가공을 해봤다.
또한 이진 분류 문제를 적용하기 위해서 입력 레이어와 출력 레이어를 어떻게 구성해야 하는 지도 알아봤다.

임신 횟수나 나이, 혈압 등은 구두로 물어보거나 측정기로 간단하게 측정할 수 있기 때문에 비용이 얼마 들지 않지만, 
포도당 내성 검사나 혈청 인슐린 수치 등 혈액 검사가 필요한 것은 비용도 발생하고 테스트 결과도 즉시 알 수 없다.
실제로도 딥러닝을 실무에 적용하려다 보면 데이터 수집 및 판정 결과를 얻기가 쉽지않고 비용산정도 어려울 때가 많다.
기간, 비용등을 고려하여 계획을 세워야 효율적으로 데이터를 원할하게 수집할 수가 있다.
'''
