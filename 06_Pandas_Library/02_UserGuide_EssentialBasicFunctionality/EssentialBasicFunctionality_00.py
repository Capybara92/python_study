#필수 기본 기능
#여기에서는 Pandas 데이터 구조에 공통적으로 적용되는 많은 필수기능에 대해 설명한다.

import numpy as np
import pandas as pd

index = pd.date_range("1/1/2000", periods=8)
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
