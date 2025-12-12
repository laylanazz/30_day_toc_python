import sys


def main():

    #Ask the user for two words and print them combined with a space

    word_1 = input("Enter a word:")
    word_2 = input("Enter another word:")

    if word_1.isalpha() and word_2.isalpha():
        print(" ".join((word_1, word_2)))
    else:
        print("Error! Try again.")

    return 0


if __name__ == '__main__':
    sys.exit(main())