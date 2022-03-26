#자신만의 스타일 정의하기
#경로와 스타일시트의 URL과 함께 matplotlib.style.use함수를 호출하여 사용자 정의 스타일을 만들고 사용가능하다.

import matplotlib.pyplot as plt

'''
예를 들어 ./images/presentation.mplstyle파일을 사용하여 만들 수 있다. (파일로 만들어 둔다)
axes.titlesize : 24
axes.labelsize : 20
lines.linewidth : 3
lines.markersize : 10
xtick.labelsize : 16
ytick.labelsize : 16
'''

plt.style.use('./images/presentation.mplstyle')

#또는 <style-name>.mplstyle파일을 mpl_configdir/stylelib에 배치하여 Matplotlib에 스타일을 알릴 수 있다.
#그런다음 style.use(<style-name>)호출하여 사용자 정의 스타일시트를 로드 할 수 있다.
'''plt.style.use(<style-name>)'''


#스타일 작성
#스타일시트는 함께 구성되도록 설계되었습니다.
#따라서 색상을 사용자 정의하는 스타일시트와 프레젠테이션의 요소, 크기를 변경하는 별도의 스타일시트를 가질 수 있다.
#이러한 스타일은 스타일 목록을 전달하여 쉽게 결합 할 수 있다.
plt.style.use(['dark_background', 'presentation']) #오른쪽의 스타일은 왼쪽의 스타일로 이미 정의 된 값을 덮어 쓴다.