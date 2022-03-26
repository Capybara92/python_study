#마커 단순화(Marker simplification)
#마커는 라인 세그먼트보다 덜 강력하지만 단순화 될 수도 있다.
#마커 단순화는 markevery를 통해 Line2D개체 에서만 사용할 수 있다.
#Marker simplification is only available to Line2D objects (through the markevery property)
'''
ex) plt.plot(x, y, markevery=10)
'''

#더 작은 덩어리로 나누기(Splitting lines into smaller chunks)
#Agg 백엔드를 사용하는 경우 rcParams["agg.path.chunksize"](기본값 0:) 덩어리 크기를 지정할 수 있으며 그보다 많은 정점이있는 모든 라인은 여러 라인으로 분할됩니다.
#어떤 종류의 데이터의 경우 라인을 합리적인 크기로 청킹하면 렌더링 시간을 크게 줄일 수 있습니다.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['path.simplify_threshold'] = 1.0

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

'''
mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()
'''

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()


#범례(Legends)
#좌표축에 대한 기본 범례 동작은 가장 적은 데이터 포인트( loc='best') 를 포함하는 위치를 찾으려고한다.
#데이터 포인트가 많으면 계산비용이 매우 많이들 수 있다. 이 경우 특정 위치를 제공 할 수 있다.

#빠른 스타일 이용하기(Using the fast style)
#The fast style can be used to automatically set simplification and chunking parameters to reasonable settings to speed up plotting large amounts of data
'''
import matplotlib.style as mplstyle
mplstyle.use('fast')
'''
#매우 가볍기 때문에 다른 스타일과 잘 어울립니다. 다른 스타일이 설정을 덮어 쓰지 않도록 빠른 스타일이 마지막에 적용되었는지 확인하세요.
'''
mplstyle.use(['dark_background', 'ggplot', 'fast'])
'''
