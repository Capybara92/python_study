#운동화나 셔츠같은 옷 이미지를 분류하는 신경망 모델을 훈련3
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'), 
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\n테스트 정확도:', test_acc)

''''''
#분류 예측 만들기
#모델이 성공적으로 만들어졌다면, 이제 실제 각각의 데이터를 호출하여 분류를 어떻게 하고 있는지 확인한다.
predictions = model.predict(test_images)
print(predictions[0])
#이 예측은 10개의 숫자 배열로 나타낸다.
#이 값은 10개의 옷 품목에 상응하는 모델의 신뢰도(confidence)를 나타낸다.
# 
#가장 높은 신뢰도를 가진 레이블을 찾기.
print(np.argmax(predictions[0]))

#모델은 이 이미지가 앵클부츠(class_name[9])라고 가장 확신하고 있습니다.
#이 값이 맞는지 테스트 레이블을 확인.
print(test_labels[0])

#10개 클래스에 대한 예측을 모두 그래프로 표현
def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.get_cmap('binary'))

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

#0번째 원소의 이미지, 예측, 신뢰도 점수 배열을 확인.
i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()

#몇 개의 이미지의 예측을 출력.
#올바르게 예측된 레이블은 파란색이고 잘못 예측된 레이블은 빨강색이다.
#숫자는 예측 레이블의 신뢰도 퍼센트(100점 만점)이다.
#신뢰도 점수가 높을 때도 잘못 예측할 수 있다.
#   처음 X 개의 테스트 이미지와 예측 레이블, 진짜 레이블을 출력한다.
#   올바른 예측은 파랑색으로 잘못된 예측은 빨강색으로 나타낸다.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()

#결과를 출력하여 확인하는 방법
#for i in range(0, 100):
#    print(class_names[test_labels[i]], '=>', class_names[np.argmax(predictions[i])])

''''''
#마지막으로 훈련된 모델을 사용하여 한 이미지에 대한 예측을 만든다.
#   테스트 세트에서 이미지 하나를 선택한다.
img = test_images[0]
print(img.shape)

#tf.keras 모델은 한 번에 샘플의 묶음 또는 배치(batch)로 예측을 만드는데 최적화되어 있다.
#하나의 이미지를 사용할 때에도 2차원 배열로 만들어야 한다.
#   이미지 하나만 사용할 때도 배치에 추가한다.
img = (np.expand_dims(img,0))
print(img.shape)

#이제 이 이미지의 예측을 만든다.
predictions_single = model.predict(img)
print(predictions_single)

plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)

#model.predict는 2차원 넘파이 배열을 반환하므로 첫 번째 이미지의 예측을 선택한다.
print(np.argmax(predictions_single[0]))
#이전과 마찬가지로 모델의 예측은 레이블 9이다.
