#키워드 문자열로 플로팅하기
#문자열을 사용하여 특정변수에 액세스 할 수있는 형식의 데이터가 있는 경우가 있다. 예를 들어, numpy.recarray또는 pandas.DataFrame.
#Matplotlib를 사용하면 data키워드 인수 와 함께 이러한 객체를 제공 할 수 있다.
#제공된 경우 이러한 변수에 해당하는 문자열로 플롯을 생성 할 수 있습니다.

import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

