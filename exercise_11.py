import sys

#Ask the user for a number representing minutes. Convert to hours (float) and print

def main():

    time_min = float(input("Enter time in minutes:"))
    time_hrs = time_min/60

    print(f"You entered {time_min} minutes which is {time_hrs} hours.")

    return 0


if __name__ == '__main__':
    sys.exit(main())