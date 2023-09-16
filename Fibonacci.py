# To print the fibonacci sequence upto nth term
def fib_1(n, a=0, b=1):
    if n > 0:
        print(a, end=" ")
        fib_1(n-1, b, a+b)


# To get the nth term of the fibonacci sequence
def fib_2(n, a=0, b=1):
    if n <= 1:
        return a
    return fib_2(n-1, b, a+b)


fib_1(5)  # print the fibonacci sequence upto 5th term

print()  # next line

print("Fibonacci Sequence of 5th term: ", fib_2(5))
