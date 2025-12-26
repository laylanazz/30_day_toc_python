import sys

#Ask the user for their age. Print whether they are at least 18 (True/False).

def main():

    age = int(input("Enter your age:"))

    print(age >= 18)


    return 0


if __name__ == '__main__':
    sys.exit(main())