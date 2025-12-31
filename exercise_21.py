import sys

#Replace the second word in the list with string "UPDATED". Print the new list

def main():

    word_1 = input("Enter a word:")
    word_2 = input("Enter another word:")
    word_3 = input("Enter another word:")

    if word_1.isalpha() and word_2.isalpha() and word_3.isalpha():
        words = [word_1, word_2, word_3]

        print(f"List is: {words}")

        words[1] = "UPDATED"

        print(f"New list : {words}")

    else:
        print("Invalid Input; try again")

    return 0


if __name__ == '__main__':
    sys.exit(main())