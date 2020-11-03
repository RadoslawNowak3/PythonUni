while(True):
   x=input("Wprowadz liczbe lub wpisz stop by zatrzymac dzialanie programu")
   if x == "stop":
       break
   else:
    try:
        floatx = float(x)
    except ValueError:
        print("Not a number")
    else:
        for i in range(3):
            print(x)
            print(float(x)**3)


