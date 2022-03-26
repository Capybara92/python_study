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

#얻기.
#series범위에 있고, df.A와 같은 단일 열(column)을 선택한다.
print(df["A"])

#[]를 통해 행을 슬라이스 한다. 
print(df[0:3])
print(df["20130102":"20130104"])

''''''
#라벨로 선택.
#For getting a cross section using a label.
print(df.loc[dates[0]])

#Selecting on a multi-axis by label.
print(df.loc[:, ["A", "B"]])

#Showing label slicing, both endpoints are included.
print(df.loc["20130102":"20130104", ["A", "B"]])

#반환 된 객체의 크기 감소(Reduction in the dimensions of the returned object).
print(df.loc["20130102", ["A", "B"]])

#스칼라 값 얻기(For getting a scalar value).
print(df.loc[dates[0], "A"])

#스칼라에 빠르게 액세스하기(For getting fast access to a scalar (equivalent to the prior method)).
print(df.at[dates[0], "A"])
