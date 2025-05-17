# python classes
class Coordinate(object):
    def __init__(self,xval,yval):
        self.x=xval
        self.y=yval
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
        
c=Coordinate(3, 4)
origin=Coordinate(0,0)
print(c.x,c.y)
print(origin.x)
print(c.distance(origin))    #conventional way


# # equivalent way
# c=Coordinate(3, 4)
# zero=Coordinate(0, 0)
# print(Coordinate.distance(c,zero))








