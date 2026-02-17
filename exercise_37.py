import sys

#Print the number of key–value pairs
def main():

    data = {"a": 1, "b": 2, "c": 3}
    print(f"Data:{data}")

    print(f"Number of key-value pairs : {len(data)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())