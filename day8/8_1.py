def checkInfiniteLoop(filename):
    accumulator = 0
    pc = 0
    with open(filename) as file:
        instList = file.read().replace("\r", "").split("\n")
    executed = set()

    while(pc not in executed and pc < len(instList)):
        instruction = instList[pc].split()
        executed.add(pc)
        if(instruction[0] == "jmp"):
            pc += int(instruction[1])
        else:
            if(instruction[0] == "acc"):
                accumulator += int(instruction[1])
            pc += 1

    return accumulator

def main(filename = "input.txt"):
    a = checkInfiniteLoop(filename)
    print(a)

if __name__ == "__main__":
    main()