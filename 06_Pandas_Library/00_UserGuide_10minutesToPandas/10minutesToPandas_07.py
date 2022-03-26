import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#카테고리
#pandas는 DataFrame에 카테고리 데이터를 포함할 수 있다.
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)

#raw grade를 카테고리 데이터 유형으로 변환
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])

#카테고리 이름을 보다 의미있는 이름으로 바꾼다. ( Series.cat.categories()가 할당됨)
df["grade"].cat.categories = ["very good", "good", "very bad"]

#카테고리 재 정렬하고 동시에 누락된 카테고리 추가한다. (methods under Series.cat() return a new Series by default)
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)
print(df["grade"])

#정렬은 어휘순서가 아닌 카테고리의 순서에 따라 이루어진다.
print(df.sort_values(by="grade"))

#카테고리의 열로 그룹화하면 빈 카테고리도 표시된다.
print(df.groupby("grade").size())

''''''
#플로팅
plt.close("all")

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

#DataFrame에서 이 plot()메서드는 레이블이 있는 모든 열을 표시하는 데 편리하다.
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)

df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')

plt.show()
