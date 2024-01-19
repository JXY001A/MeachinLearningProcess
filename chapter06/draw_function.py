#  TODO: 暂时无法运行不知道原因！！！
from plot import plot;
from math import sin;
def f(x):
    return 0.5 * x + 3
def g(x):
    return sin(x)
plot([f,g],-10,10)