import sys


def main():

    values = [5, 6, 7, 8]
    print(f"Values: {values}")

    first_two = values[0:2]
    print(f"First two values: {first_two}")

    return 0


if __name__ == '__main__':
    sys.exit(main())