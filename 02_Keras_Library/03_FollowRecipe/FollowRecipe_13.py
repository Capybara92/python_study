#영상입력 수치예측 모델 레시피1

#영상을 입력해서 수치를 예측하는 모델들에 대해서 알아보겠다.
#간단한 테스트를 위해 수치예측을 위한 영상 데이터셋 생성을 해보고, 다층퍼셉트론 및 컨볼루션 신경망 모델을 구성 및 학습 시켜보겠다.
#이 모델은 고정된 지역에서 촬영된 영상으로부터 복잡도, 밀도 등을 수치화하는 문제를 풀 수 있다.
#아래 문제들에 활용 기대 해보자.
#   - CCTV 등 촬영 영상으로부터 미세먼지 지수 예측
#   - 위성영상으로부터 녹조, 적조 등의 지수 예측
#   - 태양광 패널의 먼지가 쌓여있는 정도 예측

#데이터셋 준비
#너비가 16, 높이가 16이고, 픽셀값을 0과 1을 가지는 영상을 만들어보겠다.
#임의의 값이 주어지면, 그 값만큼 반복하여 영상 내에 1인 픽셀을 찍었다.
#여기서 임의의 값이 라벨값으로 지정했다.
import numpy as np

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

#만든 데이터셋 일부를 가시화 해보겠다.
import matplotlib.pyplot as plt

x_train, y_train = generate_dataset(1500)

plt_row = 5
plt_col = 5

plt.rcParams["figure.figsize"] = (10,10)

f, axarr = plt.subplots(plt_row, plt_col)

for i in range(plt_row*plt_col):
    sub_plt = axarr[i//plt_row, i%plt_col]
    sub_plt.axis('off')
    sub_plt.imshow(x_train[i].reshape(width, height))
    sub_plt.set_title('R ' + str(y_train[i][0]))

plt.show()

#R(Real)은 1인 값을 가진 픽셀 수를 의미한다.
#한 번 표시한 픽셀에 다시 표시가 될 수 있기 때문에 실제 픽셀 수와 조금 차이는 날 수 있다.


''''''
#레이어 준비
#   - 2D Input data	: 2차원의 입력 데이터입이다. 주로 영상 데이터를 의미하며, 너비, 높이, 채널수로 구성된다.
#   - Conv2D        : 필터를 이용하여 영상 특징을 추출하는 컨볼루션 레이어이다.
#   - MaxPooling2D  : 영상에서 사소한 변화가 특징 추출에 크게 영향을 미치지 않도록 해주는 맥스풀링 레이어이다.
#   - Flatten       : 2차원의 특징맵을 전결합층으로 전달하기 위해서 1차원 형식으로 바꿔준다.
#   - relu          : 활성화 함수로 주로 Conv2D 은닉층에 사용된다.
