import matplotlib.pyplot as plt
from plot_data import plot_data
from bwm_finder import all_car_data
from plot_line import plot_line
from scale_data import scaled_car_data
from gradient_descent3 import gradient_descent3
from sigmoid import logistic_cost



# plot_line(0.21114493446923963, 5.045439729273302, 2.126012256718192)
# plot_line(2.3698636484640563, 9.058605425515704, 4.304514392219305) 
# plot_line(3.2618570654952186, 10.59208516572984, 5.148433450185792) 
# plot_line(3.6547770641288095, 11.307339973895745, 5.535181952652802)
# plot_line(3.716521771742557, 11.42173088189173, 5.596700199993904) 
# plot_line(3.716700420305167, 11.42206260708127, 5.596878473105733)


plot_data(scaled_car_data)
for i in range(0,1000,100):
    a,b,c = gradient_descent3(logistic_cost,1,1,1,max_steps=i)
    plot_line(a,b,c,alpha=i/1000,c='k')

# plot_data(all_car_data)
plt.show()