import sys

#Ask the user for three words (one per input).
#Store them in a list and print the list exactly as Python represents it

def main():

    word_1 = input("Enter a word:")
    word_2 = input("Enter another word:")
    word_3 = input("Enter another word:")

    if word_1.isalpha() and word_2.isalpha() and word_3.isalpha():
        words = [word_1, word_2, word_3]
        print(words)
    else:
        print("Invalid Input; try again")

    return 0


if __name__ == '__main__':
    sys.exit(main())