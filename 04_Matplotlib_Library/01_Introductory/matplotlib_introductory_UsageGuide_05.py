#성능(performance)
#데이터를 탐색하든 프로그래밍 방식으로 많은 플롯을 저장하든 관계없이 렌더링 성능은 파이프 라인에서 고통스러운 병목 현상이 될 수 있습니다. 
#Matplotlib는 플롯의 모양에 약간의 변경(설정 가능한 허용 오차)을 사용하여 렌더링 시간을 크게 줄일 수있는 몇 가지 방법을 제공합니다.
#렌더링 시간을 줄이는 데 사용할 수있는 방법은 작성중인 플롯 유형에 따라 다릅니다.

#랜더링(rendering)이란?
#2차원의 화상에 광원·위치·색상 등 외부의 정보를 고려하여 사실감을 불어넣어, 3차원 화상을 만드는 과정을 뜻하는 컴퓨터그래픽스 용어이다.

#선분 단순화(Line segment simplification)
#matplotlibrc파일 에서 정의 할 수 있습니다

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True #선분이있는 플롯 (예 : 일반적인 선 플롯, 다각형 윤곽선 등)의 경우 렌더링 성능을 제어.
                                     #선 세그먼트가 전혀 단순화되었는지 여부를 나타내는 부울.

'''
mpl.rcParams['path.simplify_threshold'] = 0.0 #라인 세그먼트가 단순화되는 정도를 제어합니다. 임계 값이 높을수록 렌더링 속도가 빨라진다.
plt.plot(y)
plt.show()
'''

mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()


#단순화는 벡터에 대한 다음 선분의 수직 거리(디스플레이 좌표 공간에서 측정 됨)가 path.simplify_threshold매개 변수 보다 클 때까지 선분을 단일 벡터로 반복적으로 병합하여 작동.
#라인 세그먼트가 단순화되는 방식과 관련된 변경 사항은 버전 2.1에서 이루어졌습니다.
