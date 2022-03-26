#Matplotlib로 배열 플로팅하기(Plotting arrays with Matplotlib)
#Plotting : 제도(製圖), 구획 정리

#값에 대한 플롯을 생성 해야하는 경우 Matplotlib을 사용하면 매우 간단하다.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])

#값을 플로팅하기 위해 수행하는 작업
plt.plot(a)

#1D 배열을 플로팅
x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple') # line
plt.plot(x, y, 'o')      # dots

#Matplotlib를 사용하면 수많은 시각화 옵션에 액세스할 수 있다.
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')

plt.show()
