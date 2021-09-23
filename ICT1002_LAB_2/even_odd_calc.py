import sys

def calc(vals):
    """
    Even Odd calculator
    """
    even = []
    odd = []
    max = vals[0]
    min = vals[0]
    for num in vals:
        if num > max:
            max = num
        
        if num < min:
            min = num
        
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    sum_of_even = sum(even)
    sum_of_odd = sum(odd)
    diff = max-min
    no_of_even = len(even)
    no_of_odd = len(odd)
    vals.remove(max)
    vals.remove(min)
    centered_av = sum(vals)//len(vals)
    return "The sum of all even numbers is {}, the sum of all odd numbers is {}, the difference between the biggest and smallest number is {}, the total number of even numbers is {}, the total number of odd numbers is {}, the centered average is {}.".format(sum_of_even, sum_of_odd,diff,no_of_even,no_of_odd,centered_av)
    
    
    
def main():
    args = sys.argv[1].strip().split(",")
    try:
        args = list(map(int, args))
    
    except ValueError:
        print("Please enter valid integers.")
        return 0
    print(calc(args))
    
if __name__ == "__main__":
    main()