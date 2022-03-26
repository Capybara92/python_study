#고유항목 및 개수를 얻는 방법(How to get unique items and counts)
'''np.unique()'''

#np.unique()함수를 사용하면 배열에서 고유 한 요소를 쉽게 찾을 수 있다.

import numpy as np

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])

unique_values = np.unique(a)
print(unique_values)

#NumPy배열(배열에서 고유 값의 첫 번째 인덱스 위치 배열)에서 고유 값의 인덱스를 얻으려면,
#np.unique()배열과 함께 return_index인수를 전달하면 된다.
unique_values, indices_list = np.unique(a, return_index=True)
print(indices_list) #인덱스 리턴

#np.unique()배열과 함께 return_counts인수를 전달하여 NumPy배열에서 고유 한 값의 빈도 수를 가져올 수 있다.
unique_values, occurrence_count = np.unique(a, return_counts=True)
print(occurrence_count) #빈도수
print()


#2D 배열에서도 작동한다.
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])

unique_values = np.unique(a_2d)
print(unique_values) #축 인수가 전달되지 않으면 2D배열이 평평해 진다.

unique_rows = np.unique(a_2d, axis=1)
print(unique_rows)
#고유한 행이나 열을 얻으려면 axis인수를 전달해야 한다.
#고유한 행을 찾으려면 axis=0을 지정하고 열을 찾으려면 axis=1을 지정한다.

#고유 행, 인덱스 위치 및 발생 횟수를 가져 오려면 다음을 사용한다.
unique_rows, indices, occurrence_count = np.unique(
      a_2d, axis=0, return_counts=True, return_index=True)
      
print(unique_rows)
print(indices)
print(occurrence_count)
