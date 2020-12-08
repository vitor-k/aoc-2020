def checkInfiniteLoop(filename):
    accumulator = 0
    pc = 0
    with open(filename) as file:
        instList = file.read().replace("\r", "").strip().split("\n")
    attempted = set()

    while(pc < len(instList)):
        accumulator = 0
        pc = 0
        executed = set()
        triedFlag = False
        while(pc not in executed and pc < len(instList)):
            operation, argument = instList[pc].strip().split()
            argument = int(argument)
            executed.add(pc)
            if(operation == "jmp"):
                if(not triedFlag and pc not in attempted):
                    attempted.add(pc)
                    pc+=1
                    triedFlag = True
                else:
                    pc += argument
            else:
                if(operation == "acc"):
                    accumulator += argument
                    pc += 1
                elif(not triedFlag and pc not in attempted):
                    attempted.add(pc)
                    pc += argument
                    triedFlag = True
                else:
                    pc += 1

    return accumulator

def main(filename = "input.txt"):
    a = checkInfiniteLoop(filename)
    print(a)

if __name__ == "__main__":
    main()