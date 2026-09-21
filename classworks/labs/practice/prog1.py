import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import sample

x = np.linspace(0,5, 11)
x
y = x**3
y

# plt.plot(x, y)
# plt.title("Hello")
# plt.xlabel(" x axis")
# plt.ylabel("y axis")

#first plot

# plt.subplot(2,2, 1)
# plt.plot(x, y)
# plt.subplot(2,2, 2)
# plt.plot(x, y)
# plt.subplot(2,2, 3)
# plt.plot(y, x)
# plt.subplot(2,2, 4)
# plt.plot(x**2, x**2)


fig  = plt.figure(figsize=(20,8), dpi = 100)
axis1 = fig.add_axes([0.5, 0.1, 0.5, 1])
axis1.plot(x,y)


axis2 = fig.add_axes([0.1, 0.1 , 0.5,1])
axis2.plot(x, y)

plt.scatter(x,y)




data = sample(range(1, 10000), 100)
plt.hist(data)


plt.boxplot(x)

#Types of plots





plt.show()