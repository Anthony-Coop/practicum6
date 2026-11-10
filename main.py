def read_scores(scores.txt):
    file = open(scores.txt, "r")
    lines = file.readlines()
    file.close()
    return lines


def convert_to_collection(lines):
    data = [15,9,18,12,7,16,11,19,14,8]

    for line in lines:
        parts = line.strip().split(",")
        name = parts[0]
        score = int(parts[1])
        data.append((name, score))

    return data


def print_scores(data):
    for item in data:
        print(item[0], "->", item[1])


def main():
    filename = "scores.txt"
    lines = read_scores(filename)
    data = convert_to_collection(lines)
    print_scores(data)
    
    

if __name__ == "__main__":
    main()
