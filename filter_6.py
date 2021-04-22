def find_expressions(a):
    return (x for x in str(a).split("\n") if x.endswith(".ico") or x.endswith(".png"))

def generator_(x):
    for x in str(x).split("\n"):
        if x.endswith(".ico") or x.endswith(".png"):
            yield x


if __name__ == '__main__':
    string_a = """
      -rw-rw-r--@ 1 aeksei  staff  145466 Apr  6 16:00 about.jpg
      -rw-rw-r--@ 1 aeksei  staff  462484 Apr  6 16:00 bg_1.jpg
      -rw-rw-r--@ 1 aeksei  staff  749355 Apr  6 16:00 bg_2.jpg
      -rw-rw-r--@ 1 aeksei  staff  430425 Apr  6 16:00 bg_3.jpg
      -rw-rw-r--@ 1 aeksei  staff  180832 Apr  6 16:00 category-1.jpg
      -rw-rw-r--@ 1 aeksei  staff  136871 Apr  6 16:00 category-2.jpg
      -rw-rw-r--@ 1 aeksei  staff  105803 Apr  6 16:00 category-3.jpg
      -rw-rw-r--@ 1 aeksei  staff  275752 Apr  6 16:00 category-4.jpg
      -rw-rw-r--@ 1 aeksei  staff  150644 Apr  6 16:00 category.jpg
      -rw-rw-r--@ 1 aeksei  staff    1150 Apr  6 16:00 favicon.ico
      -rw-rw-r--@ 1 aeksei  staff  472014 Apr  6 16:00 image_1.jpg
      -rw-rw-r--@ 1 aeksei  staff   87628 Apr  6 16:00 image_2.jpg
      -rw-rw-r--@ 1 aeksei  staff  150561 Apr  6 16:00 image_3.jpg
      -rw-rw-r--@ 1 aeksei  staff   78138 Apr  6 16:00 image_4.jpg
      -rw-rw-r--@ 1 aeksei  staff  294523 Apr  6 16:00 image_5.jpg
      -rw-rw-r--@ 1 aeksei  staff  190534 Apr  6 16:00 image_6.jpg
      -rw-rw-r--@ 1 aeksei  staff   16287 Apr  6 16:00 partner-1.png
      -rw-rw-r--@ 1 aeksei  staff   27923 Apr  6 16:00 partner-2.png
      -rw-rw-r--@ 1 aeksei  staff   23647 Apr  6 16:00 partner-3.png
      -rw-rw-r--@ 1 aeksei  staff   32460 Apr  6 16:00 partner-4.png
      -rw-rw-r--@ 1 aeksei  staff   24751 Apr  6 16:00 partner-5.png
      -rw-rw-r--@ 1 aeksei  staff   36090 Apr  6 16:00 person_1.jpg
      -rw-rw-r--@ 1 aeksei  staff   47939 Apr  6 16:00 person_2.jpg
      -rw-rw-r--@ 1 aeksei  staff   35096 Apr  6 16:00 person_3.jpg
      -rw-rw-r--@ 1 aeksei  staff   25350 Apr  6 16:00 person_4.jpg
      -rw-rw-r--@ 1 aeksei  staff   56053 Apr  6 16:00 product-1.jpg
      -rw-rw-r--@ 1 aeksei  staff   60294 Apr  6 16:00 product-10.jpg
      -rw-rw-r--@ 1 aeksei  staff   46315 Apr  6 16:00 product-11.jpg
      -rw-rw-r--@ 1 aeksei  staff   40372 Apr  6 16:00 product-12.jpg
      -rw-rw-r--@ 1 aeksei  staff  130442 Apr  6 16:00 product-2.jpg
      -rw-rw-r--@ 1 aeksei  staff   95292 Apr  6 16:00 product-3.jpg
      -rw-rw-r--@ 1 aeksei  staff   78550 Apr  6 16:00 product-4.jpg
      -rw-rw-r--@ 1 aeksei  staff   60272 Apr  6 16:00 product-5.jpg
      -rw-rw-r--@ 1 aeksei  staff  143052 Apr  6 16:00 product-6.jpg
      -rw-rw-r--@ 1 aeksei  staff   68329 Apr  6 16:00 product-7.jpg
      -rw-rw-r--@ 1 aeksei  staff   37224 Apr  6 16:00 product-8.jpg
      -rw-rw-r--@ 1 aeksei  staff   55958 Apr  6 16:00 product-9.jpg
    """

    z = find_expressions(string_a)

    for _ in z:
        print(_)

    a = generator_(string_a)
    for _ in a:
        print(_)