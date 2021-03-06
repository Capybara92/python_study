#데이터 셋 이야기
#딥러닝 모델을 학습시키려면 데이터셋이 필요하다.
#풀고자 하는 문제 및 만들고자 하는 모델에 따라 데이터셋 설계도 달라진다.
 
#훈련셋, 검증셋, 시험셋
#검증셋, 시험셋은 학습을 시키면 안된다.

#검증셋으로 가장 높은평가를 받은 학습방법이 최적의 학습방법이라고 생각하면 된다.
#이러한 학습방법을 결정하는 파라미터를 하이퍼파라미터(hyperparameter)라고 하고, 최적의 학습방법을 찾아가는 것을 하이퍼파라미터 튜닝이라고 한다.
#검증셋이 있다면 스스로 평가하면서 적절한 학습방법을 찾아볼 수 있다.
#검증셋이 있다면 어느정도의 반복학습이 좋을지를 정한다. 

#「학습」 : 문제와 해답지를 같이 준 후 문제 푼 뒤 정답과 맞추어서 학습을 하라는 것이다.
#「평가」 : 문제만 주고 풀게한 뒤 맞는 지 틀린 지 점수만 계산하는 것이다.

#언더피팅(underfitting)이란 학습을 더 하면 성능이 높아질 가능성이 있는 상태이다.
 
#에포크(epochs)를 계속 증가시키다 보면 더 이상 검증셋의 평가는 높아지지 않고 오버피팅(overfitting)이 되어 오히려 틀린 개수가 많아진다.
#이 시점이 적정 반복 횟수로 보고 학습을 중단한다.
#이를 조기종료(early stopping)이라고 한다.

#교차검증은 계산량이 많기 때문에 데이터 수가 많지 않을 때 사용하며, 딥러닝 모델은 대량의 데이터를 사용하므로 잘 사용하지 않는다고 한다.

'''
Q & A
Q1) 검증셋이 학습 시에 사용되기 때문에 가중치 갱신에 영향을 미치나요?
A1) 아닙니다. 학습 시에 현재 학습된 상태에서 평가로만 사용되므로 가중치 갱신은 일어나지 않습니다.

Q2) 교차검증 시에 검증셋을 바꿀 때 마다 학습된 상태를 초기화해야 하나요?
A2) 맞습니다. 첫번째 검증 시 모의고사 5회를 사용하였고, 두번째 검증 시 모의고사 4회를 사용할 경우, 
    첫번째 검증 시에 모의고사 1회~4회를 학습한 상태이기 때문에 만약 초기화하지 않으면 
    두번째 검증 시에 이미 모의고사 4회를 학습한 상태에서 검증하기 때문에 공정한 평가라고 보기 힘듭니다.
'''
