import sys

def sum_recursive(x):
    """
    Sums 1 to x by recursion
    """
    if x < 1:
        return 0
    
    return x + sum_recursive(x-1)

assert(sum_recursive(3) == 6)


def sum_iterative(x):
    """
    sums 1 to x by iteration
    """
    res = 0
    for i in range(1,x+1):
        res += i
    return res

assert(sum_iterative(3) == 6)


def main():
    arg = int(sys.argv[1])
    print(f"The SUM value calculated by recursive is {sum_recursive(arg)} and by iterative is {sum_iterative(arg)}.")
    

if __name__ == "__main__":
    main()    