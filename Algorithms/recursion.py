# Recursion

# Factorial
def findFactorialRecursive(number):  #O(n)
    if (number == 1):
        return 1
    return number*findFactorialRecursive(number-1)

# print(findFactorialRecursive(2))

def findFactorialIterative(number):  #O(n)
    cnt=1
    while number >= 1:
        cnt = cnt * number
        number -= 1
    return cnt

# print(findFactorialIterative(2))

# ---------------------------------------------------------

# Fibonacci

# Given a number N return the index value of the Fibonacci sequence, where the sequence is:
# 0  1  2  3  4  5  6
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8


def fibonacciIterative(n):  #O(n)
    if (n==0 or n==1):
        return n
    return fibonacciIterative(n-1)+fibonacciIterative(n-2)

def fibonacciRecursive(n): 
    # O(2^n) - this is exponenial time. Size of the tree exponentionally grows when n increases. Every addional element in the fibonacci sequance we get a increase in function calls exponentionally.
    if (n==0 or n==1):
        return n
    f1=0
    f2=1
    for i in range(1,n):
        f3 = f1 + f2
        f1=f2
        f2=f3
    return f3

# def fibonacciIterative(n):
#  arr = [0, 1];
#  for (let i = 2; i < n + 1; i++):
#    arr.push(arr[i - 2] + arr[i -1]);
#  return arr[n];

print(fibonacciRecursive(3))
