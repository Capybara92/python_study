import tensorflow as tf

#MNIST 데이터셋을 로드하여 준비한다.
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data() 
'''어떤거는 npz파일로 로드되고, 어떤거는 gz압축파일로 로드되는데 차이점이 무엇인가?????????????'''

#샘플 값을 정수에서 부동소수로 변환한다.
x_train, x_test = x_train / 255.0, x_test / 255.0


#층을 차례대로 쌓아 tf.keras.Sequential모델을 만든다. 
#훈련에 사용할 옵티마이저(optimizer)와 손실함수를 선택한다.
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


#모델을 훈련하고 평가한다.
model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)
