def draw_measure(length):
    output = "|"
    for i in range(length):
        output += "....|"
    output +="\n"
    for i in range(length+1):
     output+= '{:5}'.format(str(i))
    return output

def draw_rectangle(height, width):
    result = ""
    for index in range(2*height+1):
        if(index %2==0):
            result+=width*("+---")+("+ \n")
        else:
            result+=width*("|   ")+("| \n")
    return result
print("Measure draw:")
length = int(input("Input measure length: "))
print(draw_measure(length))

print("Rectangle draw:")
height = int(input("Input rectangle height: "))
width = int(input("Input rectangle width: "))
print(draw_rectangle(height,width))