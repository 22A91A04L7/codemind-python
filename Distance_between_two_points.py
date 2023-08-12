import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
d=math.sqrt((abs(x2-x1))**2+(abs(y2-y1))**2)
print(f"{d:.4f}")