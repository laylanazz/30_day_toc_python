import sys


def main():

    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    country = input("Enter country of residence:")

    if name.istitle() and country.istitle():
        profile = [name, age, country]
        print(f"User's profile: {profile}")

        summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]
        print(f"User's updated profile: {summary}")

    else:
        print("Try again starting with a capital letter.")

    return 0


if __name__ == '__main__':
    sys.exit(main())