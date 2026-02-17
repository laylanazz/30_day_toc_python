import sys


def main():

    student_name = input("Enter your name:")
    score_1 = int(input("Enter your first score:"))
    score_2 = int(input("Enter your second score:"))
    score_3 = int(input("Enter your third score:"))

    scores = list((score_1, score_2, score_3))
    print(f"Scores: {scores}")

    student = dict(name = student_name, scores = scores)
    print(f"Student: {student}")

    average_score = sum(student["scores"]) / len(student["scores"])
    student["average"] = average_score
    print(f"Student: {student}")

    return 0


if __name__ == '__main__':
    sys.exit(main())