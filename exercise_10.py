import sys


def main():

    x = int(input("Enter an integer:"))
    if x.is_integer():
        print(x)
        print(float(x))
   
    return 0


if __name__ == '__main__':
    sys.exit(main())