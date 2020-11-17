def fibonacci(n):
    if(n==0): return 0
    if(n==1): return 0
    n0 = 0
    n1 = 1
    for i in range(2, n+1):
        nth = n0+n1
        n0=n1
        n1=nth
    return nth

seq = int(input("Input sequence: "))
print(fibonacci(seq))