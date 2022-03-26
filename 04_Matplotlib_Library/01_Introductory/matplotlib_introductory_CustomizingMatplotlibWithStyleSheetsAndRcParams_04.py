#Matplotlib rcParams

#동적 RC 설정
#python스크립트에서 또는 python셸에서 대화식으로 기본 rc설정을 동적으로 변경할 수도 있다.
#모든 rc설정은 전역 matplotlib패키지인 matplotlib.rcParams라고 불리는 a dictionary-like variable에 저장되어 있다.
#rcParams는 다음과 같이 직접 수정할 수 있다.

import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
import numpy as np

data = np.random.randn(50)

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
plt.plot(data)
plt.show()


#일반적인 색을 바꾸기 위해서는 prop_cycle property of axes를 바꿔야 한다.
mpl.rcParams['axes.prop_cycle'] = cycler(color=['r', 'g', 'b', 'y'])
plt.plot(data)  # first color is red
plt.show()


#Matplotlib는 rc 설정을 수정하기위한 몇 가지 편리한 기능도 제공
#matplotlib.rc함수의 키워드 인수를 사용하여 한 번에 단일그룹의 여러 설정을 수정하는 데 사용할 수 있다.
mpl.rc('lines', linewidth=4, linestyle='-.')
plt.plot(data)
plt.show()

#matplotlib.rcdefaults함수는 표준 Matplotlib 기본 설정을 복원합니다.
#matplotlib.rcsetup함수는 rcParams의 값을 설정할 때 어느 정도의 유효성 검사가 있다.