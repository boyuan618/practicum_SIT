import sys

def digit(x):
    """
    count number of digits recursively
    """
    if x < 10:
        return 1
    
    return 1 + digit(x/10)

assert(digit(789) == 3)


def digit_iterative(x):
    """
    count number of digits iteratively
    """
    count = 1
    while x >= 10:
        count += 1
        x /= 10
    
    return count

assert(digit_iterative(789) == 3)
assert(digit_iterative(6789) == 4)


def main():
    arg = int(sys.argv[1])
    print(f"The number of digit(s) calculated by recursive is {digit(arg)} and by iterative is {digit_iterative(arg)}.")
    

if __name__ == "__main__":
    main()