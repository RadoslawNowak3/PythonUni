result = ""
height = int(input("Input rectangle height: "))
width = int(input("Input rectangle width: "))
for index in range(2*height+1):
    if(index %2==0):
        result+=width*("+---")+("+ \n")
    else:
        result+=width*("|   ")+("| \n")
print(result)