import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
height=test_h
width= test_w
cover= coverage

def paint_calc(height,width,cover):
  area= height* width
  can_need = math.ceil(area/cover)
  print(f"you need {can_need}")


paint_calc(test_h, test_w, cover)
