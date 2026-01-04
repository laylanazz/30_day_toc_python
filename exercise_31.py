import sys


def main():

    person = {"name": "Alice", "age": 25, "country": "Kenya"}
    print(f"Person: {person}")

    print(f"Name: {person["name"]}")
    print(f"Age: {person["age"]}")

    return 0


if __name__ == '__main__':
    sys.exit(main())