# 기본 텍스트 분류

#영화리뷰 텍스트를 긍정 또는 부정으로 분류1.
#이 예제는 binary 또는 class가 두 개인  분류 문제이다.
#이진 분류는 머신러닝에서 중요하고 널리 사용된다.

#여기에서는 인터넷 영화 데이터베이스에서 수집한 50,000개의 영화리뷰 텍스트를 담은 IMDB 데이터셋을 사용하겠다.
#25,000개 리뷰는 훈련용으로, 25,000개는 테스트용으로 나뉘어져 있다.
#훈련 세트와 테스트 세트의 클래스는 균형이 잡혀 있다.
#즉 긍정적인 리뷰와 부정적인 리뷰의 개수가 동일하다.

#이 모델을 만들고 훈련하기 위해 텐서플로의 고수준 파이썬 API인 tf.keras를 사용한다.
import tensorflow as tf
from tensorflow import keras
import numpy as np
#import gzip #파이썬에서 gz 파일의 압축을 풀지 않고 바로 읽을 수 있는 방법
#gb_file = gzip.open(sys.argv[1],'rb')

x = np.__version__
print(x)
print(tf.__version__)

''''''
#IMDB 데이터셋 다운로드
#IMDB 데이터셋은 텐서플로와 함께 제공된다.
#리뷰(단어의 시퀀스(sequence))는 미리 전처리해서 정수 시퀀스로 변환되어 있다.
#각 정수는 어휘사전에 있는 특정단어를 의미한다.

#다음 코드는 IMDB 데이터셋을 컴퓨터에 다운로드한다. (또는 이전에 다운로드 받았다면 캐시된 복사본을 사용한다)
imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
'''Object arrays can not be loaded when allow_pickle = False에러가 발생할 수 있는데 넘파이 버전이 1.16.3보다 높으면 발생한다.'''

#영화리뷰는     X_train에, 감성정보는               y_train에 저장된다.
#테스트용 리뷰는 X_test에, 테스트용 리뷰의 감성정보는 y_test에 저장된다.
#매개변수 num_words=10000은 훈련 데이터에서 가장 많이 등장하는 상위 10,000개의 단어를 선택한다.
#데이터 크기를 적당하게 유지하기 위해 드물게 등장하는 단어는 제외하겠다.

''''''
#데이터 탐색
#잠시 데이터 형태를 알아 보겠다.
#이 데이터셋의 샘플은 전처리된 정수 배열이다.
#이 정수는 영화 리뷰에 나오는 단어를 나타낸다.
#레이블(label)은 정수 0 또는 1이다.
#0은 부정적인 리뷰이고 1은 긍정적인 리뷰이다.
print("훈련 샘플: {}, 레이블: {}".format(len(train_data), len(train_labels)))

#리뷰텍스트는 어휘사전의 특정단어를 나타내는 정수로 변환되어 있다.
#첫 번째 리뷰를 확인해 보자.
print(train_data[0])

#영화 리뷰들은 길이가 다르다.
#다음 코드는 첫 번째 리뷰와 두 번째 리뷰에서 단어의 개수를 출력한다.
#신경망의 입력은 길이가 같아야 하기 때문에 나중에 이 문제를 해결하겠다.
print(len(train_data[0]), len(train_data[1]))

#정수를 다시 텍스트로 변환하는 방법이 있다면 유용할 것이다.
#여기에서는 정수와 문자열을 매핑한 딕셔너리(dictionary)객체에 질의하는 헬퍼(helper)함수를 만들겠다.
#   단어와 정수 인덱스를 매핑한 딕셔너리
#word_index = imdb.get_word_index(path='imdb_word_index.json')
word_index = imdb.get_word_index()

#   처음 몇 개 인덱스는 사전에 정의되어 있습니다
word_index = {k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

#이제 decode_review함수를 사용해 첫 번째 리뷰텍스트를 출력할 수 있다.
print(decode_review(train_data[0]))

