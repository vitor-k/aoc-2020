
def gameOfSeats(filename):
    with open(filename) as file:
        layout = [list(line) for line in file.read().replace("\r", "").strip().split("\n")]

    changed = True
    while(changed):
        changed = False
        newLayout = [[x for x in line] for line in layout]
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if(layout[i][j] == '.'):
                    continue
                occupied = 0
                if(i and j):
                    occupied += layout[i-1][j-1] == '#'
                if(i):
                    occupied += layout[i-1][j] == '#'
                if(j):
                    occupied += layout[i][j-1] == '#'
                if(i<len(layout)-1 and j<len(layout[0])-1):
                    occupied += layout[i+1][j+1] == '#'
                if(i<len(layout)-1):
                    occupied += layout[i+1][j] == '#'
                if(j<len(layout[0])-1):
                    occupied += layout[i][j+1] == '#'
                if(i and j<len(layout[0])-1):
                    occupied += layout[i-1][j+1] == '#'
                if(i<len(layout)-1 and j):
                    occupied += layout[i+1][j-1] == '#'
                
                if(layout[i][j] == 'L' and occupied == 0):
                    newLayout[i][j] = '#'
                    changed = True
                elif(layout[i][j] == '#' and occupied >= 4):
                    newLayout[i][j] = 'L'
                    changed = True
        layout = newLayout

    return ''.join([''.join(x) for x in layout]).count('#')

def main(filename = "input.txt"):
    a = gameOfSeats(filename)
    print(a)

if __name__ == "__main__":
    main()