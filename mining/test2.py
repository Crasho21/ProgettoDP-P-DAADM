from numpy import *

a = zeros(300000, int8)

a[0] = 1
a[1] = 2

print(" ".join(map(str,a)))

