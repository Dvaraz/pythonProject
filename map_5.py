if __name__ == '__main__':
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(list(map(str.upper, list_words)))

    for word in map(str.upper, list_words):
        print(word)