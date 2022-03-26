#특정 예외만 처리
listt = [10, 20, 30]

try:
    index = int(input("인덱스 입력 : "))
    a = int(input("숫자입력 : "))
    print(listt[index] / a)
except ZeroDivisionError:
    print("숫자를 0으로 나누는 것은 불가능 합니다.")
except IndexError:
    print("잘못된 인덱스 입니다.")
#except문은 여러 개 쓸 수 있다.
#특정 예외를 설정하면 그 예외가 발생할 때에 해당 except문을 수행한다.