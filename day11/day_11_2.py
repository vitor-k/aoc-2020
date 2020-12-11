
def gameOfSeats(filename):
    with open(filename) as file:
        layout = [list(line) for line in file.read().replace("\r", "").strip().split("\n")]

    height = len(layout)
    width = len(layout[0])
    changed = True
    while(changed):
        changed = False
        newLayout = [[x for x in line] for line in layout]
        for i in range(height):
            for j in range(width):
                if(layout[i][j] == '.'):
                    continue
                occupied = 0
                if(i and j): #up left
                    sublayout = [layout[i-k][j-k] for k in range(1,min(j, i)+1) if layout[i-k][j-k] != '.']
                    occupied += len(sublayout) and sublayout[0] == '#'
                if(i): #up
                    sublayout = [layout[k][j] for k in reversed(range(i)) if layout[k][j] != '.']
                    occupied += len(sublayout) and sublayout[0] == '#'
                if(j): #left
                    sublayout = list(reversed(layout[i][:j]))
                    occupied += '#' in sublayout and ('L' not in sublayout or sublayout.index('L') > sublayout.index('#'))
                if(i<len(layout)-1 and j<len(layout[0])-1): #down right
                    sublayout = [layout[i+k][j+k] for k in range(1,min(width-j, height-i)) if layout[i+k][j+k] != '.']
                    occupied += len(sublayout) and sublayout[0] == '#'
                if(i<len(layout)-1): #down
                    sublayout = [layout[k][j] for k in range(i+1,height) if layout[k][j] != '.']
                    occupied += len(sublayout) and sublayout[0] == '#'
                if(j<len(layout[0])-1): #right
                    sublayout = layout[i][j+1:]
                    occupied += '#' in sublayout and ('L' not in sublayout or sublayout.index('L') > sublayout.index('#'))
                if(i and j<len(layout[0])-1): #up right
                    sublayout = [layout[i-k][j+k] for k in range(1,min(i+1, width-j)) if layout[i-k][j+k] != '.']
                    occupied += len(sublayout) and sublayout[0] == '#'
                if(i<len(layout)-1 and j): #down left
                    sublayout = [layout[i+k][j-k] for k in range(1,min(height-i, j+1)) if layout[i+k][j-k] != '.']
                    occupied += len(sublayout) and sublayout[0] == '#'

                if(layout[i][j] == 'L' and occupied == 0):
                    newLayout[i][j] = '#'
                    changed = True
                elif(layout[i][j] == '#' and occupied >= 5):
                    newLayout[i][j] = 'L'
                    changed = True
        layout = newLayout

    return ''.join([''.join(x) for x in layout]).count('#')

def main(filename = "input.txt"):
    a = gameOfSeats(filename)
    print(a)

if __name__ == "__main__":
    main()