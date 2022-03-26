import matplotlib.pyplot as plt
import numpy as np

#fig = plt.figure()  # an empty figure with no Axes
#fig, ax = plt.subplots()  # a figure with a single Axes
#fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

#Axes
#데이터 공간이있는 이미지의 영역(a plot)
#주어진 Axes 객체는 하나의 Figure. Axes에는 데이터 제한을 처리하는 2개의 (또는 3D의 경우 3개의) Axis개체가 포함되어 있다.
#(axes.Axes.set_xlim()및 axes.Axes.set_ylim()메서드 를 통해 제어 할 수도 있다.)
#Axes은 제목(set_title()), x-라벨 (set_xlabel()) 및 y-라벨(set_ylabel())을 통해 설정된다.

#Axis
#이것은 수의 선과 같은 개체이다. 그들은 그래프 한계를 설정하고 the ticks(the marks on the axis)와 ticklabels(strings labeling the ticks)을 생성한다. 

#Artist
#그림에서 기본적으로 볼 수 있는 모든 아티스트.(또한 Figure, Axes및 Axis객체도 볼 수 있다.)
#This includes Text objects, Line2D objects, collections objects, Patch objects.
#그림이 렌더링되면 모든 아티스트가 화면에 그려집니다.
#대부분의 아티스트는 축에 묶여 있습니다. 이러한 아티스트는 여러 축에서 공유하거나 하나에서 다른 축으로 이동할 수 없습니다.


#기본적으로 Matplotlib를 사용하는 두 가지 방법

#1 기본 스타일
#그림과 축을 명시적으로 만들고 그에 대한 메서드를 호출합니다. ("객체지향 스타일")
#pyplot을 사용하여 그림과 축을 자동으로 생성 및 관리하고 플로팅에 pyplot 함수를 사용합니다.
'''
x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.show()
'''

#2 pyplot 스타일
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()