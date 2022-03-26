#데이터
#여러 회사의 판매 정보가 포함되어 있다.
import numpy as np
import matplotlib.pyplot as plt

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

#정수를 입력으로 받고 문자열을 출력으로 반환하는 함수를 정의. (7)
#x인수는 the original tick label이고, pos인수는 the tick position이다. 여기서 x만 사용 하지만 두 인수가 모두 필요하다.
def currency(x, pos):
    """The two args are the value and tick position"""
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

#스타일 제어하기 (2)
print(plt.style.available) #시각화를 필요에 맞게 조정할 수 있도록 Matplotlib에서 사용할 수있는 많은 스타일이 있다.
plt.style.use('fivethirtyeight') #스타일을 활성화
#스타일은 색상, 선폭, 배경 등과 같은 많은 것을 제어한다.

#rcParams를 사용하여 플롯의 스타일, 레이아웃 및 기타 기능을 제어 (4)
plt.rcParams.update({'figure.autolayout': True})
#Matplotlib에 우리가 만든 그림의 요소를위한 공간을 자동으로 만들도록 지시 할 수 있습니다. 이를위해 autolayoutrcParams의 값을 설정한다.

#객체 지향 접근 방식으로이를 수행하기 위해 먼저 matplotlib.figure.Figure와 matplotlib.axes.Axes의 인스턴스를 생성한다. (1)
fig, ax = plt.subplots(figsize=(8, 4)) #Figure는 캔버스와 같고 Axes는 특정 시각화를 만들 캔버스의 일부이다. #플롯의 크기를 조정할 수도 있다. (5)
'''NumPy의 인덱싱은 형식(행, 열)을 따르지만 figsize kwarg는 형식(너비, 높이)을 따릅니다. 이것은 시각화의 관습을 따르며, 불행히도 선형 대수의 관습과 다릅니다.'''
ax.barh(group_names, group_data) #Axes인스턴스가 있으므로 그 위에 플로팅 할 수 있다.

#플롯 사용자 지정
labels = ax.get_xticklabels() #x 축에서 레이블을 회전 #matplotlib.axes.Axes.get_xticklabels()방법 으로 이러한 레이블에 액세스 할 수 있다. (3)
plt.setp(labels, rotation=45, horizontalalignment='right') #한 번에 많은 항목의 속성을 설정하고 싶다면 matplotlib.pyplot.setp()기능 을 사용하는 것이 유용. (3)
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company', title='Company Revenue') #플롯에 레이블을 추가 (6)
#matplotlib.artist.Artist.set()메서드를 사용하여 이 Axes객체의 속성을 설정할 수 있다.

ax.xaxis.set_major_formatter(currency) # (7)
#matplotlib.artist.Axis.set_major_formatter함수 또는 matplotlib.artist.Axis.set_minor_formatter함수을 함께 사용하는 경우,
#위 함수들은 자동으로 생성하고 matplotlib.ticker.FuncFormatter함수를 사용한다.

plt.show()
