#문장(시계열수치)입력 다중클래스분류 모델 레시피1

#문장을 입력해서 다중클래스를 분류하는 모델에 대해서 알아보겠다.
#다중클래스 분류를 위한 데이터셋에 대해서 살펴보고 여러가지 다중클래스 분류 모델을 구성해보겠다.
#이 모델들은 문장 혹은 시계열수치로 타입을 분류하는 문제를 풀 수 있다.

#데이터셋 준비
#로이터에서 제공하는 뉴스와이어 데이터셋을 이용하겠다. 
#이 데이터셋은 총 11,228개의 샘플로 구성되어 있다. 
#라벨은 46개 주제로 지정되어 0에서 45의 값을 가지고 있다. 
#케라스에서 제공하는 reuters의 load_data() 함수을 이용하면 데이터셋을 쉽게 얻을 수 있다. 
#데이터셋은 이미 정수로 인코딩되어 있으며, 정수값은 단어의 빈도수를 나타낸다. 
#모든 단어를 고려할 수 없으므로 빈도수가 높은 단어를 위주로 데이터셋을 생성한다. 
#15,000번째로 많이 사용하는 단어까지만 데이터셋으로 만들고 싶다면, num_words 인자에 15000이라고 지정하면 된다.
from keras.datasets import reuters
(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=15000)

#훈련셋 8,982개와 시험셋 2,246개로 구성된 총 11,228개 샘플이 로딩이 된다. 
#훈련셋과 시험셋의 비율은 load_data() 함수의 test_split 인자로 조절 가능하다. 
#각 샘플은 뉴스 한 건을 의미하며, 단어의 인덱스로 구성되어 있다. 
#‘num_words=20000’으로 지정했기 때문에 빈도수가 15,000을 넘는 단어는 로딩되지 않는다. 
#훈련셋 8,982개 중 다시 7,000개을 훈련셋으로 나머지를 검증셋으로 분리한다.
x_val = x_train[7000:]
y_val = y_train[7000:]
x_train = x_train[:7000]
y_train = y_train[:7000]

#각 샘플의 길이가 달라서 모델의 입력으로 사용하기 위해 케라스에서 제공되는 전처리 함수인 sequence의 pad_sequences() 함수를 사용한다.
#이 함수는 두 가지 역할을 수행한다.
#   - 문장의 길이를 maxlen 인자로 맞춰준다. 
#     예를 들어 120으로 지정했다면 120보다 짧은 문장은 0으로 채워서 120단어로 맞춰주고 120보다 긴 문장은 120단어까지만 잘라낸다.
#   - (num_samples, num_timesteps)으로 2차원의 numpy 배열로 만들어준다.
#     maxlen을 120으로 지정하였다면, num_timesteps도 120이 된다.
from keras.preprocessing import sequence

x_train = sequence.pad_sequences(x_train, maxlen=120)
x_val = sequence.pad_sequences(x_val, maxlen=120)
x_test = sequence.pad_sequences(x_test, maxlen=120)
