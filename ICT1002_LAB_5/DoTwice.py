import sys

double = lambda x: 2*x
square = lambda x: x**2
cuber = lambda x: x**3
doTwice = lambda c, x: c(c(x))

def main():
    x, c = sys.argv[1:3]
    x = int(x)
    if c == "1":
        print(doTwice(double, x))
    
    elif c == "2":
        print(doTwice(square, x))
        
    elif c == "3":
        print(doTwice(cuber, x))
        
    else:
        print("It cannot be supported!")
        

if __name__ == "__main__":
    main()