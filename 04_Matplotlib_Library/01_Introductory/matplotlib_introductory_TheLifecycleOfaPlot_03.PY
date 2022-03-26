#플롯 저장하기
#플롯의 결과에 만족하므로 이를 디스크에 저장하려고한다. Matplotlib에 저장할 수있는 많은 파일 형식이 있다.
#{'eps': 'Encapsulated Postscript', 'jpg': 'Joint Photographic Experts Group', 'jpeg': 'Joint Photographic Experts Group', 
# 'pdf': 'Portable Document Format', 'pgf': 'PGF code for LaTeX', 'png': 'Portable Network Graphics', 'ps': 'Postscript', 
# 'raw': 'Raw RGBA bitmap', 'rgba': 'Raw RGBA bitmap', 'svg': 'Scalable Vector Graphics', 'svgz': 'Scalable Vector Graphics', 
# 'tif': 'Tagged Image File Format', 'tiff': 'Tagged Image File Format'}

#우리는 그림을 디스크에 저장하기 위해 matplotlib.figure.Figure.savefig()를 사용한다.
'''
아래에 몇 가지 유용한 플래그가 있다.
   - transparent=True 형식이 지원하는 경우 저장된 Figure의 배경을 투명하게 만든다.
   - dpi=80 출력의 해상도(제곱 인치당 도트 수)를 제어힌다.
   - bbox_inches="tight" 그림의 경계를 플롯에 맞춘다.

   ex)
   # Uncomment this line to save the figure.
   # fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
'''
#print(fig.canvas.get_supported_filetypes())