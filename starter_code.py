# Recommended imports
import math  # For doing math
import collections  # For things like Counters and defaultdict's
import string  # For things like getting all the ASCII chars, or alphabet
# Before the competition, become familiar with whats in these three modules

# Also, sometimes theres complex math (imaginary numbers!)
import cmath  # Like math but works for imaginary numbers too!
# To write imaginary numbers, write a + bj == (a + bi)
z = 3+4j  # Is equal to 3+4i
z.imag  # -> 4
z.real  # -> 3

# Some useful functions - ord, chr
print(ord('a'))  # -> 65
print(chr(65))  # -> 'a'
# Converts between ASCII (or Unicode) value and the character


# Getting input from standard input
# Use these functions when reading input from console
# input() to read a full line (without the newline at the end)
ipt = input()  # <- John
print("Hi, {}!".format(ipt))  # -> Hi, John!


def readint() -> int:
    """
    Read an integer from the input, will error if the input is not an int
    For example `5`
    """
    return int(input())


def readfloat() -> float:
    """
    Read a float from the input, will error if the input is not a float
    For example `5`, `.3`, `3.`, and `4.35`
    """
    return float(input())


def readlist(delimiter: str =" ") -> list:
    """
    Read a list of items split by the `delimiter`, which is by default a space.
    To use a comma as a delimiter use `readlist(",")`
    For example `John Roy Kevin` -> ["John", "Roy", "Kevin"]
    """
    return input().split(delimiter)


def readlistint(delimiter: str=" "):
    """
    Read a list of integers split by the `delimiter`, see `readlist`
    For example `5 4 3 1 2` -> [5, 4, 3, 1, 2]
    """
    return [int(x.strip()) for x in input().split(delimiter)]


def readlistfloat(delimiter: str=" "):
    """
    Read a list of integers split by the `delimiter`, see `readlist`
    For example `5 4.1 3.21 1. .2` -> [5, 4.1, 3.21, 1., .2]
    """
    return [float(x.strip()) for x in input().split(delimiter)]


# When reading input from a file
# For example, at CodeQuest the input files match `ProbXX.in.txt`
# Versus the file names which are `ProbXX.py`

ending = ".in.txt"
filename = __file__.split("/")[-1].split(".")[0] + ending
# If this file is called `ProbXX.py`, filename will be `ProbXX.in.txt`
dfile = open(filename, 'r')

# To use the above functions with the new file instead
# Redefine the input() function as follows:

def input():
    return dfile.readline()[:-1]


# At CodeQuest all problems will give input as
# First: a number denoting the number of test cases `n`
# Second: n number of lines for the inputs
# For example:
# 2
# Henry
# John

for case in range(readint()):
    name = input()
    print("Hello, {}!".format(name))  #(or if you're really advanced `f"Hello, {name}"`

# Hello, Henry!
# Hello, John!

# Some will include sub-cases
# For example, with sums
# 2 - number of cases
# 3 - number of numbers to sum
# 6 - the numbers to sum
# 32
# 517
# 2 - second set of numbers
# 82
# 12

for case in range(readint()):
    sum = 0
    for nnum in range(readint()):
        sum += readint()

    print("The sum is", sum)

# The sum is 555
# The sum is 94
