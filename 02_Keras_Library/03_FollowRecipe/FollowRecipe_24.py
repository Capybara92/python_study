#시계열수치입력 수치예측 모델 레시피1

#시계열 수치를 입력해서 다음 수치를 예측하는 모델들에 대해서 알아보겠다.
#각 모델에 코사인(cosine) 데이터를 학습시킨 후, 처음 일부 데이터를 알려주면 이후 코사인 형태의 데이터 예측을 얼마나 잘 하는 지 테스트 하겠다.

#시계열 :
#   일반적으로 어떤 양의 관측결과를 일정한 기준에 따라 계열로 정리한 것을 통계계열이라고 한다.
#   어떤 관측치(觀測値) 또는 통계량의 변화를 시간의 움직임에 따라서 포착하고 이것을 계열화하였을 때, 이와 같은 통계계열을 시계열이라고 한다.
#   이러한 경우의 관측결과 x는 시간 t에 따라서 변동하는 양이므로 그 시계열은 {xt}로 표시된다. 
#   예를 들면, 한 나라의 경제성장을 알기 위한 실질국민 총생산지수에 관한 통계도표는 연도를 시간이라고 생각하였을 때의 시계열의 도표이다.

#데이터셋 준비
#먼저 코사인 데이터를 만들어보겠다.
#시간의 흐름에 따라 진폭이 -1.0에서 1.0사이로 변하는 1,600개의 실수값을 생성한다.
import numpy as np

signal_data = np.cos(np.arange(1600)*(20*np.pi/1000))[:,None]

#생성한 데이터를 확인
import matplotlib.pyplot as plt

plot_x = np.arange(1600)
plot_y = signal_data
plt.plot(plot_x, plot_y)
plt.show()

#생성한 코사인 데이터를 모델에 학습시키기 위해서는 데이터와 라벨로 구성된 데이터셋으로 만들어야 한다. 
#이전 수치들을 입력하여 다음 수치를 예측하는 문제이므로 데이터는 이전 수치들이 되고, 라벨은 다음 수치가 된다. 
#다른 예제들과는 달리 데이터와 라벨이 모두 같은 속성이다. 
#아래 create_dataset()함수는 시계열 수치를 입력받아 데이터셋을 생성한다.
#이 때 look_back 인자는 얼마만큼의 이전 수치를 데이터로 만들것인가를 결정한다.
def create_dataset(signal_data, look_back=1):
    dataX, dataY = [], []
    for i in range(len(signal_data)-look_back):
        dataX.append(signal_data[i:(i+look_back), 0])
        dataY.append(signal_data[i + look_back, 0])
    return np.array(dataX), np.array(dataY)

#-1.0에서 1.0까지의 값을 가지는 코사인 데이터를 0.0과 1.0 사이의 값을 가지도록 정규화를 한 뒤 훈련셋과 시험셋으로 분리한다. 
#이전 40개의 수치를 입력하여 다음 수치 1개를 예측하는 데이터셋을 만들기 위해 look_back 인자를 40으로 설정하였다.
#look_back 인자에 따라 모델의 성능이 달라지므로 적정 값을 지정하는 것이 중요하다.
from sklearn.preprocessing import MinMaxScaler

look_back = 40

# 데이터 전처리
scaler = MinMaxScaler(feature_range=(0, 1))
signal_data = scaler.fit_transform(signal_data)

# 데이터 분리
train = signal_data[0:800]
val = signal_data[800:1200]
test = signal_data[1200:]

# 데이터셋 생성
x_train, y_train = create_dataset(train, look_back)
x_val, y_val = create_dataset(val, look_back)
x_test, y_test = create_dataset(test, look_back)

#레이어 준비
#LSTM : Long-Short Term Memory unit의 약자로 순환 신경망 레이어 중 하나이다.
#tanh : LSTM의 출력 활성화 함수로 사용된다.
