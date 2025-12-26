import sys


def main():

    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))

    print(a > b)
    print(a == b)
    print(a != b)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())