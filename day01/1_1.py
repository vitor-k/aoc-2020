def main():
    filename = "input.txt"
    with open(filename) as file:
        n_set = set()
        for line in file:
            n = int(line)
            if(2020-n in n_set):
                print(n * (2020-n))
            n_set.add(n)

if __name__ == "__main__":
    main()