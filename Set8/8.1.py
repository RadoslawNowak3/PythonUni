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
          if(-c/b>0):
            print("x = ", -b/a, "* y", -c / a)
          else:
              print("x = ", -b / a, "* y +", -c / a)

print("Solution for  10x - 5y + 25 = 0: ")
solve1(10, -5, 25)