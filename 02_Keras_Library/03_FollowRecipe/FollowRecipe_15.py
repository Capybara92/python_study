#영상입력 수치예측 모델 레시피3

#컨볼루션 신경망 모델
#model = Sequential()
#model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(width, height, 1)))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Conv2D(32, (3, 3), activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Flatten())
#model.add(Dense(256, activation='relu'))
#model.add(Dense(1))

# 0. 사용할 패키지 불러오기
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

width = 16
height = 16

def generate_dataset(samples):

    ds_x = []
    ds_y = []
    
    for it in range(samples):
        
        num_pt = np.random.randint(0, width * height)
        img = generate_image(num_pt)
        
        ds_y.append(num_pt)
        ds_x.append(img)
    
    return np.array(ds_x), np.array(ds_y).reshape(samples, 1)
    
def generate_image(points):
    
    img = np.zeros((width, height))
    pts = np.random.random((points, 2))
    
    for ipt in pts:
        img[int(ipt[0] * width), int(ipt[1] * height)] = 1
    
    return img.reshape(width, height, 1)

# 1. 데이터셋 생성하기
x_train, y_train = generate_dataset(1500)
x_val, y_val = generate_dataset(300)
x_test, y_test = generate_dataset(100)

# 2. 모델 구성하기
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(width, height, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(1))

# 3. 모델 학습과정 설정하기
model.compile(loss='mse', optimizer='adam')

# 4. 모델 학습시키기
hist = model.fit(x_train, y_train, batch_size=32, epochs=1000, validation_data=(x_val, y_val))

# 5. 학습과정 살펴보기
import matplotlib.pyplot as plt

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.ylim(0.0, 300.0)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

# 6. 모델 평가하기
score = model.evaluate(x_test, y_test, batch_size=32)

print(score)

# 7. 모델 사용하기
yhat_test = model.predict(x_test, batch_size=32)

import matplotlib.pyplot as plt

plt_row = 5
plt_col = 5

plt.rcParams["figure.figsize"] = (10,10)

f, axarr = plt.subplots(plt_row, plt_col)

for i in range(plt_row*plt_col):
    sub_plt = axarr[i//plt_row, i%plt_col]
    sub_plt.axis('off')
    sub_plt.imshow(x_test[i].reshape(width, height))
    sub_plt.set_title('R %d P %.1f' % (y_test[i][0], yhat_test[i][0]))

plt.show()


'''
학습결과 비교
다층퍼셉트론 신경망 모델와 컨볼루션 신경망 모델을 비교했을 때, 현재 파라미터로는 다층퍼셉트론 신경망 모델의 정확도가 더 높았다.
라벨값이 픽셀 간의 관계가 있거나 모양 및 색상이 다양하지 않고 단순히 1인 픽셀 개수와 관련이 있기 때문에 컨볼루션 신경망 모델이 크케 성능을 발휘하지 못했다.

요약
영상를 입력하여 수치예측을 할 수 있는 깊은 다층퍼셉트론 신경망 모델, 컨볼루션 신경망 모델을 살펴보고 그 성능을 확인 해봤다.
영상 입력이라고 해서 컨볼루션 신경망 모델이 항상 좋은 성능이 나오는 것이 아니라는 것도 알게되었다.
어떤 모델이 성능이 좋게 나올지는 테스트를 해봐야 겠지만, 워낙 모델을 다양하게 구성할 수 있고 여러 파라미터를 설정할 수 있으므로, 
모델을 개발하기 전 데이터 특징을 분석하고 적절한 후보 모델들을 선정하는 것을 권장한다.
'''
