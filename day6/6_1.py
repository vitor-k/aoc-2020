def checkPass(filename):
    with open(filename) as file:
        anslist = file.read().replace("\r", "").replace("\n\n", "|").replace("\n", "").split("|")
    
    ansnums = []

    for line in anslist:
        ansset = set()
        for char in line:
            ansset.add(char)
        print(ansset)
        ansnums.append(len(ansset))
    print(ansnums)
    return sum(ansnums)

def main(filename = "input.txt"):
    a = checkPass(filename)
    print(a)

if __name__ == "__main__":
    main()