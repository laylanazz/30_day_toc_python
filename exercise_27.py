import sys


def main():

    items = [10, 20, 30]
    print(f"List: {items}")

    items = items[0:3]
    print(f"New list: {items}")

    return 0


if __name__ == '__main__':
    sys.exit(main())