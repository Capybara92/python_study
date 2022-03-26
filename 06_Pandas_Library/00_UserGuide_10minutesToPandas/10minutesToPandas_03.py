import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
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

#위치별 선택.
#전달 된 정수의 위치를 ​​통해 선택.
print(df.iloc[3])

#정수 슬라이스로 numpy / Python과 유사하게 작동.
print(df.iloc[3:5, 0:2])

#행을 명시 적으로 분할.
print(df.iloc[1:3, :])

#열을 명시 적으로 분할.
print(df.iloc[:, 1:3])

#명시적으로 값 얻기.
print(df.iloc[1, 1])

#스칼라에 빠르게 액세스
print(df.iat[1, 1])

''''''
#부울 인덱싱
#단일 열의 값을 사용하여 데이터를 선택.
print(df[df["A"] > 0])

#부울 조건이 충족되는 DataFrame에서 값 선택.
print(df[df > 0])

#isin()필터링 방법 사용.
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
print(df2)
print(df2[df2["E"].isin(["two", "four"])])
