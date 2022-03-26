#이미지 읽기에 대한 추가 정보

#앞에서 설명한 것처럼 Image모듈의 open()함수는 이미지 파일을 여는 데 사용된다.
#대부분의 경우 파일이름을 인수로 전달하기만 하면된다.
#Image.open()컨텍스트 관리자로 사용할 수 있다.

from PIL import Image
with Image.open("puppy.jpg") as im:
#모든 것이 잘되면 결과는 PIL.Image.Image객체이다.
#그렇지 않으면 OSError예외가 발생한다.
#파일이름 대신 파일과 유사한 객체를 사용할 수 있다.
#개체는 file.read, file.seek및 file.tell메서드를 구현해야 하며 이진모드에서 열어야 한다.

#열린 파일에서 읽기
'''
from PIL import Image
with open("hopper.ppm", "rb") as fp:
    im = Image.open(fp)
'''

#이진 데이터에서 읽기
'''
from PIL import Image
import io
im = Image.open(io.BytesIO(buffer))
#라이브러리 seek(0)는 이미지 헤더를 읽기 전에 파일을 되감는다.(사용)
#또한 이미지 데이터를 읽을 때도 검색이 사용된다. (로드 방법에 의해) 
'''

#tar 아카이브에서 읽기
'''
from PIL import Image, TarIO

fp = TarIO.TarIO("Tests/images/hopper.tar", "hopper.jpg")
im = Image.open(fp)
'''