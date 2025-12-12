import sys


def main():

    #Ask the user for a short message. Print it repeated three times

    text = input("Enter a short message:")
    print((text + "\n") * 3)

    return 0


if __name__ == '__main__':
    sys.exit(main())