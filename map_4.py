if __name__ == '__main__':
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(max(map(len, list_words)))

    print(max([len(x) for x in list_words]))