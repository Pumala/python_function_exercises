import matplotlib.pyplot as plot
import math
from numpy import arange

def f(x):
    return math.sin(x)

xl = arange(-5, 6 , 0.1)
ys = []
for x in xl:
    ys.append(f(x))

plot.plot(xl, ys)
plot.show()
