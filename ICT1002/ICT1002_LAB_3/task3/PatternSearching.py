import sys

def count_occurence(candidate, pattern):
    """
    returns number of occurences of pattern in candidate, -1 if none
    """
    #result = candidate.count(pattern)
    result = 0
    len_seq = len(pattern)
    upper_bound = len(candidate)-len_seq+1
    for i in range(upper_bound):
        if candidate[i:i+len_seq] == pattern:
            result += 1
    return "Pattern appears {} time!".format(result) if result else "Pattern appears -1 time!"


def main():
    args = sys.argv[1:]
    print(count_occurence(args[0].strip().split(","), args[1].strip().split(",")))
    

if __name__ == "__main__":
    main()
    