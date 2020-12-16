def main():
    filename = "input.txt"
    valid = 0
    with open(filename) as file:
        for line in file:
            num, pol, pw = line.split()
            nmin, nmax = num.split('-')
            valid += int(nmin) <= pw.count(pol[0]) <= int(nmax)
    print(valid)

if __name__ == "__main__":
    main()