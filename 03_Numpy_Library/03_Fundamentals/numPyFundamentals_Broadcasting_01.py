#일반 방송 규칙(General Broadcasting Rules)

#두 배열에서 작동할 때 NumPy는 해당모양을 요소별로 비교한다.
#후행(즉, 가장 오른쪽)치수로 시작하여 왼쪽으로 작동힌다.
#다음과 같은 경우 두 차원이 호환된다.
#   - they are equal, or
#   - one of them is 1

#이러한 조건이 충족되지 않으면, 「ValueError: operands could not be broadcast together」예외가 발생하여 배열에 호환되지 않는 모양이 있음을 나타낸다.
#결과배열의 크기는 입력의 각 축을 따른 1이 아닌 크기이다.

#배열의 차원의 수가 같을 필요는 없다.
#예를 들어 256x256x3RGB 값 배열이 있고 이미지의 각 색상을 다른 값으로 배율 조정하려는 경우,
#이미지에 3개의 값이있는 1차원 배열을 곱할 수 있다.
#브로드캐스트 규칙에 따라 이러한 배열의 후행 축 크기를 정렬하면 호환된다는 것을 알 수 있다.
'''
    Image  (3d array): 256 x 256 x 3
    Scale  (1d array):             3
    Result (3d array): 256 x 256 x 3
'''
#비교 된 차원 중 하나가 1이면 다른 차원이 사용된다.
#즉, 크기가 1인 차원은 다른차원과 일치하도록 확장되거나 "복사"된다.

#다음 예제에서 A및 B배열에는 브로드캐스트 작업 중에 더 큰 크기로 확장되는 길이가 1인 축이 있다.
'''
    A      (4d array):  8 x 1 x 6 x 1
    B      (3d array):      7 x 1 x 5
    Result (4d array):  8 x 7 x 6 x 5
'''

#몇 가지 예.
'''
    A      (2d array):  5 x 4
    B      (1d array):      1
    Result (2d array):  5 x 4

    A      (2d array):  5 x 4
    B      (1d array):      4
    Result (2d array):  5 x 4

    A      (3d array):  15 x 3 x 5
    B      (3d array):  15 x 1 x 5
    Result (3d array):  15 x 3 x 5

    A      (3d array):  15 x 3 x 5
    B      (2d array):       3 x 5
    Result (3d array):  15 x 3 x 5

    A      (3d array):  15 x 3 x 5
    B      (2d array):       3 x 1
    Result (3d array):  15 x 3 x 5
'''

#다음은 브로드 캐스트하지 않는 모양의 예.
'''
    A      (1d array):  3
    B      (1d array):  4 # trailing dimensions do not match

    A      (2d array):      2 x 1
    B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched
'''
