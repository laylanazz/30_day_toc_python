import sys


def main():

    x = input("Enter a number:")
    print(f"Value of x : {int(x)}")

    x = None
    print(f"New value of x : {x}")

    return 0
#the variable can change type because it is not a typed variable; it does not restrict the input
    # to a certain type


if __name__ == '__main__':
    sys.exit(main())