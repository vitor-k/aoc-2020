def checkPassValid(filename):
    requiredFields = ["byr", "iyr", "eyr","hgt", "hcl", "ecl", "pid"]
    valid = 0
    with open(filename) as file:
        passlist = file.read().replace("\r", "").replace("\n\n", "|").replace("\n", " ").split("|")
    for doc in passlist:
        fields = {x[0]: x[1] for x in [y.strip().split(":") for y in doc.split()]}
        missingFields = [x for x in requiredFields if x not in fields]
        if(len(missingFields) == 0):
            #here starts part 2
            if ((int(fields["byr"]) not in range(1920, 2002+1))
            or (int(fields["iyr"]) not in range(2010, 2020+1))
            or (int(fields["eyr"]) not in range(2020, 2030+1))
            or ((int(fields["hgt"].replace("cm", "")) not in range(150, 193+1)) if "cm" in fields["hgt"] else (int(fields["hgt"].replace("in", "")) not in range(59,76+1)) if "in" in fields["hgt"] else True)
            or (len(fields["hcl"]) != 7 or fields["hcl"][0] != "#" or not all(char in "0123456789abcdef" for char in fields["hcl"][1:]))
            or (fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            or ((len(fields["pid"]) != 9) or not fields["pid"].isdigit())):
                continue
            #here ends part 2
            valid+=1
    return valid

def main(filename = "input.txt"):
    a = checkPassValid(filename)
    print(a)

if __name__ == "__main__":
    main()