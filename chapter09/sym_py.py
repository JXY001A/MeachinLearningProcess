from sympy import * 
from sympy.core.core import *


y = Symbol('y')
x = Symbol('x')
formula = Mul(y,Add(3,x))
formula2 = y*(x+3)
# sub 表示： 将表达式 formula2 中的 x 使用常数 1 代替，并返回化简后的新表达式
formula3 = formula2.subs(x,1)
print(formula3);

# diff 表示：对表达式 x**2 基于 x 求对应导数
formula4 = (x ** 2).diff(x);
print(formula4)


# integrate 表示：对表达式 3*x**2 进行积分
formula5 = (3*x**2).integrate(x);
print(formula5)