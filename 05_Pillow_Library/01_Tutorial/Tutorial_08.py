#이미지 시퀀스

#Python Imaging Library에는 이미지시퀀스(애니메이션 형식이라고도 함)에 대한 몇 가지 기본 지원이 포함되어 있다.
#지원되는 시퀀스 형식에는 FLI / FLC, GIF 및 몇가지 실험적 형식이 포함된다.
#TIFF 파일에는 두 개 이상의 프레임이 포함될 수도 있다.

#시퀀스파일을 열면 PIL은 시퀀스의 첫 번째 프레임을 자동으로 로드한다.
#seek 및 tell 메서드를 사용하여 다른 프레임 사이를 이동할 수 있다.

#시퀀스 읽기
from PIL import Image

'''
with Image.open("puppy.jpg") as im:
    im.seek(1) # skip to the second frame

    try:
        while 1:
            im.seek(im.tell()+1)
            # do something to im
    except EOFError:
        pass # end of sequence
'''
#이 예에서 볼 수 있듯이 EOFError시퀀스가 종료되면 예외가 발생한다.
#다음 클래스를 사용하면 for 문을 사용하여 시퀀스를 반복 할 수 있다.

#ImageSequence Iterator 클래스 사용
from PIL import ImageSequence
for frame in ImageSequence.Iterator(im):
    # ...do something to frame...