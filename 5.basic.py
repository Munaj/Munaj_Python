class Triangle:

     def __init__(self, angle1, angle2, angle3):
         self.angle1 = angle1
         self.angle2 = angle2
         self.angle3 = angle3
         self.number_of_sides = 3

     def __eq__(self, other):
         return self.angle1 + self.angle2 + self.angle3 == \
   	    other.angle1 + other.angle2 + other.angle3
    
     def check_angles(self):
         return (self.angle1 + self.angle2 + self.angle3) == 180

if __name__ == "__main__":
     t1 = Triangle(30, 60, 90)
     t2 = Triangle(10, 80, 80)

     print(t1.number_of_sides)
     print(t2.number_of_sides)

     print(t1.check_angles())
     print(t2.check_angles())

     print(t1 == t2)
