#학습과정 살펴보기2

#텐서보드와 연동하기
#텐서보드는 머신러닝 실험에 필요한 시각화 및 도구를 제공한다.
#   - 손실 및 정확도와 같은 측정항목 추적 및 시각화
#   - 모델 그래프(작업 및 레이어) 시각화
#   - 시간의 경과에 따라 달라지는 가중치, 편향, 기타 텐서의 히스토그램 확인
#   - 저차원 공간에 임베딩 투영
#   - 이미지, 텍스트, 오디오 데이터 표시
#   - TensorFlow 프로그램 프로파일링
#   - 그 외 다양한 도구

#텐서플로우에서는 텐서보드라는 훌륭한 학습과정 모니터링 툴을 제공하고 있다.
#텐서플로우 기반으로 케라스를 구동할 경우 이 텐서보드를 사용할 수 있다.
#따라서 텐서보드를 이용하기 위해서는 먼저 백엔드를 케라스 설정 파일(keras.json)에서 텐서플로우로 지정해야 한다.
'''
{
    "image_data_format": "channels_last",
    "epsilon": 1e-07,
    "floatx": "float32",
    "backend": "tensorflow"
}
'''
#여기서 중요한 인자는 backend이 이다.
#이 항목이 tensorflow로 지정되어 있어야 한다. 연동하는 방법은 간단하다.
#TensorBoard라는 콜백함수를 생성한 뒤 fit 함수인자로 넣어주기만 하면 된다.
#TensorBoard 콜백함수 생성 시 log_dir 인자에 경로를 넣어야 하는데, 이 경로에 텐서보드와 정보를 주고 받을 수 있는 파일이 생성된다.
'''
tb_hist = keras.callbacks.TensorBoard(log_dir='./graph', histogram_freq=0, write_graph=True, write_images=True)
model.fit(X_train, Y_train, epochs=1000, batch_size=10, validation_data=(X_val, Y_val), callbacks=[tb_hist])
'''


''''''
#예제코드는 DeeplearningConception_02.py와 같다.

''''''
#TensorBoard 콜백함수 생성 시 logdir 인자로 지정한 로컬의 graph라는 폴더 안을 보면 events로 시작하는 파일이 생성되는 것을 확인 할 수 있다.
#콘솔에서 아래 명령으로 텐서보드를 실행한다.
#여기서 주의할 사항은 –logdir 인자에는 graph 폴더의 절대경로로 지정해야 한다.
'''
tensorboard --logdir=~/Projects/Keras/_writing/graph
'''

#위 명령을 실행하면 아래와 같은 메시지를 볼 수 있다.
'''
Starting TensorBoard 41 on port 6006
(You can navigate to http://169.254.225.177:6006)
'''

#웹 브라우저에 메시지에 표시된 주소를 입력하면 텐서보드를 볼 수 있다.
