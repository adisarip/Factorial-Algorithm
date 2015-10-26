# Factorial-Algorithm
 Suite of Python programmes to calculate the n! for a large number Efficiently.
 
This is a suite of Python programmes to calculate the n! for a large number Efficiently. They have been written for pedagogical purposes, to illustrate the effect of several fundamental algorithmic optimisations in the n factorial of a very large number.

- The [first one](https://github.com/ankur-anand/Factorial-Algorithm/blob/master/fact_01_recursive.py) is the naive recursive approach which will give us `RuntimeError: maximum recursion depth exceeded.` for large number as python doesn't have optimized [tail recursion](https://en.wikipedia.org/wiki/Tail_call). 

- The [Second one](https://github.com/ankur-anand/Factorial-Algorithm/blob/master/fact_02_multiplication.py) use the uses the approach of successive multiplication.From the line profilier, for `n = 100000` most of the %time was spent in multiplication step which is '98.8'`31    100000      3728380     37.3     98.8         result *= x`. so we can reduce the multiplication in factorial by half, for even number, hence doing Strength Reduction.

- The [Third one](https://github.com/ankur-anand/Factorial-Algorithm/blob/master/fact_03_multi_half.py) has been further Optimized to reduce the number of successive multiplication. It reduces the number of number to half, Which shows some improvement in the mid range but didn't improved much with scaling, from the second one. For `n = 100000` most of the %time was again spent in multiplication step which is '97.8  `61     50000      3571126     71.4     97.8  		factorial *= next_multi` though the number of multiplication has reduced to half

- The last i.e [fourth one](https://github.com/ankur-anand/Factorial-Algorithm/blob/master/fact_04_prime_decompose.py) has been Optimized further using [prime decomposition](https://en.wikipedia.org/wiki/Integer_factorization) to reduce the total number of multiplication.
None of them is optimised very much, but the last two are at least not obscenely slow.

**Some profiled timings in seconds (single runs, on ubuntu 14.04, 64 - bit ):**

|  Algorithm Used     |      n      |       Total Time (second)    |
|---------------------|-------------|------------------------------|
| Recursive           | n = 100     |         0.000268 s           |
|                     | n = 200     |         0.000597 s           |
|---------------------|-------------|------------------------------|
|Successive Multiplication  | n =  1000 | 0.001115 s |
| | n = 10000 | 0.035327 s |
| | n =  100000 | 3.77454 s |
| ---------| -------------| --------------------|
| Half Successive Multiplication | n = 1000 | 0.00115 s |
| | n = 10000 | 0.023636 s |
| | n = 100000 | 3.65019 s |
| --- | ---- | ---- |
| Prime Decompostion | n = 1000 | 0.007484 s |
| | n = 10000 | 0.061662 s|
| | n = 100000 | 2.45769 s |

