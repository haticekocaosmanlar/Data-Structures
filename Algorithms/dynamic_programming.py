
calculations_recursive_fib = 0
def fibonacciRecursive(n):  #O(2^n)
    global calculations_recursive_fib
    calculations_recursive_fib += 1
    if (n<2):
        return n
    return fibonacciRecursive(n-1)+fibonacciRecursive(n-2)
# Dynamic Programming

# A closure—unlike a plain function—allows the function to access those captured 
# variables through the closure’s copies of their values or references, even when 
# the function is invoked outside their scope.

# Closures in Python help to invoke functions outside their scope. 
# The function innerFunction(fib) has its scope only inside the outerFunction(fibonacciMaster). 
# But with the use of Python closures, we can easily extend its scope to invoke 
# a function outside its scope.
calculations_dp_fib = 0
def fibonacciMaster():   #O(n) but we increase the space comlexity
    cache = {}
    def fib(n):
        global calculations_dp_fib
        calculations_dp_fib += 1
        if(n in cache):
            return cache[n]
        else:
            if(n<2):
                return n
            else:
                cache[n] = fib(n-1) + fib(n-2)
                return cache[n]
    # Note we are returning function
    # WITHOUT parenthesis
    return fib
            
fasterFib = fibonacciMaster()
print('DP ', fasterFib(35))
print('Recursive ', fibonacciRecursive(35))
print('We did ', calculations_dp_fib, ' calculations with DP')
print('We did ', calculations_recursive_fib, ' calculations with recursion')