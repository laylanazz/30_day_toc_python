import sys


def main():

    num_1 = input("Enter a number:")
    num_2 = input("Enter another number:")
    num_3 = input("Enter another number:")

    numbers = [num_1, num_2, num_3]
    print(f"List of numbers: {numbers}")

    num_1 = int(numbers[0])
    num_2 = int(numbers[1])
    num_3 = int(numbers[2])
    numbers = [num_1, num_2, num_3]
    print(f"New list: {numbers}")

    print(f"Sum of the numbers: {sum(numbers)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())