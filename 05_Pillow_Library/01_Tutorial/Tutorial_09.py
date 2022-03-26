#PostScript 인쇄

#Python Imaging Library에는 PostScript 프린터에서 이미지, 텍스트, 그래픽을 인쇄하는 기능이 포함되어 있다.
#다음은 간단한 예.

#PostScript 그리기
from PIL import Image
from PIL import PSDraw

with Image.open("puppy.jpg") as im:
    title = "puppy"
    box = (1*72, 2*72, 7*72, 10*72) # in points

    ps = PSDraw.PSDraw() # default is sys.stdout
    ps.begin_document(title)

    # draw the image (75 dpi)
    ps.image(box, im, 75)
    ps.rectangle(box)

    # draw title
    ps.setfont("HelveticaNarrow-Bold", 36)
    ps.text((3*72, 4*72), title)

    ps.end_document()
