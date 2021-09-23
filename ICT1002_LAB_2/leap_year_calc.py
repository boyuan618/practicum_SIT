import sys

def check_leap(year):
    """
    check if year is leap year
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                return False
        return True
    
    return False
        
    
def calc(start, end):
    """
    Leap year calculator
    """
    leaps = []
    for year in range(start, end+1):
        if check_leap(year):
            leaps.append(year)
            

    return "The number of Leap Years is {}, the Leap Years are ".format(len(leaps)) + ("{}, "*len(leaps)).format(*leaps)

def main():
    args = sys.argv[1:]
    try:
        args = list(map(int, args))
    
    except ValueError:
        print("Please enter valid values.")
    
    print(calc(args[0], args[1])[:-2])
    
if __name__ == "__main__":
    main()