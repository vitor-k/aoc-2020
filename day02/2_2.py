def main():
    filename = "input.txt"
    valid = 0
    with open(filename) as file:
        for line in file:
            (num, pol, pw) = line.split()
            (first, second) = num.split('-')
            valid += (pw[int(first)-1] == pol[0]) ^ (pw[int(second)-1] == pol[0])
    print(valid)

if __name__ == "__main__":
    main()