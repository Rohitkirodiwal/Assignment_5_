class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqrSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z

        return(a+b+c)
point_obj1 = Point(1,3,5)
print(point_obj1.sqrSum())