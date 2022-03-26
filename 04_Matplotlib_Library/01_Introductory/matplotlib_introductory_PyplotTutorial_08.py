#텍스트에서 수학 표현식 사용하기
#matplotlib는 모든 텍스트 표현식에서 TeX 방정식 표현식을 허용한다다.
#예를 들어 σi=15 표현식을 작성하려면 제목에서 달러기호($)로 둘러싸인 TeX 표현식을 작성할 수 있습니다.

#ex) plt.title(r'$\sigma_i=15$')

#문자열 앞에 선행하는 'r'은 중요하다.
#위의 의미는 문자열은 파이선 이스케이프로 raw문자열 이고 백 슬래시로 다루지 않는다.
#matplotlib에는 TeX 표현식 파서(parser) 및 레이아웃 엔진이 내장되어 있으며 자체 수학 글꼴을 제공합니다.
#TeX를 설치하지 않고도 여러 플랫폼에서 수학 텍스트를 사용할 수 있습니다.


#텍스트 주석 달기
#text의 기본기능을 사용하면 축의 임의위치에 텍스트를 배치할 수 있습니다.
#텍스트의 일반적인 용도는 플롯의 일부 기능에 주석을 추가하는 것이며,이 annotate메서드는 주석을 쉽게 만드는 도우미 기능을 제공합니다.

import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()

#이 기본 예에서 xy(화살표)와 xytext위치(텍스트 위치)는 모두 데이터 좌표에 있습니다. 다른 다양한 좌표계를 선택할 수 있습니다.