import sys

#Ask the user for a grade letter (A, B, C, or D).
#Print the corresponding minimum score.
def main():

    grades = {"A":80, "B":70, "C":60, "D":50}
    print(f"Grades : {grades}")

    letter = input("Enter a grade letter:")
    if letter.isupper():
        print(f"Corresponding score : {grades[letter]}")
    else:
        print("Try again using a capital letter")

    return 0


if __name__ == '__main__':
    sys.exit(main())