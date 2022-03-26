#임시 스타일링(Temporary styling)
#특정 코드 블록에만 스타일을 사용하고 전역 스타일을 변경하지 않으려는 경우,
# 스타일 패키지는 변경 내용을 특정 범위로 제한하는 컨텍스트 관리자를 제공한다.
#스타일 변경 사항을 분리하려면 다음과 같이 작성할 수 있습니다.

import matplotlib.pyplot as plt
import numpy as np

with plt.style.context('dark_background'):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
plt.grid(True)
plt.show()