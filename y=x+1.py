import matplotlib.pyplot as plot
# Write a function f(x) that returns x + 1 and plot it for x values of -3 to 3 in increments of 1.

def f(x):
    return x + 1

xs = range(-3, 4)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
