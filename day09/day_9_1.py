def XMAS(filename):
    plen = 25
    with open(filename) as file:
        codeList = file.read().replace("\r", "").strip().split("\n")

    xmasqueue = []
    for i in range(plen):
        xmasqueue.append(int(codeList[i]))
    
    for i in range(plen, len(codeList)):
        n = int(codeList[i])
        flag = False
        for num in xmasqueue:
            if(n-num in xmasqueue and num != n-num):
                flag = True
        if(not flag):
            return n
        xmasqueue.pop(0)
        xmasqueue.append(n)
    return 0

def main(filename = "input.txt"):
    a = XMAS(filename)
    print(a)

if __name__ == "__main__":
    main()