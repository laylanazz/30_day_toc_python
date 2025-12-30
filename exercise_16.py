import sys

#Create a variable x = None. Print it. Ask the user to then assign a value to x via input. Print the new value
def main():

    x = None
    print(f"Value of x is: {x}")

    x = input("Enter a value:")
    print(f"New value of x is: {x}")

    return 0


if __name__ == '__main__':
    sys.exit(main())