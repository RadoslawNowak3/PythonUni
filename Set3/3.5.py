length = int(input("Input measure length: "))
output = "|"
for i in range(length):
    output += "....|"
output += "\n"
for i in range(length + 1):
    output += '{:5}'.format(str(i))
print(output)