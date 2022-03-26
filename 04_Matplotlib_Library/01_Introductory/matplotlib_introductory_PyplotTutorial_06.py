#여러도형 및 축 작업
#MATLAB 및 pyplot에는 현재 Figure와 현재 좌표축의 개념이 있다.
#모든 플로팅 기능은 현재 좌표축에 적용된다.
#matplotlib.pyplot.gca함수는 현재 좌표축(matplotlib.axes.Axes인스턴스)을 반환하고, 
#matplotlib.pyplot.gcf함수는 현재Figure(matplotlib.figure.Figure인스턴스)를 반환한다. 
#아래는 두 개의 서브 플롯을 만드는 스크립트이다.

import matplotlib.pyplot as plt
import numpy as np

'''
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
'''

#figure nymber가 증가 하는 여러 figure호출을 사용하여 여러 그림을 만들 수 있다.
#물론 각 figure는 자신이 원하는만큼의 축과 subplots이 포함될 수 있다.
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title
plt.show()

#figure에 필요한 메모리는 figure가 close함수로 닫힐 때까지 완전히 해제되지 않는다.
#figure에 대한 모든 참조를 삭제하거나 또는 창 관리자를 사용하여 figure이 화면에 나타나는 창을 종료하는 것만으로는 충분하지 않습니다.
#pyplot.close이 호출 될 때까지 내부 참조를 유지하기 때문 입니다.