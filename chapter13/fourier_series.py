from math import cos,sin,pi,sqrt
from draw import *
import matplotlib.pyplot as plt


def const(t):
  return 1

# def fourier_series(a0,a,b):
#   def result(t):
#     cos_terms = [an * cos(2 * pi *(n+1) * t ) for (n,an)   in  enumerate(a)]
#     sin_terms = [bn * sin(2 * pi *(n+1) * t ) for (n,bn)   in  enumerate(b)]

#     return a0 * const(t) + sum(cos_terms) + sum(sin_terms)
#   return  result


def fourier_series(a0,a,b):
    def result(t):
        cos_terms = [an*cos(2*pi*(n+1)*t) for (n,an) in enumerate(a)] #<1>
        sin_terms = [bn*sin(2*pi*(n+1)*t) for (n,bn) in enumerate(b)] #<2>
        return a0*const(t) + sum(cos_terms) + sum(sin_terms) #<3>
    return result
# f1 = fourier_series(0,[],[4/pi])
# f2 = fourier_series(0,[],[4/pi,0,4/(3*pi)])

# b3 = [4/(pi * n) if n%2!=0 else 0 for n in range(1,10) ]
# f3 = fourier_series(0,[],b3)

# b4 = [4/(pi * n) if n%2!=0 else 0 for n in range(1,100) ]
# f4 = fourier_series(0,[],b4)


# plot_function(f1,0,3)
# plot_function(f2,0,3)
# plot_function(f3,0,3)
# plot_function(f4,0,3)


# plt.show()

