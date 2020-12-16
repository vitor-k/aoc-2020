import re

def recursiveCount(dictty, key):
    num = 1
    if(key in dictty):
        #print(key, dictty[key])
        for innieTuple in dictty[key]:
            n, innie = innieTuple
            inNum = recursiveCount(dictty, innie)
            num += n*inNum
    return num

def checkRules(filename):
    with open(filename) as file:
        ruleslist = file.read().replace("\r", "").split("\n")
    
    faux = dict()

    pattern = re.compile(r"(\d [\w ]+) bags*")
    
    for line in ruleslist:
        if(len(line) == 0):
            continue
        line = line.split(" bags contain ")
        parent = line[0]
        if("no" in line[1]):
            continue
        i = 0
        while(pattern.search(line[1], i)):
            child = pattern.search(line[1], i)
            i = child.span(1)[1]
            child = child.group(1)
            n = int(child.split()[0])
            child = " ".join(child.split()[1:])
            if(parent in faux):
                faux[parent].append((n, child))
            else:
                faux[parent] = [(n, child)]
    
    numBags = recursiveCount(faux, "shiny gold")

    return numBags - 1

def main(filename = "input.txt"):
    a = checkRules(filename)
    print(a)

if __name__ == "__main__":
    main()