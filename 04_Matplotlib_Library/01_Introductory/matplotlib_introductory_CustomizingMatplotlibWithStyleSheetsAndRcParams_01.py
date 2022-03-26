#스타일 시트 사용하기
#이 matplotlib.style패키지는 matplotlib rc파일(시작시 Matplotlib 구성을 위해 읽음)과 동일한 매개변수를 사용하여,
#쉽게 전환할 수 있는 플로팅 "스타일"에 대한 지원을 추가한다.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
plt.style.use('ggplot')
#['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 
# 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 
# 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 
# 'seaborn-whitegrid', 'tableau-colorblind10']
data = np.random.randn(50)

#사용 가능한 모든 스타일을 나열하려면 다음을 사용
print(plt.style.available)