import matplotlib.pyplot as plot
import math

def f(x):
    return x * 1.8 + 32

xl = range(15, 51)
ys = []
for x in xl:
    ys.append(f(x))

plot.plot(xl, ys)
plot.show()
