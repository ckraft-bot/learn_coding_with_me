################################################# Loop Efficiency Test
import timeit
"""
sum the numbers from 0 to n-1 in different ways.
"""
def while_loop(n = 100_000_000):
    i = 0 # initialize
    s = 0 # sum
    while i< n:
        s += i
        i += 1
    return s

def for_loop(n = 100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s

def for_loop_with_increment(n = 100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s

def for_loop_with_test(n = 100_000_000):
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
    return s

def for_loop_with_increment_and_test(n = 100_000_000):
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
    return s

# python functions
def sum_range(n = 100_000_000): 
    return sum(range(n)) 

# numpy functions-- mostly written in C
import numpy
def sum_numpy(n = 100_000_000): 
    return numpy.sum(numpy.arange(n))

def sum_math(n = 100_000_000): 
    return (n * (n-1))//2 # formula for finding the total number of subarrays for a given array of size n

def main():
    print("while loop\t\t", timeit.timeit(while_loop, number = 1)) # expected output: 6.7826302
    print("for loop\t\t", timeit.timeit(for_loop, number = 1)) # expected output: 4.8714659
    print("for increment\t\t", timeit.timeit(for_loop_with_increment, number = 1)) # expected output: 5.983620700000001
    print("for test\t\t", timeit.timeit(for_loop_with_test, number = 1)) # expected output: 7.527691699999998
    print("for increment + test\t", timeit.timeit(for_loop_with_increment_and_test, number = 1)) # expected output: 7.6164038000000005
    print("sum range\t\t", timeit.timeit(sum_range, number = 1)) # expected output: 4.055566499999998
    print("numpy sum\t\t", timeit.timeit(sum_numpy, number = 1)) # expected output: 0.20567159999999518
    print("math sum\t\t", timeit.timeit(sum_math, number = 1)) # expected output: 2.2999999984563146e-06 OR 0.0000022999999984563146

if __name__ == "__main__":
    main()
    
"""
The extra checks (such as if i < n: pass lines) in the for lopps with increments, or tests, or increments and tests slowed down the computation.
The verdict is that in the looping methods the pure for loop was the most efficient. 
All methods considered, the non loops are faster than for loops. Amongst the three non loop methods pure math was the best! 
The second and third fastest are the numpy sum and sum range respectively. 
The reason numpy sum is faster than sum range is due to the fact that numpy is written in C whereas sum range is using python functions.
C is faster than python. 
Back to the ultimate winner--the pure math (sum_math) implementation is the way to go in the future.
"""