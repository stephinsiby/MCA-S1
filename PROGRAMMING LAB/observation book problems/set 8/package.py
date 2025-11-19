import Graphics
from Graphics import Circle, Rectangle
from Graphics.threeDGraphics import Cuboid, Sphere
from Graphics.Circle import  *
rad1 = float(input("Enter the radius of the circle: "))
print("Area of the circle is:", Circle.area_circle(rad1))
print("Perimeter of the circle is:", Circle.perimeter_circle(rad1))

len1 = float(input("Enter the length of the rectangle: "))
breadth1 = float(input("Enter the breadth of the rectangle: "))
print("Perimeter of the rectangle is:", Rectangle.perimeter_rec(len1, breadth1))

len2 = float(input("Enter the length of the cuboid: "))
breadth2 = float(input("Enter the breadth of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
print("Area of the cuboid is:", Cuboid.area_cuboid(len2, breadth2, height))
print("Perimeter of the cuboid is:", Cuboid.perimeter_cuboid(len2, breadth2, height))

rad2 = float(input("Enter the radius of the sphere: "))
print("Area of the sphere is:", Sphere.area_sphere(rad2))
print("Perimeter of the sphere is:", Sphere.perimeter_sphere(rad2))



