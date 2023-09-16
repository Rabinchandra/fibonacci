# Fibonacci
Fibonacci Sequence with Recursive Functions without Memoization in time complexity of O(n)

# Explanation:

1. `fib_1` is a function to print the Fibonacci sequence up to the nth term using recursion. It takes three arguments: `n` (the number of terms to print), `a` (the first Fibonacci number), and `b` (the second Fibonacci number).

2. In `fib_1`, it prints the current Fibonacci number (`a`) and then recursively calls itself with `n-1`, `b`, and `a+b` to calculate and print the next number. This process continues until `n` reaches 0, at which point it stops.

3. `fib_2` is a function to get the nth term of the Fibonacci sequence using recursion. It also takes three arguments: `n`, `a`, and `b`.

4. In `fib_2`, it returns `a` when `n` is 0 or 1, as these are the base cases. Otherwise, it recursively calls itself with `n-1`, `b`, and `a+b` to calculate the nth term of the sequence.

Now, let's discuss the time complexity of these functions:

- For `fib_1`, the time complexity is O(n), where "n" is the number of terms to print. It prints each Fibonacci number once, and the recursion depth is directly proportional to "n."

- For `fib_2`, the time complexity is also O(n) because it calculates the nth term of the Fibonacci sequence using recursion, and the recursion depth is proportional to "n."

These functions have linear time complexity, making them efficient for calculating and printing Fibonacci numbers up to a specified term. 
