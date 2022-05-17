#My own math module

def add(x, y):
    """
    returns the summation of x and y
    """
    return x + y

assert(add(1,2) == 3)
assert(add(-1,2) == 1)
assert(add(-1,-2) == -3)


def subtraction(x,y):
    """
    returns the subtraction between x and y
    """
    return x - y

assert(subtraction(2,1) == 1)
assert(subtraction(2,-1) == 3)
assert(subtraction(-2,-1) == -1)


def evenNum(x):
    """
    returns number of even numbers in given list
    """
    return len([1 for i in x if i % 2 == 0])

assert(evenNum([1,2,3,4,5,6]) == 3)
assert(evenNum([1]) == 0)
assert(evenNum([345,123,22]) == 1)


def maximum(x):
    """
    returns maximum value from given list
    """
    return sorted(x)[-1]

assert(maximum([1,2,3,4,5,6]) == 6)
assert(maximum([1,1,1,2,2,2]) == 2)
assert(maximum([-1,-2,-3,-4]) == -1)


def minimum(x):
    """
    returns minimum value from given list
    """
    return sorted(x)[0]

assert(minimum([1,2,3,4,5,6]) == 1)
assert(minimum([1,1,1,2,2,2]) == 1)
assert(minimum([-1,-2,-3,-4]) == -4)


def absolute(x):
    """
    returns absolute value of one number x
    """
    return -x if x < 0 else x

assert(absolute(-1) == 1)
assert(absolute(1) == 1)
assert(absolute(0) == 0)


def sumTotal(x):
    """
    returns the summation of all the elements for a given list x
    """
    sum = 0
    for i in x:
        sum += i
    return sum

assert(sumTotal([1,2,3,4,5,6]) == 21)
assert(sumTotal([1,1,1,2,2,2]) == 9)
assert(sumTotal([-1,-2,-3,-4]) == -10)


def clear(x):
    """
    sets all elements into 0 for a given list x
    """
    return [0 for i in x]

assert(clear([1]) == [0])
assert(clear([1,1,1,1]) == [0,0,0,0])