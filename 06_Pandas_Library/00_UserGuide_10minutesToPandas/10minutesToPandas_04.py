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

#설정
#새로운 열을 설정하면 인덱스별로 데이터가 자동으로 정렬된다.
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
print(s1)
df["F"] = s1

#라벨 별 설정 값 
df.at[dates[0], "A"] = 0

#위치 별 설정 값
df.iat[0, 1] = 0

#NumPy 배열로 할당하여 설정
df.loc[:, "D"] = np.array([5] * len(df))

#위의 작업의 결과
print(df)

#A where operation with setting
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)

''''''
#누락 된 데이터(Missing data)
#pandas는 주로 nan값을 사용하여 누락 된 데이터를 나타낸다.
#인덱싱을 다시 사용하면 지정된 축에서 인덱스를 변경 / 추가 / 삭제할 수 있다.
#이것은 데이터의 복사본을 반환한다.
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
print(df1)

#누락 된 데이터가있는 행을 삭제.
print(df1.dropna(how="any"))

#누락 된 데이터 채우기.
print(df1.fillna(value=5))

#값이 nan인 부울 마스크를 가져오기.
print(pd.isna(df1))
