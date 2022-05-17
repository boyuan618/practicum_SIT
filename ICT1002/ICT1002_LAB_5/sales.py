import sys

scale = lambda l, x: [x*i for i in l]
sort = lambda l: sorted(l, key=lambda x: str(x)[-1])
goodsales = lambda l: [i for i in l if i > sum(l)/len(l)]


def main():
    l, x = sys.argv[1:3]
    x = int(x)
    l = list(map(int, l.strip().split(",")))
    print(f"The scaled number is: {scale(l,x)} The sorted sales numbers are: {sort(l)} The good sales numbers are: {goodsales(l)}")
    

if __name__ == "__main__":
    main()