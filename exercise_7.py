import sys


def main():

    word_1 = input("Enter a word:")
    n = len(word_1)

    if word_1.isalpha():
        print(f"The first letter is {word_1[0]} and the last letter is {word_1[n-1]}")
    else:
        print("Error! Try again.")


    return 0


if __name__ == '__main__':
    sys.exit(main())