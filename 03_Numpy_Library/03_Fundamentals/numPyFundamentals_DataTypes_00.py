#배열유형 및 유형 간 변환_1
#NumPy는 Python보다 훨씬 더 다양한 숫자유형을 지원한다.
#이 섹션에서는 사용 가능한 항목과 배열의 데이터유형을 수정하는 방법을 보여준다.

#지원되는 기본 유형은 C언어의 유형과 밀접하게 연결되어 있다.
'''
Numpy유형	                C 유형	             기술
numpy.bool_	                bool	            바이트로 저장되는 부울 (True 또는 False)
numpy.byte	                signed char	        플랫폼 정의
numpy.ubyte	                unsigned char	    플랫폼 정의
numpy.short	                short	            플랫폼 정의
numpy.ushort	            unsigned short	    플랫폼 정의
numpy.intc	                int	                플랫폼 정의
numpy.uintc	                unsigned int	    플랫폼 정의
numpy.int_	                long	            플랫폼 정의
numpy.uint	                unsigned long	    플랫폼 정의
numpy.longlong	            long long	        플랫폼 정의
numpy.ulonglong	            unsigned long long	플랫폼 정의
numpy.half /                X                   반 정밀도 부동 : 부호 비트, 지수 5 비트, 가수 10 비트
numpy.float16		        X                   반 정밀도 부동 : 부호 비트, 지수 5 비트, 가수 10 비트
numpy.single	            float	            플랫폼 정의 단 정밀도 부동 소수점 : 일반적으로 부호 비트, 8 비트 지수, 23 비트 가수
numpy.double	            double	            플랫폼 정의 배정 밀도 부동 소수점 : 일반적으로 부호 비트, 11 비트 지수, 52 비트 가수.
numpy.longdouble	        long double	        플랫폼 정의 확장 정밀도 부동
numpy.csingle	            float complex	    두 개의 단 정밀도 부동 소수점 (실수 및 허수 성분)으로 표현되는 복소수
numpy.cdouble	            double complex	    두 개의 배정 밀도 부동 소수점 (실수 및 허수 구성 요소)으로 표현되는 복소수.
numpy.clongdouble	        long double complex	두 개의 확장 정밀도 부동 소수점 (실수 및 허수 구성 요소)으로 표시되는 복소수.
'''

#이들 중 대부분은 플랫폼에 따라 정의되기 때문에 고정크기 별칭집합이 제공된다.
'''
Numpy 유형	        C 유형	         기술
numpy.int8	        int8_t	        바이트 (-128 ~ 127)
numpy.int16	        int16_t	        정수 (-32768 ~ 32767)
numpy.int32	        int32_t	        정수 (-2147483648 ~ 2147483647)
numpy.int64	        int64_t	        정수 (-9223372036854775808 ~ 9223372036854775807)
numpy.uint8	        uint8_t	        부호없는 정수 (0 ~ 255)
numpy.uint16	    uint16_t	    부호없는 정수 (0 ~ 65535)
numpy.uint32	    uint32_t	    부호없는 정수 (0 ~ 4294967295)
numpy.uint64	    uint64_t	    부호없는 정수 (0 ~ 18446744073709551615)
numpy.intp	        intptr_t	    인덱싱에 사용되는 정수 (일반적으로 다음과 동일) ssize_t
numpy.uintp	        uintptr_t	    포인터를 담을만큼 큰 정수
numpy.float32	    float	        X
numpy.float64 /     float	        X
numpy.float_	    double	        이것은 내장 파이썬 float 의 정밀도와 일치합니다 .
numpy.complex64	    float complex	두 개의 32 비트 부동 소수점 (실수 및 허수 구성 요소)으로 표시되는 복소수
numpy.complex128 /  float complex	두 개의 32 비트 부동 소수점 (실수 및 허수 구성 요소)으로 표시되는 복소수
numpy.complex_	    double complex	이것은 내장 파이썬 콤플렉스 의 정밀도와 일치합니다 .
'''
