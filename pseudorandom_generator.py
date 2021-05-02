
m = 7829
a = 378
c = 2310
seed = 4321


def random_gen(m, a, c, seed, n):
    for i in range(n):
        seed = (seed * a + c) % m
        yield seed


for _ in random_gen(m, a, c, seed, 4):
    print(_)
