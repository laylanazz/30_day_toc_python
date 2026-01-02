import sys


def main():

    integers = list((10, 20, 30, 40, 50, 60))
    print(f"List of integers: {integers}")

    integers = integers[1:5]
    print(f"New list of integers: {integers}")

    return 0


if __name__ == '__main__':
    sys.exit(main())