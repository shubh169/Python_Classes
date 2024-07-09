import math

def area(h,w,c):
    can=math.ceil((h*w)/c)
    print(f"you will need {can} cans of paint")

height=float(input("Enter your height?:"))
width=float(input("Enter your width? :"))
coverage_per_can=5
area(height,width,coverage_per_can)