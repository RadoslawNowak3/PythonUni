romanArray = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# zakladam, ze uzytkownik poprawnie zapisuje liczby rzymskie, bo nie mam pomyslu jak sprawdzac poprawnosc wprowadzonej
# liczby bez wielu, brzydkich ifow
# jedna z instrukcji warunkowych ktora probowalem weryfikowac liczby
# if i+2 < len(string):
#    if romanArray[string[i]]<=romanArray[string[i+1]] and romanArray[string[i+1]] < romanArray[string[i+2]]:
#       return False
def checkIfRoman(string):
    string = string.upper()
    for letters in string:
        if letters not in romanArray:
            return False
    return True
def roman2int(string):
    if checkIfRoman(string) is False:
        print("Not a roman number")
        return
    else:
        i=0
        result=0
        string = string.upper()
        while(i<len(string)):
            if(i+1 <len(string) and romanArray[string[i]]<romanArray[string[i+1]]):
                result+=romanArray[string[i+1]]-romanArray[string[i]]
                i+=2
            else:
                result+=romanArray[string[i]]
                i+=1
        return result

print(roman2int("MDII"))
print(roman2int("XD"))
print(roman2int("DX"))
print(roman2int("I"))
print(roman2int("ZDII"))
print(roman2int("123DII"))
