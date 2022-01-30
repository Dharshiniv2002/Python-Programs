import math
def newtonsquareroot(n,howmany):
 approx=0.5*n
for i in range(howmany):
    betterapprox=0.5*(approx+n/approx)
    approx =betterapprox
rprint("squareroot of newton's square root: ",newtonsqrt(10,10))
