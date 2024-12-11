from math import sqrt
print("---CALCULATOR---")
operator = input("Operator (x, +, -, /, ^, h, sqrt, cbrt,\nafr, aft, vcfc, vcft ")
if operator == "x":
  print("---Multiplier---")
  fnx = int(input("First number: "))
  snx = int(input("Second number: "))
  print(f"The answer is: {fnx*snx}")
elif operator == "+":
  print("---Adder---")
  fnplus = int(input("First number: "))
  snplus = int(input("Second number: "))
  print(f"The answer is: {fnplus+snplus}")
elif operator == "-":
  print("---Subtractor---")
  fnminus = int(input("First number: "))
  snminus = int(input("Second number: "))
  print(f"The answer is: {fnminus-snminus}")
elif operator == "/":
  print("---Divider---")
  fnd = int(input("Divisor: "))
  snd = int(input("Dividend: "))
  print(f"The answer is: {snd/fnd}")
elif operator == "^":
  coe = int(input("Coefficient: "))
  ind = int(input("Index: "))
  print(f"The answer is: {coe**ind}")
elif operator == "h":
  print("---Hypotenuse finder---")
  base = int(input("Base of right-angle triangle: "))
  height = int(input("Height of right angle triangle: "))
  print(f"The hypotenuse is: {sqrt(height**2 + base**2)}")
elif operator == "sqrt":
  print("---Square root finder---")
  sqt = int(input("Number: "))
  print(f"The answer is: {sqrt(sqt)}")
elif operator == "cbrt":
  print("---Cube root finder---")
  cbt = int(input("Number: "))
  print("The cubic root is",
      round(cbt**(1/3), 6))
elif operator == "afr":
  print("---Area finder for rectangles---")
  length = int(input("Length: "))
  width = int(input("Width: "))
  print(f"The area is: {length*width}")
elif operator == "aft":
  aotf = 1/2
  print("---Area finder for triangles---")
  heightt = int(input("Height: "))
  baset = int(input("Base: "))
  print(f"The area is: {aotf*heightt*baset}")
elif operator == "vcfc":
  print("---Volume calculator for cuboids---")
  lengthvr = int(input("Length: "))
  widthvr = int(input("Width: "))
  heightvr = int(input("Height: "))
  print(f"The volume is: {lengthvr*widthvr*heightvr}")
elif operator == "vcft":
  print("---Volume calculator for triangles---")
  tvol = 1/2
  basevt = int(input("Length: "))
  heightvt = int(input("Width: "))
  lengthvt = int(input("Height: "))
  print(f"The volume is: {tvol*basevt*heightvt*lengthvt}")
else:
  print("Invalid operator!")