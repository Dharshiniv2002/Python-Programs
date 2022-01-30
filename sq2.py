import math
def newtonsquareroot(n,howmany):
    approx=0.5*n
for i in range(howmany):
    betterapprox=0.5*(approx+n/approx)
    approx=betterapprox
    return betterapprox
print("Squaring of two roots by newtons method: ",newtonsqrt(10,10))
