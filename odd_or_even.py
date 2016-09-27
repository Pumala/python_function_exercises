import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

xl = range(-5, 6)
ys = []
for x in xl:
    ys.append(f(x))

plot.bar(xl, ys)
plot.show()
