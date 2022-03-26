import numpy as np
import pandas as pd

#그룹화(Grouping)
#"그룹 별"이란 다음 단계 중 하나 이상이 포함 된 프로세스를 의미한다.
#   - 일부 기준에 따라 데이터를 그룹으로 분할.
#   - 각 그룹에 독립적으로 기능 적용.
#   - 결과를 데이터 구조로 결합.
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
print(df)

#그룹화 한 다음 sum()결과 그룹에 함수를 적용한다.
print(df.groupby("A").sum())

#여러 열로 그룹화하면 계층적 인덱스가 형성되어 다시 sum()함수를 적용할 수 있다.
print(df.groupby(["A", "B"]).sum())

''''''
#재구성(Reshaping)
#스택
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
print(df2)

#이 stack()메서드는 DataFrame의 열에서 레벨을 "압축"한다.
stacked = df2.stack()
print(stacked)

#"stacked"이 DataFrame 또는 Series(MultiIndex가 index)인 경우, stack()의 역 연산은 default unstacks the last level인 unstack()이다.
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))

#피벗 테이블(Pivot tables), Pivot : 중심점, (중심을 축으로)회전하다
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
print(df)

#이 데이터에서 매우 쉽게 피벗 테이블을 생성할 수 있다.
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))

''''''
#타임시리즈(Time series).
#pandas는 빈도변환 중 리샘플링 작업을 수행하기 위한 간단하고 강력하며 효율적인 기능을 제공한다.
#이는 금융 애플리케이션에서 매우 일반적이지만 이에 국한되지는 않는다.
#예 : 2차 데이터를 5분 데이터로 변환.
rng = pd.date_range("1/1/2012", periods=100, freq="S")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts.resample("5Min").sum())

#시간대 표현.
rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)

ts_utc = ts.tz_localize("UTC")
print(ts_utc)

#다른 시간대로 변환.
print(ts_utc.tz_convert("US/Eastern"))

#시간범위 표현 간 변환
rng = pd.date_range("1/1/2012", periods=5, freq="M")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)

ps = ts.to_period()
print(ps)
print(ps.to_timestamp())

#기간과 타임스탬프 사이를 변환하면 편리한 산술함수를 사용할 수 있다.
#다음 예에서는 연도가 11월로 끝나는 분기별 빈도를 분기 종료 후 월말 오전 9시로 변환한다.
prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9
print(ts.head())
