#데이터 입출력

import numpy as np
import pandas as pd

df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)

#CSV.
#CSV파일에 쓰기.
'''df.to_csv("foo.csv")'''
#CSV파일에서 읽기.
'''pd.read_csv("foo.csv")'''

#HDF5.
#HDF5 Store에 쓰기.
'''df.to_hdf("foo.h5", "df")'''
#HDF5 Store에서 읽기.
'''pd.read_hdf("foo.h5", "df")'''

#엑셀(Excel).
#엑셀 파일에 쓰기.
'''df.to_excel("foo.xlsx", sheet_name="Sheet1")'''
#엑셀 파일에서 읽기.
'''pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])'''

''''''
#고차(Gotchas)
#작업을 수행하려는 경우 다음과 같은 예외가 표시 될 수 있다.
'''
if pd.Series([False, True, False]):
    print("I was true")

#Traceback
#ValueError: The truth value of an array is ambiguous. Use a.empty, a.any() or a.all().
'''
