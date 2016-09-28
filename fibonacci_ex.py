# Instructor's example of fibonacci
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        previous = fib(n - 1)
        previous_previous = fib(n - 2)
        return previous + previous_previous

answer = fib(4)
