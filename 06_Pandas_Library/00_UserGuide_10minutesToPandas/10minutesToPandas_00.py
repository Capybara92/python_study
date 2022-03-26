import numpy as np
import pandas as pd

#객체생성
#값의 리스트를 만든 Series값을 전달하여, pandas가 defualt inteager 인덱스를 만듬.
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

#datetime인덱스와 레이블이 지정된 열(columns)이 있는 NumPy 배열을 전달하여 생성한 DataFrame.
dates = pd.date_range("20130101", periods=6) #20130101날짜부터 6일(periods=6)연속 범위.
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD")) #index=dates는 행으로 나열, columns=list("ABCD")는 열로 나열.
print(df)

#시리즈와 같이 변환할 수 있는 개체의 DICT을 전달하여 만든 DataFrame.
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)

#결과 DataFrame의 열(column)들은 다른 dtypes를 갖는다.
print(df2.dtypes)

#IPython을 사용하는 경우 열 이름(및 공용 속성)에 대한 탭 완성이 자동으로 활성화된다.
#완료 될 속성의 하위집합은 다음과 같다.
'''print(df2.<TAB>) #noqa : E225, E999'''
#당신이 볼 수 있듯이, 열 A, B, C, D의 자동 탭이 완료된다.
#E 그리고 F거기에 있다.
#나머지 속성은 간결함을 위해 잘렸다.
