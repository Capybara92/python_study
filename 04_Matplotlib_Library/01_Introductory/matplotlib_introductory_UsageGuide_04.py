import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()

#버전 1.0 이전에는 show()일반적으로 단일 스크립트에서 두 번 이상 호출 할 수 없었습니다. 
#버전 1.0.1 이상에서는이 제한이 해제되므로 위와 같은 스크립트를 작성할 수 있습니다.

'''
내용 요약
대화 형 모드에서 pyplot 함수는 자동으로 화면에 그립니다.
대화 형으로 플로팅 할 때 pyplot 함수 외에 객체 메서드 호출을 사용하는 경우 draw()플롯을 새로 고치고 싶을 때마다 호출 하십시오.

하나 이상의 그림을 생성하고 새 그림 세트를 종료하거나 생성하기 전에 표시하려는 스크립트에서 비대화 형 모드를 사용하십시오.
이 경우 show()그림을 표시하고 수동으로 삭제할 때까지 실행을 차단하는 데 사용하십시오.
'''