import sys


def main():

    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    city = input("Enter your city:")

    if name.istitle() and city.istitle():
        profile = dict(name=name, age=age, city=city)
        print(f"Profile: {profile}")
    else:
        print("Try again starting with a capital letter.")
    return 0


if __name__ == '__main__':
    sys.exit(main())