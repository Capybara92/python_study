#Generating visualizations with pyplot is very quick
#pyplot으로 시각화를 생성하는 것은 매우 빠릅니다.

import matplotlib.pyplot as plt
'''
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
'''

#x축이 0-3이고 y축이 1-4인 이유가 궁금 할 수 있다.
#만약 plot로 단일 리스트나 배열을 만들면, matplotlib는 이것이 y 값의 시퀀스라고 가정하고 자동으로 x 값을 생성한다.
#파이썬 범위는 0으로 시작하므로 기본 x벡터의 길이는 y와 같지만 0으로 시작한다. 따라서 x데이터는 .[0, 1, 2, 3]
#plot는 다목적 함수이며 임의의 수의 인수를 사용합니다.


#예를 들어 x, y를 플로팅하려면 다음과 같이 작성할 수 있습니다.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('some numbers')
plt.show()