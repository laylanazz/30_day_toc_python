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

    if words[0].startswith("a") or words[0].startswith("A"):
        a_words.append(words[0])
    if words[1].startswith("a") or words[1].startswith("A"):
        a_words.append(words[1])
    if words[2].startswith("a") or words[2].startswith("A"):
        a_words.append(words[2])
    if words[3].startswith("a") or words[3].startswith("A"):
        a_words.append(words[3])
    if words[4].startswith("a") or words[4].startswith("A"):
        a_words.append(words[4])

    print(f"New list: {a_words}")
    return 0


if __name__ == '__main__':
    sys.exit(main())