import sys

#Print the result of data.values().
def main():

    data = {"a": 1, "b": 2, "c": 3}
    print(f"Data : {data}")

    print(data.values())

    return 0


if __name__ == '__main__':
    sys.exit(main())