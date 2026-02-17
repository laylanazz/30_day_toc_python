import sys


def main():

    name = input("Enter your name:")
    birth_year = int(input("Enter year of birth:"))
    country = input("Country:")

    profile = dict(name = name , birth_year = birth_year, country = country)


    summary = {"NAME": profile["name"].upper(),
               "age_in_2025":2025 - profile["birth_year"],
               "country" : profile["country"].lower()}

    print(f"Profile:{profile}")
    print(f"Summary:{summary}")

    return 0


if __name__ == '__main__':
    sys.exit(main())