from car_data import bmws,priuses

def bwm_finder(mileage,price):
  if price > 25000 :
    return 1 
  else:
    return 0;
  
  
all_car_data = []

for bmw in bmws:
  all_car_data.append((bmw.mileage,bmw.price,1))


for priuse in priuses:
  all_car_data.append((priuse.mileage,priuse.price,0))
  

def test_classifier(classifier,data):
  true_count = 0
  false_count = 0
  
  for mileage,price,is_bwm in data :
    if classifier(mileage,price) == is_bwm :
      true_count +=1
    else :
      false_count +=1
  
  return true_count/(true_count+false_count)

