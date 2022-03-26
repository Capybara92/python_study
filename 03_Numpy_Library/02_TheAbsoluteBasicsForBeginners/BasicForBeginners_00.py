#Numpy(Numerical Python)

#거의 모든과학 및 공학분야에서 사용되는 오픈 소스 Python라이브러리이다.
#Python에서 숫자데이터 작업을 위한 보편적 표준이며 과학적 Python 및 PyData 생태계의 핵심이다.
#NumPy 사용자에는 초보부터 최첨단과학, 산업연구, 개발을 수행하는 숙련된 연구원까지 모든 사람이 포함된다.
#NumPy API는 Pandas, SciPy, Matplotlib, scikit-learn, scikit-image 및 대부분의 기타 데이터과학 및 과학 Python패키지에서 광범위하게 사용된다.

#NumPy 라이브러리에는 다차원 배열 및 행렬데이터 구조가 포함되어 있다.
#균일한 N차원 배열개체는 효율적으로 작동하는 방법으로 ndarray를 제공한다.
#NumPy는 배열에서 다양한 수학연산을 수행하는 데 사용할 수 있다. 
#배열과 행렬로 효율적인 계산을 보장하는 강력한 데이터구조를 Python에 추가하고 이러한 배열과 행렬에서 작동하는 고수준 수학함수의 방대한 라이브러리를 제공한다.

import numpy as np #넘파이 가져오기

#예제 코드
a = np.arange(6)
a2 = a[np.newaxis, :]
print(a2.shape)
