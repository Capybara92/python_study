#색상 변환

#Python Imaging Library를 사용하면 convert()메서드를 사용하여 서로다른 픽셀 표현간에 이미지를 변환 할 수 있다.
from PIL import Image
with Image.open("puppy.jpg") as im:
    im = im.convert("L")
#라이브러리는 지원되는 각 모드와 "L"및 "RGB"모드 간의 변환을 지원한다.
#다른 모드간에 변환하려면 중간이미지(일반적으로 "RGB"이미지)를 사용해야 할 수 있다.
im.show()
