def get_distance(point):
    x = point[0]
    y = point[1]
    return (x ** 2 + y ** 2) ** 0.5


if __name__ == '__main__':
    pts = [
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    print(f"Max point {max(map(get_distance, pts))}")

    print(max([((x ** 2 + y ** 2) ** 0.5) for x, y in pts]))
