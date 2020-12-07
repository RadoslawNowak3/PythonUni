def solve1(a, b, c):
  if a == 0:
    if b == 0:
      if c == 0:
        print("identity equation")
      else:
        print("contradictory equation")
    else:
      if c == 0:
        print("y = 0")
      else:
        print("y = ", -c / b)
  else:
    if b == 0:
      if c == 0:
        print("x = 0")
      else:
        print("x = ", -c / a)
    else:
      if c == 0:
        print("x = ",-b/a, "* y")
      else:
          if(c>0):
            print("x = ", -b/a, "* y", -c / b)
          else:
              print("x = ", -b / a, "* y +", -c / b)

x = float(input("Enter x"))
y = float(input("Enter y"))
z = float(input("Enter z"))
print("Solution for equation 5x + 10y + 50 = 0: ")
solve1(x, y, z)