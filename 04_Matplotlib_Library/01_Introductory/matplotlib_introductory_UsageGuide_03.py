import matplotlib.pyplot as plt
import numpy as np

#Backends(백엔드)
#matplotlib은 다양한 사례와 출력형식을 대상으로한다.
#이러한 모든 사례를 지원하기 위해 서로 다른 출력을 대상으로 할 수 있으며 이 기능을 「백엔드」라고 한다.
#「프론트엔드」는 사용자가 직면하는 코드이며, 「백엔드」 는 화면뒤에서 모든 힘든일을 한다.
#백엔드에는 2가지 유형이 있다.
#「사용자 인터페이스 백엔드」(pygtk, wxpython, tkinter, qt4 또는 macosx에서 사용; "대화 형 백엔드"라고도 함)
#이미지 파일을 만들기 위한「하드 카피 백엔드」(PNG, SVG, PDF, PS; "비대화 형 백엔드"라고도 함)

#백엔드를 구성하는 3가지 방법
'''
1. The rcParams["backend"] (default: 'agg') parameter in your matplotlibrc file
2. The MPLBACKEND environment variable
3. The function matplotlib.use()

백엔드가 명시 적으로 설정되지 않은 경우 Matplotlib는 시스템에서 사용할 수있는 항목과 GUI 이벤트 루프가 이미 실행 중인지 여부에 따라 사용 가능한 백엔드를 자동으로 감지합니다. 
Linux에서 환경 변수가 DISPLAY 설정되지 않은 경우 "이벤트 루프"는 "헤드리스"로 식별되어 비대화 형 백엔드 (agg)로 대체됩니다.
'''
import matplotlib
matplotlib.use('qt5agg')
#이 작업은 그림을 만들기 전에 수행해야합니다. 그렇지 않으면 Matplotlib가 백엔드를 전환하지 못하고 ImportError가 발생할 수 있습니다.
#「use」를 사용하여 사용자가 다른 백엔드를 사용하려면 코드에서 변경이 필요합니다. 따라서 절대적으로 「use」가 필요한 경우가 아니면 명시 적으로 호출 하지 않아야합니다.

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

fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

plt.show()