import matplotlib.pyplot as plot

def f(x):
    return x ** 2

xl = range(-100, 101)
ys = []
for x in xl:
    ys.append(f(x))

plot.plot(xl, ys)
plot.show()
