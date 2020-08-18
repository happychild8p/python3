#!/usr/bin/python3
def calc_area(radius):
    result = 3.14 * (radius**2)
    return result

def calc_area2():
    global area, r
    area = (3.14 * (r**2))

def calc_area3():
    print(r)
    area = 3.14 * r**2
    return area

def calc_area4():
    area = 3.14 * r**2

if __name__ == "__main__":
    area = 0
    r = float(input("Enter the radius of a circle: "))
    calc_area4()
    print(area)
