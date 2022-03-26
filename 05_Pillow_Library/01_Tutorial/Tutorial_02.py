#이미지 읽기 및 쓰기 ??????????????????????????????????????????????????????????????????

#Python Imaging Library는 다양한 이미지 파일 형식을 지원한다.
#디스크에서 파일을 읽으려면 Image모듈 의 open()기능을 사용한다.
#파일을 열기 위해 파일형식을 몰라도된다.
#라이브러리는 파일내용에 따라 형식을 자동으로 결정한다.

#파일을 저장하려면 Image클래스 의 save()메소드를 사용한다.
#파일을 저장할 때 이름이 중요해진다.
#형식을 지정하지 않으면 라이브러리는 파일이름 확장자를 사용하여 사용할 파일 저장형식을 찾는다.

#파일을 JPEG로 변환
'''
import os, sys
from PIL import Image
im = Image.open("puppy.jpg")

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)
'''
#두 번째 인수는 save() 파일형식을 명시적으로 지정하는 메서드에 제공 될 수 있다.
#비표준 확장을 사용하는 경우 항상 다음과 같이 형식을 지정해야한다.

#JPEG 축소판 만들기
'''
import os, sys
from PIL import Image
im = Image.open("puppy.jpg")

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)
'''
#실제로 필요한 경우가 아니면 라이브러리가 래스터 데이터를 디코딩하거나 로드하지 않는다는 점에 유의해야한다.
#파일을 열 때 파일형식을 결정하고 파일을 디코딩하는데 필요한 모드, 크기 및 기타 속성과 같은 항목을 추출하기 위해 파일헤더를 읽지만 나머지 파일은 나중에 처리되지 않는다.
#즉, 이미지 파일을 여는것은 파일 크기 및 압축 유형에 관계없이 빠른 작업이다. 
#다음은 이미지 파일 집합을 빠르게 식별하는 간단한 스크립트이다.

#이미지 파일 식별
'''
import sys
from PIL import Image
im = Image.open("puppy.jpg")

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass
'''
