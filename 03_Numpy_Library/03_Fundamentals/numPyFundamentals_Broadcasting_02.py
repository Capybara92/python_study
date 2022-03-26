#실제 방송의 예1.

import numpy as np

x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3,4))

print(x.shape)
print()
print(y.shape)
print()
#print(x + y) # ValueError: operands could not be broadcast together with shapes (4,) (5,)
print(xx.shape)
print()
print(y.shape)
print()
print((xx + y).shape)
print()
print(xx + y)
print()
print(x.shape)
print()
print(z.shape)
print()
print((x + z).shape)
print()
print(x + z)
