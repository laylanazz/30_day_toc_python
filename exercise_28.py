import sys


def main():

    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    num_3 = int(input("Enter third number: "))
    num_4 = int(input("Enter fourth number: "))

    nums = [num_1, num_2, num_3, num_4]
    print(f"List: {nums}")

    nums[0] = (nums[0])**2
    nums[3] = (nums[3])**3
    print(f"New list: {nums}")

    print(f"Sum of all the integers: {sum(nums)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())