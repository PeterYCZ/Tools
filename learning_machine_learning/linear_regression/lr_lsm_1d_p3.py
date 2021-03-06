#python3.5
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
x = 5 * rng.rand(10000, 1)
y = np.array(list(map(lambda x:4*x-1,x))).T[0]#different place,python2's map() return list and python3's map() return iter.
y[::5] += 3.0 * (0.5 - rng.rand(int(x.shape[0]/5)))
x_mean = np.mean(x)
w = (np.sum(list(map(lambda x,y:y*(x-x_mean),x,y))))/(np.sum(list(map(lambda x:x*x,x)))-np.sum(x)*np.sum(x)/len(x))
b = np.sum(list(map(lambda x,y:y-w*x,x,y)))/len(x)
y_plot = np.array(list(map(lambda x:x*w+b,x)))
plt.plot(x,y,'r*')
plt.plot(x,y_plot,'b.')
plt.show()
