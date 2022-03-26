#기하학적 변환(Geometrical transforms)

#PIL.Image.Image클래스는 이미지에 resize()와 rotate()메서드를 포함한다. 
#전자는 새로운 크기를 제공하는 튜플을 취하고, 후자는 시계 반대 방향으로 각도를 지정한다.
from PIL import Image
im = Image.open("puppy.jpg")

#간단한 형상 변환(Simple geometry transforms)
out = im.resize((128, 128))
out = im.rotate(45) # degrees counter-clockwise
#이미지를 90도 단계로 회전하려면 rotate()방법 또는 transpose()방법을 사용할 수 있다.
#후자는 가로 또는 세로 축을 중심으로 이미지를 뒤집는 데 사용할 수도 있다.
out.show()

#이미지 조옮김(Transposing an image)
out = im.transpose(Image.FLIP_LEFT_RIGHT)
out.show()
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out.show()
out = im.transpose(Image.ROTATE_90)
out.show()
out = im.transpose(Image.ROTATE_180)
out.show()
out = im.transpose(Image.ROTATE_270)
out.show()
#expand플래그가 TRUE라면, 이미지 크기에 동일한 변경을 제공하기 위해, rotate()작업을 transpose(ROTATE)작업과 동일하게 수행 할 수도 있다. 
#보다 일반적인 형태의 이미지변환은 transform()방법을 통해 수행 할 수 있다.
