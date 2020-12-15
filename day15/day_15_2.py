
def elfGame(filename, ith):
    with open(filename) as file:
        lines = file.read().strip().split(",")

    latest = 0
    numbers = {}
    i=0
    for el in lines:
        latest = el
        newLatest = str(i - int(numbers[latest])) if latest in numbers else '0'
        numbers[latest] = i
        i+=1
    
    while(i < ith):
        latest = newLatest
        newLatest = str(i - int(numbers[latest])) if latest in numbers else '0'
        numbers[latest] = i
        i+=1
    
    return latest

def main(filename = "input.txt"):
    a = elfGame(filename, 30_000_000)
    print(a)

if __name__ == "__main__":
    main()