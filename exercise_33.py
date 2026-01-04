import sys


def main():

    person = {"name": "Alice", "age": 25, "country": "Kenya"}
    print(f"Person: {person}")

    person["is_student"] = False
    print(f"Updated: {person}")

    return 0


if __name__ == '__main__':
    sys.exit(main())