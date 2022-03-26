#확장 정밀도(Extended Precision)

'''
Python’s floating-point numbers are usually 64-bit floating-point numbers, nearly equivalent to np.float64. 
In some unusual situations it may be useful to use floating-point numbers with more precision. 
Whether this is possible in numpy depends on the hardware and on the development environment: specifically, 
x86 machines provide hardware floating-point with 80-bit precision, and while most C compilers provide this as their long double type, 
MSVC (standard for Windows builds) makes long double identical to double (64 bits). 
NumPy makes the compiler’s long double available as np.longdouble (and np.clongdouble for the complex numbers). 
You can find out what your numpy provides with np.finfo(np.longdouble).

NumPy does not provide a dtype with more precision than C’s long double\; 
in particular, the 128-bit IEEE quad precision data type (FORTRAN’s REAL*16\) is not available.

For efficient memory alignment, np.longdouble is usually stored padded with zero bits, either to 96 or 128 bits. 
Which is more efficient depends on hardware and development environment; 
typically on 32-bit systems they are padded to 96 bits, while on 64-bit systems they are typically padded to 128 bits. 
np.longdouble is padded to the system default; np.float96 and np.float128 are provided for users who want specific padding. 
In spite of the names, np.float96 and np.float128 provide only as much precision as np.longdouble, 
that is, 80 bits on most x86 machines and 64 bits in standard Windows builds.

Be warned that even if np.longdouble offers more precision than python float, it is easy to lose that extra precision, 
since python often forces values to pass through float. 
For example, the % formatting operator requires its arguments to be converted to standard python types, 
and it is therefore impossible to preserve extended precision even if many decimal places are requested. 
It can be useful to test your code with the value 1 + np.finfo(np.longdouble).eps.
'''
