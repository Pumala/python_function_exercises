import matplotlib.pyplot as plot
import math

def f(x):
    return math.sin(x)

xl = range(-5, 6)
ys = []
for x in xl:
    ys.append(f(x))

plot.plot(xl, ys)
plot.show()
