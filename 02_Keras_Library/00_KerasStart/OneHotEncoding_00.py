#원-핫 인코딩(One-Hot Encoding)이란?

#원-핫 인코딩은 단어집합의 크기를 벡터의 차원으로 하고, 표현하고 싶은 단어의 인덱스에 1의 값을 부여하고, 다른 인덱스에는 0을 부여하는 단어의 벡터 표현방식이다.
#이렇게 표현된 벡터를 원-핫 벡터(One-Hot vector)라고 한다.

#원-핫 인코딩을 두 가지 과정으로 정리해보겠다.
#   (1) 각 단어에 고유한 인덱스를 부여한다. (정수 인코딩)
#   (2) 표현하고 싶은 단어의 인덱스의 위치에 1을 부여하고, 다른 단어의 인덱스의 위치에는 0을 부여한다.

#이해를 돕기 위해서 한국어 문장을 예제로 원-핫 벡터를 만들어보겠다.
#   ex) 나는 자연어 처리를 배운다
#위 문장에 대해서 원-핫 인코딩을 진행하는 코드는 아래와 같다.

from konlpy.tag import Okt  
okt=Okt()
#JVMNotFoundException No JVM shared library file (jvm.dll) found. Try setting up the JAVA_HOME environment variable properly. 에러발생
#jdk를 다운받고 환경변수를 설정해 줘야함.

#SystemError java.nio.file.InvalidPathException: Illegal char <*> at index 105: C:\Users\ALJP1B901504\AppData\Local\Continuum\anaconda3\envs\python_3_6_12\lib\site-packages\konlpy\java\*
#에러가 발생함. (이유를 모르겠음)

token=okt.morphs("나는 자연어 처리를 배운다")  
print(token)
# -> ['나', '는', '자연어', '처리', '를', '배운다']

#코엔엘파이의 Okt 형태소 분석기를 통해서 우선 문장에 대해서 토큰화를 수행
word2index={}
for voca in token:
     if voca not in word2index.keys():
       word2index[voca]=len(word2index)
print(word2index)
# -> {'나': 0, '는': 1, '자연어': 2, '처리': 3, '를': 4, '배운다': 5}  
#각 토큰에 대해서 고유한 인덱스(index)를 부여하였다.
#지금은 문장이 짧기 때문에 각 단어의 빈도수를 고려하지 않지만, 빈도수 순대로 단어를 정렬하여 고유한 인덱스를 부여하는 작업이 사용되기도 한다.

#토큰을 입력하면 해당 토큰에 대한 원-핫 벡터를 만들어내는 함수
def one_hot_encoding(word, word2index):
       one_hot_vector = [0]*(len(word2index))
       index=word2index[word]
       one_hot_vector[index]=1
       return one_hot_vector

one_hot_encoding("자연어",word2index)
# -> [0, 0, 1, 0, 0, 0] 

