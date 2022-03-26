#평가 이야기1
#이번에는 학습한 모델을 어떤 기준으로 평가를 해야되는 지를 알아보자.
#모델을 평가한다고 하면 정확도라는 단어를 떠올리기 쉬운데, 문제에 따라 단순히 정확도로만 평가하기 힘든경우가 있다.
#조금 더 알아보면 「민감도, 특이도, 재현」율 등의 용어가 나오는데, 비전공자에게는 생소하게만 느껴진다.
#몇가지 문제와 모델을 정의하고 여기에 적합한 평가 기준이 무엇인지 알아보자.
#보통평가에 관련된 내용을 보면 표와 수식이 많은 편인데, 손가락만 있으면 계산할 수 있도록 간단한 예제를 통해 알아보자.
#레고로 해본다. (짝수레고 6개, 홀수레고 4개)
'''
「케라스_평가하기.docx」에 정리
'''


''''''
#분류하기
#ROC(Receiver Operating Characteristic) curve  : 민감도와 특이도가 어떤 관계를 가지고 변하는 지 그래프로 표시한 것.
#AUC(Area Under Curve) : ROC curve 아래 면적을 구한 값.

import matplotlib.pyplot as plt
import numpy as np

sens_F = np.array([1.0,  1.0, 1.0,  1.0, 0.75,  0.5,  0.5, 0.5, 0.5, 0.5, 0.0])
spec_F = np.array([0.0, 0.16, 0.5, 0.66, 0.66, 0.66, 0.83, 1.0, 1.0, 1.0, 1.0])

sens_G = np.array([1.0,  1.0, 0.75, 0.75, 0.5,  0.5,  0.5,  0.5, 0.25, 0.25, 0.0])
spec_G = np.array([0.0, 0.33, 0.33,  0.5, 0.5, 0.66, 0.66, 0.83, 0.83,  1.0, 1.0])

plt.title('Receiver Operating Characteristic')
plt.xlabel('False Positive Rate(1 - Specificity)')
plt.ylabel('True Positive Rate(Sensitivity)')

plt.plot(1-spec_F, sens_F, 'b', label = 'Model F')   
plt.plot(1-spec_G, sens_G, 'g', label = 'Model G') 
plt.plot([0,1],[1,1],'y--')
plt.plot([0,1],[0,1],'r--')

plt.legend(loc='lower right')
plt.show()

#여기서 노란점선이 이상적인 모델을 표시한 것이다.
#임계값과 상관없이 민감도와 특이도가 100%일때를 말하고, AUC 값은 1이다.
#빨간점선은 기준선으로서 AUC값이 0.5이다.
#개발한 모델을 사용하려면, 적어도 이 기준선보다는 상위에 있어야 되겠지?
#모델 F와 모델 G를 비교해보면, 모델 F가 모델 G보다 상위에 있음을 알 수 있다.
#AUC를 보더라도 모델 F가 면적이 더 넓다.


''''''
#sklearn 패키지는 ROC curve 및 AUC를 좀 더 쉽게 구할 수 있는 함수를 제공한다. 
#임계값 변화에 따른 민감도, 특이도를 계산해서 입력할 필요없이, 클래스 값과 모델에서 나오는 클래스 확률 값을 그대로 입력하면, 
#ROC curve를 그릴 수 있는 값과 AUC 값을 알려준다.
#sklearn 패키지를 이용한 소스코드는 다음과 같다.
'''
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

class_F = np.array([0, 0, 0, 0, 1, 1, 0, 0, 1, 1])
proba_F = np.array([0.05, 0.15, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.95, 0.95])

class_G = np.array([0, 0, 1, 0, 1, 0, 0, 1, 0, 1])
proba_G = np.array([0.05, 0.05, 0.15, 0.25, 0.35, 0.45, 0.65, 0.75, 0.85, 0.95])

false_positive_rate_F, true_positive_rate_F, thresholds_F = roc_curve(class_F, proba_F)
false_positive_rate_G, true_positive_rate_G, thresholds_G = roc_curve(class_G, proba_G)
roc_auc_F = auc(false_positive_rate_F, true_positive_rate_F)
roc_auc_G = auc(false_positive_rate_G, true_positive_rate_G)

plt.title('Receiver Operating Characteristic')
plt.xlabel('False Positive Rate(1 - Specificity)')
plt.ylabel('True Positive Rate(Sensitivity)')


plt.plot(false_positive_rate_F, true_positive_rate_F, 'b', label='Model F (AUC = %0.2f)'% roc_auc_F)
plt.plot(false_positive_rate_G, true_positive_rate_G, 'g', label='Model G (AUC = %0.2f)'% roc_auc_G)
plt.plot([0,1],[1,1],'y--')
plt.plot([0,1],[0,1],'r--')

plt.legend(loc='lower right')
plt.show()
'''
