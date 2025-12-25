import sys

#Ask the user for a number and a word.
#Print:
#"<word> repeated <number> times."

def main():

    number = int(input("Enter a number:"))
    word = input("Enter a word:")

    print((word + "\n") * number)

    return 0


if __name__ == '__main__':
    sys.exit(main())