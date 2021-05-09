from random import randint, uniform
from geojson import Polygon
import geojson

def random_point(min_long=-180, max_long=180, min_lat=-90, max_lat=90):
    point = [round(uniform(min_long, max_long), 2), round(uniform(min_lat, max_lat), 2)]
    if -180 < point[0] - .5 < 180 and -180 < point[0] + 0.5 < 180:
        min_long = point[0] - .5
        max_long = point[0] + .5
    else:
        random_point()
    if -90 < point[1] - .5 < 90 and -90 < point[1] + 0.5 < 90:
        min_lat = point[1] - .5
        max_lat = point[1] + .5
    else:
        random_point()
    return min_long, max_long, min_lat, max_lat

a, b, c, d = random_point()
print(a, b, c, d)

def create_points(ct, min_long, max_long, min_lat, max_lat):
    return [[round(uniform(min_long, max_long), 2),round(uniform(min_lat, max_lat), 2)] for _ in range(ct)]


a = create_points(10, a, b, c, d)

p1 = Polygon([a])
for _ in range(5):
    print(_)

# with open("p1_test.geojson", "w") as f:
#     f.write(geojson.dumps(p1))