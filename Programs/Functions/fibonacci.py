
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        print("fib no ",n)
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))

n_terms = 3

# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
    for i in range(0, n_terms):
        print("fib ",i, recursive_fibonacci(i))