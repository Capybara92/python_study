#plot 스타일 서식 지정

#모든 x, y 쌍의 인수에 대해 플롯의 색상과 선 유형을 나타내는 형식 문자열인 선택적 세 번째 인수가 있다.
#형식 문자열의 문자와 기호는 MATLAB에서 가져 왔으며 색상 문자열을 선 스타일 문자열과 연결한다.

import matplotlib.pyplot as plt
import numpy as np

#빨간색 원으로 그리려면 다음을 실행한다.
'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
'''
#위 예제의 axis함수는 [xmin, xmax, ymin, ymax]의 리스트를 가져와서 좌표축의 viewport를 지정한다


#matplotlib가 리스트로 제한되면 숫자 처리에 상당히 쓸모가 없습니다. 일반적으로 numpy 배열 을 사용 합니다. 실제로 모든 시퀀스는 내부적으로 numpy 배열로 변환됩니다.
#아래 예제는 배열을 사용하여 하나의 함수 호출에서 서로 다른 형식 스타일로 여러 줄을 그리는 것을 보여줍니다.
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
