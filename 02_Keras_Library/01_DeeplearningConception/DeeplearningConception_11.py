#학습모델 보기, 저장하기, 불러오기4

#모델 아키텍처 보기
#model_to_dat()함수를 통해 모델 아키텍처를 가시화 시킬 수 있다.
#model 객체를 생성한 뒤라면 언제든지 아래코드를 호출하여 모델 아키텍처를 블록형태로 볼 수 있다.

'''
from IPython.display import SVG #IPython을 다운받으라고 에러가 나옴
from keras.utils.vis_utils import model_to_dot

%matplotlib inline

#pydot 라이브러리가 필요하다고 에러가 나옴(pip설치)
#graphvis 라이브러리가 필요하다고 에러가 나옴(conda설치)
#pydot는 현재 개발이 그쳤고 python3.5 및 3.6에서는 동작하지 않는다.
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))
#그래서 에러가 난다.
'''

#위의 내용의 에러는 스크립트 코드에서 나는 에러이므로, jupyter notebook에서 해보도록 한다.
