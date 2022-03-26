import matplotlib.pyplot as plt
import numpy as np

#일반적으로 동일한 플롯을 반복해서 작성하지만 데이터 세트가 다르기 때문에 플로팅을 수행하기 위해 특수 함수를 작성해야합니다. 
#권장되는 함수 서명은 다음과 같습니다.
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

#그러면 다음과 같이 사용할 수 있습니다.

data1, data2, data3, data4 = np.random.randn(4, 100)

'''
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

plt.show()
'''

#또는 2 개의 서브 플롯을 원할 경우

fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

plt.show()
#이 간단한 예제의 경우이 스타일은 과잉처럼 보이지만 그래프가 약간 더 복잡해지면 효과가 있습니다.