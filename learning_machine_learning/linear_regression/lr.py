import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model

x = np.array([range(100),range(100)])
noise = np.random.uniform(-10.0, 10.0, 100)
y = x[0]+noise
lr = linear_model.LinearRegression()
predicted = cross_val_predict(lr, x.T, y)

fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()],"r",lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()


