def checkPass(filename):
    with open(filename) as file:
        anslist = file.read().replace("\r", "").replace("\n\n", "|").split("|")
    
    ansnums = []

    for line in anslist:
        resbin = (1<<27) - 1
        answers = line.split("\n")
        for person in answers:
            if(len(person) == 0):
                continue
            ansbin = 0
            for char in person:
                ansbin |= 1 << (ord(char) - 97)
            resbin &= ansbin
        ansnums.append(bin(resbin).count("1"))
    return sum(ansnums)

def main(filename = "input.txt"):
    a = checkPass(filename)
    print(a)

if __name__ == "__main__":
    main()