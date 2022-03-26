#범주형 변수(categorical variables)로 플로팅하기
#범주 형 변수를 사용하여 그림을 생성 할 수도 있습니다. Matplotlib를 사용하면 범주 형 변수를 여러 플로팅 함수에 직접 전달할 수 있습니다.

import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values) #바
plt.subplot(132)
plt.scatter(names, values) #점
plt.subplot(133)
plt.plot(names, values) #선
plt.suptitle('Categorical Plotting')
plt.show()
