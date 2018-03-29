class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line:
    def __init__(self, point1, point2):
        self.m = (point2.y - point1.y) / (point2.x - point1.x)
        self.b = point2.y - self.m * point2.x

def intersect(line1, line2):
    if line1.m == line2.m and line1.b != line2.b:
        return "They'll never intersect"
    elif line1.m == line2.m and line1.b == line2.b:
        return "They are the same line"
    else:
        x = (line2.b - line1.b) / (line2.m - line1.m)
        y = line1.m * x + line1.b
        return point(x, y)

def main ():
    line1 = line(point(3,4), point(15,16))
    line2 = line(point(3,6), point(19,33))
    # line2 = line(point(3,4), point(15,16))
    point3 = intersect(line1, line2)
    # print(point3)
    print("{} {}".format(point3.x, point3.y))

main()
