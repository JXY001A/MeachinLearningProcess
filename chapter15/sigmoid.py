from math import exp,log
from scale_data import scaled_car_data
def sigmoid(x):
  return 1/ (1 + exp(-x))


def make_logistic(a,b,c):
  def l(x,p):
    return sigmoid(a * x + b * p - c)
  return l


def point_cost(l,x,p,is_bmw): #1
  wrong = 1 - is_bmw
  return -log(abs(wrong - l(x,p)))

def logistic_cost(a,b,c):
  l = make_logistic(a,b,c)
  errors = [point_cost(l,x,p,is_bmw) for x,p,is_bmw in scaled_car_data]
  return sum(errors)

def simple_logistic_cost(a,b,c):
  l = make_logistic(a,b,c)
  errors = [abs(is_bwm - l(mileage,price)) for mileage,price,is_bwm  in scaled_car_data]
  return sum(errors)
  


# log 函数解决 0.1 与 0.01 之间差异小的，代价不明显的问题。他俩实际精度相差 10 倍，然而数值上相差 0.09（极小）
# def point_cost(l,x,p,is_bwm):
#   wrong =  1 - is_bwm
#   print("abs(wrong - l(x,p))",abs(wrong - l(x,p)))
#   return -log(abs(wrong - l(x,p)))

# def logistic_cost(a,b,c):
#   l = make_logistic(a,b,c)
#   errors = [point_cost(l,mileage,price,is_bwm) for mileage,price,is_bwm  in scaled_car_data]
#   return sum(errors)
    
# print(simple_logistic_cost(0.35,1,0.56))
# print(simple_logistic_cost(1,1,1))

# print(logistic_cost(0.35,1,0.56))
# print(logistic_cost(1,1,1))
