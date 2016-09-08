from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

i = 0.025
C = 10000
t = 0.5

FV = C*(1+i*t)

print FV

x=np.linspace(0,1,100)
y = C*(1+i*x)
plt.cla()
plt.grid()
plt.plot(x, y)
plt.show()
