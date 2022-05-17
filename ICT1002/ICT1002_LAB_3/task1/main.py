from myMath import *
import sys


def main():
    x = sys.argv[1].strip().split(",")
    try:
        x = list(map(int, x))
        print("The difference is:%d" % (subtraction(maximum(x),minimum(x))), end=" ")
        print("The summation is:%d" % (add(maximum(x),minimum(x))), end=" ")
        print("The summation of all input is:%d" % (sumTotal(x)), end=" ")
        print("The number of even numbers is:%d" % (evenNum(x)), end=" ")
        print("The values in the list are: " + str(clear(x)))
        
    except ValueError:
        pass
    
if __name__ == "__main__":
    main()

