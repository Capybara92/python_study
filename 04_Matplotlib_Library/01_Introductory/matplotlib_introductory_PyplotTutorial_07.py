#텍스트 작업
#'text'는 임의의 위치에서 텍스트를 추가 할 수 있고 xlabel, ylabel, title들은 표시된 위치에 텍스트를 추가하는 데 사용된다.

import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

#모든 text함수는 matplotlib.text.Text 인스턴스를 반환 합니다.
#위의 줄과 마찬가지로 키워드 인수를 텍스트 함수에 전달하거나 matplotlib.pyplot.step을 사용하여 속성을 사용자 지정할 수 있다.
#ex) t = plt.xlabel('my data', fontsize=14, color='red')