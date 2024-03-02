from bwm_finder import all_car_data
def make_scale(data):
  min_val = min(data)
  max_val = max(data)
  
  def scale(x) :
    return (x-min_val) / (max_val-min_val)
  def un_scale(y) :
    return y * (max_val-min_val) + min_val
  
  return scale,un_scale
  
  
price_scale,price_unscale =  make_scale([x[1] for x in all_car_data])
mile_scale ,mile_unscale =  make_scale([x[0] for x in all_car_data])

scaled_car_data = [(mile_scale(mileage),price_scale(price),is_bwm)  for mileage,price,is_bwm in all_car_data] 




    