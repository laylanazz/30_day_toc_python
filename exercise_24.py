import sys


def main():
    word_1 = input("Enter a word: ")
    word_2 = input("Enter another word: ")
    word_3 = input("Enter another word: ")
    word_4 = input("Enter another word: ")
    word_5 = input("Enter another word: ")

    words = [word_1, word_2, word_3, word_4, word_5]
    print(f"List of words: {words}")

    a_words = list()

    if word_1.startswith("a") or word_1.startswith("A"):
        a_words.append(word_1)
    if word_2.startswith("a") or word_2.startswith("A"):
        a_words.append(word_2)
    if word_3.startswith("a") or word_3.startswith("A"):
        a_words.append(word_3)
    if word_4.startswith("a") or word_4.startswith("A"):
        a_words.append(word_4)
    if word_5.startswith("a") or word_5.startswith("A"):
        a_words.append(word_5)

    print(f"New list: {a_words}")
    return 0


if __name__ == '__main__':
    sys.exit(main())