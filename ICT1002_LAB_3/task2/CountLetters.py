import sys

def count_letters(*args):
    """
    returns a dictionary of what letters appeared and how many times
    """
    letters = {}
    keys = []
    for arg in args:
        for letter in arg:
            if letter not in keys:
                keys.append(letter)
                letters[letter] = 1
            
            else:
                letters[letter] += 1
                
    return letters


def main():
    words = sys.argv[1].strip().split(",")
    result = count_letters(*words)
    for key in sorted(result, reverse=True):
        print("{}:{}".format(key, result[key]), end=" ")
    

if __name__ == "__main__":
    main()