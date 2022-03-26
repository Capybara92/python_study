#영상입력 다중클래스분류 모델 레시피1

#영상을 입력해서 다중클래스를 분류할 수 있는 모델들에 대해서 알아보겠다.
#숫자 손글씨 데이터셋인 MNIST을 이용하여 다층퍼셉트론 및 컨볼루션 신경망 모델을 구성하고 학습 시켜보겠다.
#이 모델들은 아래 문제들에 활용해 본다.
#   - 동양인 얼굴 사진으로 한국인, 일본인, 중국인 구분
#   - 현미경 촬영 영상으로부터 다양한 균 구분
#   - 스마트폰으로 찍은 식물 종류 구분
#   - 기상위성영상으로부터 태풍 타입 분류

#데이터셋 준비
#케라스 함수에서 제공하는 숫자 손글씨 데이터셋인 MNIST을 이용하겠다. 
#초기 라벨값은 0에서 9까지 정수로 지정되어 있다.
#데이터 정규화를 위해서 255.0으로 나누었다. 
#아래는 다층퍼셉트론 신경망 모델에 입력하기 위해 데이터셋 생성하는 코드이다.
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, width*height).astype('float32') / 255.0
x_test = x_test.reshape(10000, width*height).astype('float32') / 255.0

#아래는 컨볼루션 신경망 모델에 입력하기 위해 데이터셋 생성하는 코드이다.
#샘플수, 너비, 높이, 채널수로 총 4차원 배열로 구성한다.
x_train = x_train.reshape(60000, width, height, 1).astype('float32') / 255.0
x_test = x_test.reshape(10000, width, height, 1).astype('float32') / 255.0

#불러온 훈련셋을 다시 훈련셋 50,000개와 검증셋 10,000개로 나눈다.
x_val = x_train[50000:]
y_val = y_train[50000:]
x_train = x_train[:50000]
y_train = y_train[:50000]

#다중클래스분류 모델의 출력과 맞추기 위해서 0에서 9까지의 값이 저장된 라벨에 ‘one-hot 인코딩’ 처리를 수행한다.
y_train = np_utils.to_categorical(y_train)
y_val = np_utils.to_categorical(y_val)
y_test = np_utils.to_categorical(y_test)
