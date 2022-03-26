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

#데이터보기
#프레임의 상단 및 하단 행을 보는 방법은 다음과 같다.
print(df.head())
print(df.tail(3))

#인덱스와 열을 출력한다.
print(df.index)
print(df.columns)

#DataFrame.to_numpy()함수는 기본 데이터의 NumPy표현을 제공한다.
#DataFramepandas와 NumPy사이의 근본적인 차이로 귀결되는 데이터 유형이 다른 열이있는 경우 이는 비용이 많이드는 작업일 수 있다.
#NumPy배열에는 전체배열에 대해 하나의 dtype이 있고 pandas DataFrame에는 열(columns)당 하나의 dtype이 있다.
#DataFrame.to_numpy()를 호출하면 pandas는 DataFrame의 모든 dtype을 보유할 수 있는 NumPy dtype을 찾는다.
#이것은 결국 object모든 값을 Python객체로 캐스팅해야 끝날 수 있다.

#DataFrame모든 부동 소수점 값 df에서는, DataFrame.to_numpy()는 빠르고, 복사 데이터를 필요로 하지 않는다.
print(df.to_numpy())

#DataFrame여러 dtypes df2에서는, DataFrame.to_numpy()은 상대적으로 비싸다.
print(df2.to_numpy())
'''DataFrame.to_numpy()은 출력에 인덱스 또는 열 레이블을 포함 하지 않는다.'''

#describe()는 데이터에 대한 빠른 통계 요약을 보여준다.
print(df.describe())

#데이터 전치(Transposing your data)
print(df.T)

#축으로 정렬
print(df.sort_index(axis=1, ascending=False))

#값으로 정렬
print(df.sort_values(by="B"))
