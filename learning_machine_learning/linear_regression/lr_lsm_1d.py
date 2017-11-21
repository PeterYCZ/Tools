#python2.7
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
x = 5 * rng.rand(10000, 1)
y = np.array(map(lambda x:4*x-1,x)).T[0]
y[::5] += 3.0 * (0.5 - rng.rand(int(x.shape[0]/5)))
x_mean = np.mean(x)
w = (np.sum(map(lambda x,y:y*(x-x_mean),x,y)))/(np.sum(map(lambda x:x*x,x))-np.sum(x)*np.sum(x)/len(x))
b = np.sum(map(lambda x,y:y-w*x,x,y))/len(x)
y_plot = np.array(map(lambda x:x*w+b,x))
plt.plot(x,y,'r*')
plt.plot(x,y_plot,'b.')
plt.show()
