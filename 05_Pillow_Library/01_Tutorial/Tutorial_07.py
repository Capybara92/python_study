#상승

#고급 이미지 향상을 위해 ImageEnhance모듈의 클래스를 사용할 수 있다.
#이미지를 만든 후에는 향상 개체를 사용하여 다른설정을 빠르게 시도할 수 있다.
#대비, 밝기, 색상 균형 및 선명도를 조정할 수 있다.

#이미지 향상
from PIL import Image
from PIL import ImageEnhance

im = Image.open("puppy.jpg")
im.show()

enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
