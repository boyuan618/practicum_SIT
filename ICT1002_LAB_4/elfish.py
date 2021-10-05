import sys

def elfish(word,e=False,l=False,f=False):
    """
    checks recursively if it has letter e,l,f in it
    """
    if not word:
        return e and l and f
    
    letter = word[0]
    if letter == "e":
        e = True
    
    elif letter == "l":
        l = True
        
    elif letter == "f":
        f = True
        
    return elfish(word[1:], e, l, f)

assert(elfish("waffles") == True)
assert(elfish("instance") == False)
assert(elfish("elish") == False)


def main():
    arg = sys.argv[1].lower()
    is_elfish = elfish(arg)
    if is_elfish:
        print(f"{arg} is one elfish word!")
    
    else:
        print(f"{arg} is not an elfish word!")
        
        
if __name__ == "__main__":
    main()