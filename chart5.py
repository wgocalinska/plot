import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress as lr

def plot():
    file = input('Enter your file : ')

    x, y = np.loadtxt(file, delimiter=',', unpack=True, skiprows=1)

    a, b, r, _, da = lr(x, y)
    regline = a*x + b

    print('Regression line = ' + str(round(a, 2)) + '*x + ' + str(round(b, 2)))

    plt.figure(figsize=(5, 5))
    plt.plot(x, y, 'ro')
    plt.plot(x, regline)
    plt.grid(True)
    plt.xlabel("Mass [g]")
    plt.ylabel("Elongate [cm]")
    plt.tight_layout(0,2)
    plt.show()
plot()
