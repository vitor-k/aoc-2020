def main():
    filename = "input.txt"
    n_set = set()
    sum_dict = dict()
    with open(filename) as file:
        for line in file:
            n = int(line)
            if(2020-n in sum_dict):
                tuppy = sum_dict[2020-n]
                print(tuppy[0] * tuppy[1] * n)
            else:
                for m in n_set:
                    sum_dict[n+m] = m,n
                n_set.add(n)

if __name__ == "__main__":
    main()