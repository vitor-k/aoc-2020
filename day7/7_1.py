import re

def recursiveSet(dictty, key):
    setty = set([key])
    if(key in dictty):
        #print(key, dictty[key])
        for outer in dictty[key]:
            outSet = recursiveSet(dictty, outer)
            print(outSet)
            setty = setty.union(outSet)
    return setty

def checkRules(filename):
    with open(filename) as file:
        ruleslist = file.read().replace("\r", "").split("\n")
    
    faux = dict()

    pattern = re.compile(r"\d ([\w ]+) bags*")
    
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
            if(child in faux):
                faux[child].append(parent)
            else:
                faux[child] = [parent]
    
    containingSet = recursiveSet(faux, "shiny gold")
    containingSet.discard("shiny gold")

    return len(containingSet)

def main(filename = "input.txt"):
    a = checkRules(filename)
    print(a)

if __name__ == "__main__":
    main()