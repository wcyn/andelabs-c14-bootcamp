# Day 0 - Prime Number Generator

# Prime Number Generator
This repo contains Python code that generates [prime numbers](https://en.wikipedia.org/wiki/Prime_number) from `0` to a given number `n`.

[__Asymptotic analysis__](#asymptotic-analysis) is later carried out on the program in order to measure its efficiency in time and space.

A number of [__Test Cases__](#running-the-tests) are provided as well.


## Getting Started
These instructions should help you run the code on your machine.

### Prerequisites
Note that the code is written in Python3. Some functionality may not work with Python2
Install [nose](http://nose.readthedocs.io/en/latest/). Nose is a python package that makes unittesting easier by sorting out issues with relative imports in Python.
```
$ pip install nose
```
or
```
$ easy_install nose
```
### Installing

Clone the repository from GitHub:
```
$ git clone https://github.com/wcyn/andelabs-c14-bootcamp
```

### Running the program
Change Directory into the `prime_number_gen` folder
```
$ cd prime_number_gen
```

Run the python file with the code by typing:
```
$ python code/prime_num_gen.py
```
## Running the Tests
There are 11 tests in the Python test file.
In order to run these tests, use the following command while in the 'project folder':

```
$ nosetests
```

## Asymptotic Analysis
Below is the basic code used to generate the prime numbers from `0` to a given number `n`:

```
prime_nums = [2]
for i in range(3,n+1):
    # start from 3 onwards
    # "outer loop"
    factor_count=0
    for x in range (2,i):
        # start from 2 onwards
        if i % x == 0:
            factor_count+=1
            # inner loop breaking..
            break # i is not a prime number 
    if factor_count==0:
        prime_nums.append(i)
```

In the above code, there exists two loops. The outer loops iterates through all the numbers from 3 and n, which gives us n-3.

The inner loop seems to iterate through the numbers 2 up to i-1, which gives us i-3. 

However, this doesn't happen if the number is not a prime number since the loop breaks if even one factor is found.

The worst case scenario would therefore mean that all the numbers between `0` and the number `n` are prime nunmbers, which is not the actual behaviour of numbers. This would give us the quadractic `O(N^2)`. Meaning that the code runs with more efficiency that `O(N^2)`. 

These facts aside, the big-O notation of the above code would be (n-3)(n-1), which approximates to n^2. The Big-O analysis of the above code is therefore quadratic __`O(N^2)`__.

