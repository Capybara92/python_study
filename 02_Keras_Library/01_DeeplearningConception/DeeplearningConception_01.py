#학습과정 이야기
#같은 문제집이라도 사람마다 푸는 방식이 다르고 학습된 결과도 다르다.
#딥러닝 모델의 학습도 비슷하다.
#케라스에서는 모델을 학습시킬 때 fit()함수를 사용하는데, 그 파라미터(인자)에 따라 학습과정 및 결과가 차이난다.

#배치사이즈와 에포크
'''
model.fit(x, y, batch_size=32, epochs=10)

x          : 입력 데이터                                 ex) 100문항의 문제들
y          : 라벨 값                                    ex)  100문항의 답들
batch_size : 몇 개의 샘플로 가중치를 갱신할 것인지 지정    
epochs     : 학습 반복 횟수                              
'''

#batch_size(배치사이즈)
#배치사이즈는 몇 문항을 풀고 해답을 맞추는 지를 의미한다.
#100문항일 때, 배치사이즈가 100이면 전체를 다 풀고 난 뒤에 해답을 맞춰보는 것이다.
#우리가 해답을 맞춰볼 때 ‘아하, 이렇게 푸는구나’라고 느끼면서 학습하는 것처럼 모델도 이러한 과정을 통해 가중치가 갱신된다.

#문제를 푼 뒤 해답과 맞춰봐야 학습이 일어난다. 
#   > 모델의 결과값과 주어진 라벨값과의 오차를 줄이기 위해, 「역전파(Backpropagation)」 알고리즘으로 가중치가 갱신된다.

#배치사이즈가 10이면 열 문제씩 풀어보고 해답 맞춰보는 것이다.
#100문항을 10문제씩 나누어서 10번 해답을 맞추므로 가중치 갱신은 10번 일어난다.

#100문항 다 풀고 해답과 맞추어보려면 문제가 무엇이었는지 다 기억을 해야 맞춰보면서 학습이 된다 -> 기억력(용량)이 커야한다.
#1문항씩 풀고 해답 맞추면 학습은 꼼꼼히 잘 되겠지만                                         -> 시간이 너무 걸린다.
#배치사이즈가 작을수록 가중치 갱신이 자주 일어난다.

''''''
#epchos(에포크)
#100문항의 문제들을 몇 번이나 반복해서 풀어보는 지 정하는 것이다.
#에포크가 20이면 100문항을 20번 푸는 것이다.
#모델도 같은 데이터셋으로 반복적으로 가중치를 갱신하면서 모델이 학습된다.
#같은 문제라도 이전에 풀었을 때랑 지금 풀었을 때랑 학습상태(가중치)가 다르기 때문에 다시 학습이 일어난다.

#모의고사 1회분을 20번 푸는 것과 서로 다른 모의고사 20회분을 1번 푸는 것과는 어떤 차이가 있을까?
#이것은 분야에 따라 데이터특성에 따라 다를 것이라고 생각한다.
#잡다한 문제를 많이 푸는 것보다 양질의 문제를 여러 번 푸는 것이 도움이 된다고 생각한다.
#피아노를 배울 때도 기본 곡을 반복적으로 학습하면 다양한 악보도 쉽게 보는 반면 이곡 저곡 연습하면 제대로 익히기 쉽지 않다.
#이런 문제를 제외하고도 현실적으로 데이터를 구하기가 쉽지 않기 때문에 제한된 데이터셋으로 반복적으로 학습하는 것이 효율적이다.

'''
Q & A
Q1) 그럼 에포크를 무조건 늘리면 좋은가요?
A1) 아닙니다. 하나의 문제집만 계속 학습하면 오히려 역효과가 발생할 수 있습니다.
    피아노 칠 때 처음에 곡을 연습할 때는 악보를 보면서 치다가 다음엔 악보안보고도 치고, 나중엔 눈감고도 칩니다.
    눈감고만 치다보면 악보 보는 법을 까먹게 되고 다른 곡을 치지 못하는 지경에 이릅니다. 
    연습한 곡은 완벽하게 칠 지 몰라도 다른 곡은 치지 못하는 상태가 됩니다. 
    우린 이것을 오버피팅(overfitting)이라고 부릅니다. 
    악보보고 잘 치는 정도에서 그만 연습하는 것이 더 좋았을 수 있습니다. 
    실제로 모델을 학습할 때도 오버피팅이 일어나는 지 체크하다가 조짐이 보이면 학습을 중단합니다.
'''