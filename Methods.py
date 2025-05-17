# #methods

class Circle(object):
    def __init__(self,center,radius):
        if type(center)!= Coordinate:
            raise ValueError
        if type(radius)!=int:
            raise ValueError
        self.center=center
        self.radius=radius
    def is_inside(self,point):
        return point.distance(self.center)<self.radius
class Coordinate(object):
    def __init__(self,xval,yval):
        self.x=xval
        self.y=yval 
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    def __str__(self):
        return "<"+str(self.x)+str(self.y)+">"
       
center=Coordinate(3,4)
my_circle=Circle(center, 4)
p=Coordinate(2,3)
# my_circle=Circle(center, 2.0)      #throws value error
# my_circle=Circle(center, 'dfgh')
print(my_circle.is_inside(p))




class Simplef(object):
    def __init__(self,a,b):
        self.num=a
        self.deno=b
    def times(self,other):
        top=self.num * other.num
        bottom=self.deno * other.deno
        return top/bottom
    def plus(self,other):
        top=(self.num * other.deno)+(self.deno * other.num)
        bottom=self.deno * other.deno
        return top/bottom

f1=Simplef(3,4)
f2=Simplef(1,4)
print(f1.num)
print(f1.deno)
print(f1.plus(f2)) 
print(f1.times(f2))



class Fraction(object):
    def __init__(self,num,deno):
        self.num=num
        self.deno=deno
    def reduce(self):
        def gcd(n,d):
            while(d!=0):
                (d,n)=(n%d,d)
            return n
        if self.deno==0:
            return None
        elif self.deno==1:
            return Fraction(self.num,1)
        else:
            gcd=gcd(self.num,self.deno)
            top=int(self.num/gcd)
            bottom=int(self.deno/gcd)
            return Fraction(top,bottom)
            
    def __str__(self):
        if (self.deno==1):
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.deno)
    def __mul__(self,other):
        top=self.num * other.num
        bottom=self.deno * other.deno
        return Fraction(top,bottom)
f1=Fraction(3,1)
print(f1)
a=Fraction(1,4)
b=Fraction(2,3)
c=a*b
print(c)
print(c.reduce())













