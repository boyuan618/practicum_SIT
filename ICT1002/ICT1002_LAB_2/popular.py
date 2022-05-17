import sys

def main():
    arg = sys.argv[1].lower()
    count = []
    letters = []
    for letter in arg:
        if letter not in letters:
            count.append([1,letter])
            letters.append(letter)
        else:
            count[letters.index(letter)][0] += 1
    
    count.sort()
    count = count[::-1][:5]
    for i in range(5):
        for j in range(i):
            if count[i][0] == count[j][0]:
                if count[i][1] < count[j][1]:
                    temp = count[i]
                    count[i] = count[j]
                    count[j] = temp
    res = ""
    for i in count:
        res += "{}:{},".format(i[1], i[0])
    
    print(res[:-1])
    

        
        
if __name__ == "__main__":
    main()
    