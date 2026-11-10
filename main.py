def read_scores(filename: str = "scores.txt") -> list:
    with open(filename, "r") as file:
        return file.readlines()


def convert_to_collection(lines):
    data = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) < 2:
            continue

        name = parts[0].strip()
        score = int(parts[1].strip())
        data.append((name, score))

    return data


def print_scores(data):
    for name, score in data:
        print(name, "->", score)


def average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def convert_to_dictionary(data):
    result = {}

    for item in data:
        result[item["Name"]] = item["Score"]

    return result


def main():
    filename = "scores.txt"
    lines = read_scores(filename)
    data = convert_to_collection(lines)

    print("All scores:")
    print_scores(data)

    scores = [score for _, score in data]
    if scores:
        print("Average score:", average(scores))
        print("Highest score:", max(scores))
        print("Failed students:", [name for name, score in data if score < 10])

    write_summary("summary.txt", data)


def calculate_bonus_scores(data):
    bonus_list = []

    for student in data:
        name = student[0]
        score = student[1]

        if score > 15:
            score += 1

        bonus_list.append((name, score))

    return bonus_list


def write_summary(filename, data):
    scores = [score for _, score in data]

    if not scores:
        average_score = 0
        highest_score = 0
        failed_students = 0
    else:
        average_score = average(scores)
        highest_score = max(scores)
        failed_students = sum(1 for _, score in data if score < 10)

    student_count = len(data)

    with open(filename, "w") as file:
        file.write(f"Average score: {average_score}\n")
        file.write(f"Highest score: {highest_score}\n")
        file.write(f"Number of students: {student_count}\n")
        file.write(f"Number of failed students: {failed_students}\n")


if __name__ == "__main__":
    main()
