pts = [
    (3, 4),
    (4.5, 3),
    (2.1, -1),
    (6.8, -3),
    (1.4, 2.9)
]
# ((x1-x0) ** 2  + (y1-y0) ** 2) ** 0.5


def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]


a = pairwise(pts)
# for _ in a:
#     print(_)
b = ((j[0] - j[1], k[0] - k[1]) for j, k in a)
for _ in b:
    print(_)



print(sum(map(lambda point: (point[0] ** 2 + point[1] ** 2) ** 0.5, b)))

# for j, k in a:
#     print((j[0] - j[1], k[0] - k[1]))
#
# def get_distance(point):
#     x = point[0]
#     y = point[1]
#     return (x ** 2 + y ** 2) ** 0.5