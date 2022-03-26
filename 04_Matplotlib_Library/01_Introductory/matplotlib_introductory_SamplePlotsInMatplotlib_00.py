#Matplotlib의 샘플 plots

#선 Plot
#텍스트 레이블이있는 선 figure을 만드는 방법
#   matplotlib.pyploy.plot()

#하나의 figure에 여러 subplots
#여러 축 (예 : 서브 플롯)이 생성
#   matplotlib.pyploy.subplot()

#이미지
#이미지를 표시할 수 있다. (동일한 간격의 수평 치수 가정)
#   matplotlib.pyploy.imshow()

#윤곽과 유사색
#수평 차원의 간격이 고르지 않은 경우에도 2 차원 배열의 색상 표현을 만들 수 있다.
#   matplotlib.pyploy.pcolormesh()
#동일한 데이터를 표현
#   matplotlib.pyploy.contour()

#히스토그램
#자동으로 히스토그램을 생성하고 빈 개수 또는 확률을 반환한다.
#   matplotlib.pyploy.hist()

#경로
#Matplotlib에서 임의의 경로를 추가 할 수 있다.
#   matplotlib.path

#3차원 플로팅
#표면, 와이어 프레임, 분산 형 및 막대 차트를 포함한 간단한 3D 그래프를 지원한다.
#   The mplot3d toolkit (이 툴킷은 모든 표준 Matplotlib 설치에 포함되어 있다.)

#스트림 플롯
#벡터 장의 유선을 플로팅한다.
#유선형을 단순히 플로팅하는 것 외에도 유선형의 색상 및 선, 너비를 벡터 필드의 속도 또는 로컬 강도와 같은 별도의 매개 변수에 매핑 할 수 있다.
#   matplotlib.pyploy.streamplot()
#벡터 필드 플로팅 기능을 보완 -> matplotlib.pyploy.quiver()

#타원
#화성에 대한 「Phoenix」임무 (Matplotlib를 사용하여 우주선의 지상 추적 표시)를 지원하기 위해
#matplotlib.pyploy.Arc하여 확대 / 축소 수준에 민감하지 않은 타원 호 (참조 )에 대해 매우 정확한 8- 스플라인 근사치를 제공

#막대 차트
#오차 막대와 같은 사용자 지정을 포함하는 막대 차트를 만든다.
#   matplotlib.pyploy.bar()
#누적막대 -> bar_stacked.py
#가로막대 -> barh.py 로도 가능하다.

#파이차트
#원형 차트를 만들 수 있다.
#선택적 기능에는 영역, 비율, 자동 레이블지정, 원형 중앙에서 하나 이상의 쐐기 폭발 및 그림자 효과가 포함된다.
#   matplotlib.pyploy.pie()

#테이블
#좌표축에 텍스트 테이블을 추가
#   matplotlib.pyploy.table()

#산점도
#크기 및 색상 인수를 사용하여 산점도를 만듭니다.
#   matplotlib.pyploy.scatter()

#GUI위젯
#Matplotlib에는 사용중인 그래픽 사용자 인터페이스와 독립적인 기본 GUI위젯이 있어 교차 GUI그림 및 위젯을 작성할 수 있습니다.
#   matplotlib.widgets

#채워진 곡선
#채워진 곡선과 다각형을 그릴 수 있다.
#   matplotlib.pyploy.fill()

#날짜 처리
#메이저 및 마이너 틱과 둘 모두에 대한 사용자 지정 틱 포맷터(custom tick formatters)를 사용하여 시계열 데이터를 플로팅 할 수 있습니다.
#   matplotlib.ticker
#   matplotlib.dates

#로그플롯
#대수 플롯의 생성을 단순화.
#   matplotlib.pyploy.semilogx()
#   matplotlib.pyploy.semilogy()
#   matplotlib.pyploy.loglog()

#극좌표
#   matplotlib.pyploy.polar()

#범례
#MATLAB과 호환되는 범례 배치 함수를 사용하여 그림 범례를 자동으로 생성한다.
#   matplotlib.pyploy.legend()

#텍스트 객체에 대한 TeX 표기법
#다음은 Matplotlib의 내부 수학 텍스트 엔진에서 지원하는 많은 TeX 표현식의 샘플이다.
#mathtext모듈은 FreeType, DejaVu, BaKoMa 컴퓨터모던 또는 STIX글꼴을 사용하여 TeX 스타일의 수학 표현식을 제공한다.
#   matplotlib.mathtext

#네이티브 TeX 렌더링
#Matplotlib의 내부 수학 렌더링 엔진은 매우 강력하지만 때로는 TeX가 필요하다.
#Matplotlib는 usetex 옵션을 사용하여 문자열의 외부 TeX 렌더링을 지원한다.

#EEG GUI
#Matplotlib를 pygtk, wx, Tk, Qt 애플리케이션에 포함 할 수 있다.
#「pbrain」 라는 EEG 뷰어의 스크린 샷
#   matplotlib.pyploy.specgram()

#XKCD 스타일 스케치 플롯
#재미로 Matplotlib는 「xkcd」 스타일의 플로팅을 지원합니다 .

#서브플롯 예제
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()
