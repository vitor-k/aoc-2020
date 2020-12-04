def checkPassValid(filename):
    valid = 0
    with open(filename) as file:
        passlist = file.read().replace("\r", "").replace("\n\n", "|").replace("\n", " ").split("|")
    for doc in passlist:
        fields = [(x[0], x[1]) for x in [y.strip().split(":") for y in doc.split()]]
        if(len(fields) >= 7):
            if(len(fields) == 8):
                valid += 1
                continue
            flag = 0
            for field in fields:
                if(field[0] == "cid"):
                    flag = 1
            if(not flag):
                valid += 1
    return valid

def main(filename = "input.txt"):
    a = checkPassValid(filename)
    print(a)

if __name__ == "__main__":
    main()