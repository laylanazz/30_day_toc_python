import sys

#Ask for a word. Print whether the word starts with "a" or "A" using a boolean expression

def main():

    while True:
        word = input("Enter a word:")

        if word.isalpha():
            break
        else:
            print("Try again")

    print(word.istitle())

    return 0


if __name__ == '__main__':
    sys.exit(main())