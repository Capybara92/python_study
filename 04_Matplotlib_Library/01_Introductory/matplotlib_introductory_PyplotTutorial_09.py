#로그 및 기타 비선형 축(Logarithmic and other nonlinear axes)
#matplotlib.pyplot은 선형 축 스케일(axis scales)뿐만 아니라 로그(logarithmic) 및 로짓 스케일(logit scales)도 지원합니다.
#데이터가 여러 폭에 걸쳐있는 경우 일반적으로 사용됩니다.

#Changing the scale of an axis is easy
#ex) plt.xscale('log')

#y 축에 대해 동일한 데이터와 다른 스케일을 가진 4개의 플롯의 예가 아래에 나와있다.
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()

#자신 만의 스케일을 추가 할 수도 있다.