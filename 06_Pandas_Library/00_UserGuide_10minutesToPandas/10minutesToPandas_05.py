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

#운영
#통계
#일반적으로 연산은 누락된 데이터를 제외한다.
print(df.mean())

#다른 축에서 동일한 작업.
print(df.mean(1))

#차원이 다르고 정렬이 필요한 개체로 작동한다.
#또한 Pandas는 지정된 차원을 따라 자동으로 브로드캐스트 된다.
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)
print(df.sub(s, axis="index"))

#적용
#데이터에 함수 적용.
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))

#히스토그램(Histogramming) : 비교할 양이나 수치의 분포를 막대 모양의 도형으로 나타낸 그래프.
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())

#문자열 메서드
#Series에는 배열의 각 요소에서 쉽게 조작 할 수 있도록 str속성에 문자열 처리 메소드의 세트가 있다, as in the code snippet below. 
#str의 패턴매칭은 일반적으로는 정규식을 사용하지만, 몇 경우는 항상 정규식을 사용한다.
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print(s.str.lower())

''''''
#병합(Merge)
#concat()메서드.
#Pandas는 Series 및 DataFrame 객체를 결합, 병합 유형작업의 경우 인덱스 및 관계형 대수기능에 대한 다양한 종류의 세트로직과 함께 쉽게 결합할 수있는 다양한 기능을 제공한다.
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
pieces = [df[:3], df[3:7], df[7:]] #break it into pieces
print(pd.concat(pieces))

#가입(Join)
#SQL 스타일의 병합.
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on="key"))
#또는
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on="key"))
