print("If area of one wall of a cubical wooden box is 16 units, \
write a Python program to display the volume of the box. ")
import math
area=16
side=math.sqrt(area)
print("After calculating the square root of the wall area the side is",side)
volume=math.pow(side,3)
print('So the volume of the wall is',volume)
