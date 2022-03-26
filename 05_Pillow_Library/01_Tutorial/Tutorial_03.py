#이미지 잘라내기, 붙여넣기, 병합

#이 Image클래스에는 이미지 내의 영역을 조작 할 수있는 메서드가 포함되어 있다.
#이미지에서 하위 직사각형을 추출하려면 crop()방법을 사용한다.

from PIL import Image
im = Image.open("puppy.jpg")

#이미지에서 하위 직사각형 복사
box = (100, 100, 400, 400)
region = im.crop(box)
#영역은 좌표가(왼쪽, 위쪽, 오른쪽, 아래쪽)인 4-튜플로 정의된다.
#Python Imaging Library는 왼쪽 상단 모서리에 (0, 0)이 있는 좌표계를 사용한다.
#또한 좌표는 픽셀사이의 위치를 ​​나타내므로 위 예제의 영역은 정확히 300x300 픽셀이다.
region.show()

#하위 직사각형을 처리하고 다시 붙여 넣기
region = region.transpose(Image.ROTATE_180) #위에서 지정한 영역(300x300)부분이 180도 회전한다.
im.paste(region, box)
#영역을 다시 붙여 넣을 때 영역의 크기는 지정된영역과 정확히 일치해야한다.
#또한 영역은 이미지 외부로 확장 할 수 없다. 
#그러나 원본 이미지의 모드와 영역이 일치 할 필요는 없다.
#그렇지 않으면 붙여넣기 전에 영역이 자동으로 변환된다.
region.show()

#이미지 롤링
def roll(image, delta):
    """Roll an image sideways."""
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image
#고급 트릭을 위해 paste메서드는 투명 마스크를 선택적 인수로 사용할 수도 있다.
#이 마스크에서 값 255는 붙여넣은 이미지가 해당 위치에서 불투명 함을 나타낸다. (즉, 붙여 넣은 이미지를있는 그대로 사용해야 함)
#값 0은 붙여 넣은 이미지가 완전히 투명 함을 의미한다.
#사이의 값은 서로 다른 투명도 수준을 나타낸다.
#예를 들어 RGBA 이미지를 붙여넣고 이를 마스크로 사용하면 이미지의 불투명 한 부분은 붙여넣지만 투명한 배경은 붙여지지 않는다.

#Python Imaging Library를 사용하면 RGB 이미지와 같은 다중대역 이미지의 개별대역으로 작업 할 수도 있다.
#분할방법은 각각 원본 다중 대역 이미지에서 하나의 대역을 포함하는 새 이미지 세트를 만든다.
#merge 함수는 모드와 이미지 튜플을 가져 와서 새로운 이미지로 결합합니다. 다음 샘플은 RGB 이미지의 세 밴드를 바꾼다.

#밴드 분할 및 병합
r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))
#단일 대역(single-band) 이미지의 경우, split()는 이미지 자체를 반환한다.
#개별 색상 밴드로 작업하려면 먼저 이미지를 "RGB"로 변환 할 수 있다.
im.show()
