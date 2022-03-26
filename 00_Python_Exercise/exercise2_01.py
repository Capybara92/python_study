#자료형
#파이썬의 자료형에는 숫자형, 문자열, 리스트, 튜플, 딕셔너리, 집합이 있다.

#숫자형(정수형, 실수형, 2진수, 8진수, 16진수)

#정수형
num1 = 11.4 #실수형
str1 = "81" #문자형
print(int(num1)) #int로 형변환
print(int(str1)) #int로 형변환

#실수형
num1 = 11    #정수형
num2 = "5.4" #문자형
print(float(num1)) #int로 형변환
print(float(num2)) #int로 형변환

num3 = 0.0314e2 #다른방법의 실수형 표현 3.14
num4 = 901E-3   #다른방법의 실수형 표현 0.901
print(num3)
print(num4)

#2진수(접두어 0b 혹은 0B)
num1 = 0b10101
num2 = 0B1101
print(num1) #10진수로
print(num2) #10진수로

num1 = 107
num2 = 51
print(bin(num1)) #2진수로(※문자형 형태) 0b1101011
print(bin(num2)) #2진수로(※문자형 형태) 0b110011

#8진수(접두어 0o 혹은 0O)
num1 = 0o473
num2 = 0O107
print()
print(num1) #10진수로
print(num2) #10진수로

num1 = 87      #10진수
num2 = 0b10101 #2진수
num3 = 0xF3    #16진수
print(oct(num1)) #8진수로(※문자형 형태) 0o127
print(oct(num2)) #8진수로(※문자형 형태) 0o25
print(oct(num3)) #8진수로(※문자형 형태) 0o363

#16진수(접두어0x 혹은 0X)
num1 = 0xF29
num2 = 0XAB5
print(num1) #10진수로
print(num2) #10진수로

num1 = 15    #10진수
num2 = 0B100 #2진수
num3 = 0o32  #8진수
print(hex(num1)) #16진수로(※문자형 형태) 0xf
print(hex(num2)) #16진수로(※문자형 형태) 0x4
print(hex(num3)) #16진수로(※문자형 형태) 0x1a