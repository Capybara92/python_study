#matplotlibrc파일
#Matplotlib는 matplotlibrc구성 파일을 사용하여 'rc 설정'또는 'rc 매개 변수'라고하는 모든 종류의 속성을 사용자 지정한다.
#Matplotlib의 거의 모든 속성(그림 크기 및 DPI, 선, 너비, 색상 및 스타일, 축, 축 및 격자 속성, 텍스트 및 글꼴 속성 등)의 기본값을 제어 할 수 있다.
#style.use('<path>/<style-name>.mplstyle')를 호출하여 URL 또는 경로를 지정하지 않으면,
#Matplotlib는 matplotlibrc를 다음 순서로 4개의 위치에서 찾는다.

    #1. 현재작업 디렉토리의 matplotlibrc은 일반적으로 다른 곳에 적용하지 않으려는 특정 사용자 정의에 사용됩니다.
    #2. $MATPLOTLIBRC이 파일이면, 다른 $MATPLOTLIBRC/matplotlibrc.
    #3. 플랫폼에 따라 사용자 별 위치를 찾는다.
    #   - 리눅스, FreeBSD에서 환경을 사용자정의한 경우 「.config/matplotlib/matplotlibrc　또는 $XDG_CONFIG_HOME/matplotlib/matplotlibrc」
    #   - 다른 플랫폼 에서는 「 .matplotlib/matplotlibrc」
    #   (matplotlib 구성 및 캐시 디렉토리 위치를 참조할것) 
    #4. INSTALL/matplotlib/mpl-data/matplotlibrc의 install은 
    #   리눅스의 위치는 「like /usr/lib/python3.7/site-packages」 윈도우의 위치는는「C:\Python37\Lib\site-packages」일 것이다.
    #   matplotlib를 설치할 때마다 이 파일을 덮어 쓰므로 사용자 정의를 저장하려면 이 파일을 사용자 별 matplotlib디렉토리로 이동해야 한다.
    #   「/usr/lib/python3.7/site-packagesC:\Python37\Lib\site-packages」

#matplotlibrc파일이 발견 되면 다른 경로를 검색하지 않는다.
#현재 활성중인 matplotlibrc파일이 로드 된 위치를 표시하려면 다음을 수행 할 수 있다.
'''
 import matplotlib
 matplotlib.matplotlib_fname() #'/home/foo/.config/matplotlib/matplotlibrc'
'''
