#라인 속성 제어하기
#라인 속성에는 여러가지가 있습니다. (linewidth, dash style, antialiased 등)
#참조) matplotlib.lines.Line2D

#키워드 인수 사용
#ex) plt.plot(x, y, linewidth=2.0)

#Line2D인스턴스의 setter 메서드를 사용한다 . plot는 Line2D객체의 목록을 반환한다. 
#ex) line, = plt.plot(x, y, '-') #We use tuple unpacking with line, to get the first element of that list
#    line.set_antialiased(False) #turn off antialiasing

#matplotlib.pyplot.step 사용.
#아래 예제에서는 MATLAB 스타일 함수를 사용하여 행 목록에 여러 속성을 설정합니다. 
#setp개체 목록 또는 단일 개체와 투명하게 작동합니다.
#python 키워드 인수 또는 MATLAB 스타일 문자열 / 값 쌍을 사용할 수 있습니다.
#ex) lines = plt.plot(x1, y1, x2, y2)           # use keyword args
#    plt.setp(lines, color='r', linewidth=2.0)  # or MATLAB style string value pairs
#    plt.setp(lines, 'color', 'r', 'linewidth', 2.0)


'''
특성(Property)	            값 유형(Value Type)
alpha	                    float
animated	                [True | False]
antialiased or aa	        [True | False]
clip_box	                a matplotlib.transform.Bbox instance
clip_on	                    [True | False]
clip_path	                a Path instance and a Transform instance, a Patch
color or c	                any matplotlib color
contains	                the hit testing function
dash_capstyle	            ['butt' | 'round' | 'projecting']
dash_joinstyle	            ['miter' | 'round' | 'bevel']
dashes	                    sequence of on/off ink in points
data	                    (np.array xdata, np.array ydata)
figure	                    a matplotlib.figure.Figure instance
label	                    any string
linestyle or ls	            [ '-' | '--' | '-.' | ':' | 'steps' | ...]
linewidth or lw	            float value in points
marker	                    [ '+' | ',' | '.' | '1' | '2' | '3' | '4' ]
markeredgecolor or mec	    any matplotlib color
markeredgewidth or mew	    float value in points
markerfacecolor or mfc	    any matplotlib color
markersize or ms	        float
markevery	                [ None | integer | (startind, stride) ]
picker	                    used in interactive line selection
pickradius	                the line pick selection radius
solid_capstyle	            ['butt' | 'round' | 'projecting']
solid_joinstyle	            ['miter' | 'round' | 'bevel']
transform	                a matplotlib.transforms.Transform instance
visible	                    [True | False]
xdata	                    np.array
ydata	                    np.array
zorder	                    any number
'''