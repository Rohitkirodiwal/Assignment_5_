# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def sqrSum(self):
#         a = self.x * self.x
#         b = self.y * self.y
#         c = self.z * self.z

#         return(a+b+c)
# point_obj1 = Point(1,3,5)
# print(point_obj1.sqrSum())

# Challenge 1: Square Numbers and Return Their Sum

class Point :
        
        
    def __init__(self):
        self.x=int(input("enter first number"))
        self.y=int(input("enter second number"))
        self.z=int(input("enter third number"))
        
    def sqSum(self):

        a=self.x*2+self.y*2+self.z*2
        return a
    
     
obj=Point()
print(obj.sqSum())