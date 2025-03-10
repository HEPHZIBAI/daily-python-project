import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def falls_in_rectangel(self,lower,upper):
        if lower[0]<self.x<upper[0] and lower[1]<self.y<upper[1]:
            print(True)
        else:
            print(False) 
    def distance(self,x1,y1):
        x=(x1-self.x)**2
        y=(y1-self.y)**2
        print(math.sqrt(x+y))


point1=Point(3,4)
point1.falls_in_rectangel((5,6),(7,9))
point1.distance(4,5)
point2=Point(6,8)
point2.falls_in_rectangel((5,6),(7,9))
point2.distance(4,5)