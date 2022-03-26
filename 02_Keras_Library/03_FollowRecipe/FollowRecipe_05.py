#수치입력 이진분류 모델 레시피1

#수치를 입력해서 이진분류할 수 있는 모델들에 대해서 알아보자.
#이진분류를 위한 데이터셋 생성을 해보고, 가장 간단한 퍼셉트론 모델부터 깊은 다층퍼셉트론 모델까지 구성 및 학습을 시켜보겠다.

#데이터셋 준비
#훈련에 사용할 임의의 값을 가진 인자 12개로 구성된 입력(x) 1000개와 각 입력에 대해 0과 1 중 임의로 지정된 출력(y)를 가지는 데이터셋을 생성한다.
#시험에 사용할 데이터는 100개를 준비한다.
import numpy as np

# 데이터셋 생성
x_train = np.random.random((1000, 12))
y_train = np.random.randint(2, size=(1000, 1))
x_test = np.random.random((100, 12))
y_test = np.random.randint(2, size=(100, 1))

#데이터셋의 12개 인자(x) 및 라벨값(y) 모두 무작위 수 이다. 
#패턴이 없는 데이터이고, 학습하기에 가장 어려운 케이스라 볼 수 있다.
#물론 패턴이 없기 때문에 이런 데이터로 학습한 모델은 시험셋에서 정확도가 상당히 낮다.
#하지만 이러한 무작위 데이터를 사용하는 이유는 다음과 같다.
#   - 패턴이 없는 데이터에서 각 모델들이 얼마나 빨리 학습되는 지 살펴볼 수 있다.
#   - 실제 데이터를 사용하기 전에 데이터셋 형태를 설계하거나 모델 프로토타입핑 하기에 적절하다.

#12개 입력인자 중 첫번째와 두번째 인자 값만 이용하여 2차원으로 데이터 분포를 살펴보겠다.
#라벨값에 따라 점의 색상을 다르게 표시했다.
import matplotlib.pyplot as plt

# 데이터셋 확인 (2차원)
plot_x = x_train[:,0]
plot_y = x_train[:,1]
plot_color = y_train.reshape(1000,)

plt.scatter(plot_x, plot_y, c=plot_color)
plt.show()

#실제 데이터에서는 첫번째 인자와 두번째 인자사이의 상관관계가 있다면 그래프에서 패턴을 볼 수 있다.
#우리는 임의의 값으로 데이터셋을 만들었으므로 예상대로 패턴을 찾을 수 없다.
#이번에는 첫번째, 두번째, 세번째의 인자값을 이용하여 3차원으로 그래프를 확인해보겠다.
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot_x = x_train[:,0]
plot_y = x_train[:,1]
plot_z = x_train[:,2]
plot_color = y_train.reshape(1000,)

ax.scatter(plot_x, plot_y, plot_z, c=plot_color)
plt.show()

#역시나 패턴을 찾아볼 수는 없다.
#하지만 실제 데이터에서는 인자 간의 상관관계가 있을 경우 패턴을 확인할 수 있므으로 이와 같은 방식으로 모델을 설계하기 전에 데이터셋을 먼저 확인해보는 것은 권장한다. 
#단, 훈련데이터셋에 과적합 되는것을 가정하고 있으므로 시험셋의 정확도는 무시해도 된다.


''''''
#레이어 준비
#sigmoid : 활성화 함수로 입력되는 값을 0과 1사이의 값으로 출력시킨다.
#          출력값이 특정 임계값(예를 들어 0.5) 이상이면 양성, 이하이면 음성이라고 판별할 수 있기 때문에 이진분류 모델의 출력층에 주로 사용된다.