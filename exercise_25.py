import sys


def main():

    nums = [1, 2, 3]
    print(f"nums: {nums}")

    nums.append(4)
    print(f"After appending, nums: {nums}")

    return 0


if __name__ == '__main__':
    sys.exit(main())