side1 = float(input("What is the length of side 1?: "))
side2 = float(input("What is the length of side 2?: "))
side3 = float(input("What is the length of side 3?: "))
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print("The area of the triangle is:", area,)
