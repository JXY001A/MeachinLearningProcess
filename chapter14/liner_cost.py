from sum_f import sum_squared_error
from car_data import priuses
from math import sqrt,exp
import matplotlib.pyplot as plt
import numpy as np


prius_mileage_price = [(p.mileage, p.price) for p in priuses]



def length(v):
  return sqrt(sum([coord ** 2 for coord in v]))

def secant_slope(f,xmin,xmax):
  return (f(xmax) - f(xmin)) / (xmax-xmin)

def approx_derivative(f,x,dx=1e-6):
  return secant_slope(f,x-dx,x+dx)

def approx_gradient(f,x0,y0,dx=1e-6):
  partial_x = approx_derivative(lambda x: f(x,y0),x0,dx=dx)
  partial_y = approx_derivative(lambda y: f(x0,y),y0,dx=dx)
  
  return (partial_x,partial_y);




def gradient_descent(f,xstart,ystart,tolerance=1e-6):
  x = xstart
  y = ystart
  grad = approx_gradient(f,x,y)
  while length(grad) > tolerance:
    x -= 0.01 * grad[0]
    y -= 0.01 * grad[1]
    grad = approx_gradient(f,x,y)
  return x,y
  
# def gradient_ascent(f,x_start,y_start,tolerance=1e-6):
#   x = x_start
#   y = y_start
  
#   grad = approx_gradient(f,x,y)
  
#   while length(grad) > tolerance:
#     x += grad[0]
#     y += grad[1]
#     grad = approx_gradient(f,x,y)
    
#   return x,y


def coefficient_cost(a,b):
  def f(x):
    return a * x + b
  return sum_squared_error(f,prius_mileage_price)

def exp_coefficient_cost(q,r):
  def f(x):
    return q * exp(r*x)
  return sum_squared_error(f,prius_mileage_price)


def scaled_cost_function(c,d):
  # 0.5 至少每公里折损 0.5 分前（预估）
  # 5000 表示 0 公里车程的车最大值 5w 
  # 提供呢以上两个预估参数的目的是减少计算；及将 c 限制在 小于 1 的范围内，这样讲大幅降低计算量；同时除以 1e13 则是防止数据过大超出最大范围
  return coefficient_cost(0.5 * c , 50000 * d) / 1e13


def scaled_exp_coefficient_cost(s,t):
  return exp_coefficient_cost(30000 * s,t * 1e-4) / 1e11


# 梯度下降线性训练 : 其中 c,d 为线性模型最佳参数
# c,d = gradient_descent(scaled_cost_function,0,0)

# 梯度下降非线形训练: 其中 s,t 为指数模型最佳参数
# s,t = gradient_descent(scaled_exp_coefficient_cost,0,0)



def plot_mileage_price(cars):
    prices = [c.price for c in cars]
    mileages = [c.mileage for c in cars]
    plt.scatter(mileages, prices, alpha=0.5)
    plt.ylabel("Price ($)",fontsize=16)
    plt.xlabel("Odometer (mi)",fontsize=16)
    
def plot_function(f,xmin,xmax,**kwargs):
    ts = np.linspace(xmin,xmax,1000)
    plt.plot(ts,[f(t) for t in ts],**kwargs)

def p(x):
  c = -0.1211190178116973 
  d = 0.3149542288803843
  a = 0.5 * c
  b = 50000 * d;
  return a*x + b

def k(x):
  s = 0.6235404892844091 
  t = -0.07686877731083401
  q = 30000 * s
  r = t * 1e-4
  return q * exp(r*x)

plot_mileage_price(priuses)
plot_function(p,0,350000,c='k')
plot_function(k,0,350000,c='k')
plt.show()