#이미지 향상
#Python Imaging Library는 이미지를 향상시키는 데 사용할 수있는 여러 방법과 모듈을 제공한다.

#필터
#ImageFilter모듈은 filter()메서드로 사용할 수 있는 많은 미리 정의된 강화 필터를 포함한다.

from PIL import ImageFilter
from PIL import Image

#필터 적용
im = Image.open("puppy.jpg")
im.show()
out = im.filter(ImageFilter.DETAIL)
out.show()

#포인트 운영
#point()의 사용은 이미지의 픽셀 값을 변환하는 데 사용할 수 있다. (예 : 이미지 대비 조작)
#대부분의 경우 하나의 인수를 예상하는 함수객체가 이 메서드에 전달 될 수 있다.
#각 픽셀은 해당 기능에 따라 처리된다.

#포인트 변환 적용
# multiply each pixel by 1.2
out = im.point(lambda i: i * 1.2)
#위의 기술을 사용하면 간단한 표현을 이미지에 빠르게 적용할 수 있다.
#point()및 paste()메서드를 결합하여 이미지를 선택적으로 수정할 수도 있다.
out.show()

#개별 밴드 처리
# split the image into individual bands
source = im.split()

R, G, B = 0, 1, 2
# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)
# process the green band
out = source[G].point(lambda i: i * 0.7)
# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)
im.show()

'''
#마스크를 만드는데 사용된 구문에 유의할 것.
imout = im.point(lambda i: expression and 255) #NameError: name 'expression' is not defined에러가 난다. expression문제인듯
#파이썬은 결과를 결정하는 데 필요한 논리 표현식의 일부만 평가하고 표현식의 결과로 조사 된 마지막 값을 반환한다.
#따라서 위의 표현식이 거짓(0)이면 파이썬은 두 번째 피연산자를 보지 않으므로 0을 반환한다.
#그렇지 않으면 255를 반환한다.
print(imout)
'''
