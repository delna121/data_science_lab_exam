import numpy as np
X = np.array([[12,13,14],[1,2,3],[5,6,7]])
Y = np.array([[2,3,6],[4,6,7],[8,9,10]])
Z = np.array([[7,11,2],[6,5,3],[2,5,6]])

a = np.multiply(X,X)
print("X^2=",a)
b = np.multiply(2,Y)
print("2Y=",b)
c = np.multiply(Z,Z)
d = np.multiply(c,Z)
print("Z^3=",d)

print("the final result of X^2 + 2Y + Z^3 is:")
r = np.add(a,b)
s = np.subtract(r,d)
print(s)