
test_data = [
    (-1.0, -2.0137862606487387),
    (-0.9, -1.7730222478628337),
    (-0.8, -1.5510125944820812),
    (-0.7, -1.6071832453434687),
    (-0.6, -0.7530149734137868),
    (-0.5, -1.4185018340443283),
    (-0.4, -0.6055579756271128),
    (-0.3, -1.0067254915961406),
    (-0.2, -0.4382360549665138),
    (-0.1, -0.17621952751051906),
    (0.0, -0.12218090884626329),
    (0.1, 0.07428573423209717),
    (0.2, 0.4268795998864943),
    (0.3, 0.7254661223608084),
    (0.4, 0.04798697977420063),
    (0.5, 1.1578103735448106),
    (0.6, 1.5684111061340824),
    (0.7, 1.157745051031345),
    (0.8, 2.1744401978240675),
    (0.9, 1.6380001974121732),
    (1.0, 2.538951262545233)
]

def sum_error(f,data):
  errors = [f(x)-y for (x,y) in data]
  return sum(errors)

def sum_squared_error(f,data):
  errors = [(f(x)-y) ** 2 for (x,y) in data]
  return sum(errors)

def f(x):
  return 2 * x

def g(x):
  return 1-x


# sum_error_f = sum_error(f,test_data)
# sum_error_g = sum_error(g,test_data)
# print('sum_error_f',sum_error_f,'sum_error_g',sum_error_g)

# sum_squared_error_f = sum_squared_error(f,test_data)
# sum_squared_error_g = sum_squared_error(g,test_data)
# print('sum_squared_error_f',sum_squared_error_f,'sum_squared_error_g',sum_squared_error_g)




