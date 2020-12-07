from time import *
P = {
  (0, 0): 0.5,
  (0, 1): 1,
  (1, 0): 0
}


def rec(i, j):
    if i==0:
        if j==0:
            return P.get((0, 0))
        return P.get((1, 0))
    if j==0:
        return P.get((0, 1))
    else:
        return 0.5 * (rec(i - 1, j) + rec(i, j - 1))


def dp(i, j):
    if i==0:
        if j==0:
             return P.get((0, 0))
        return P.get((1, 0))
    if j==0:
        return P.get((0, 1))
    else:
        P[(i, j)] = 0.5 * (dp(i - 1, j) + dp(i, j - 1))
    return P.get((i, j))


start = time()
recval = rec(15, 9)
end = time()
start2 = time()
dpval = dp(15, 9)
end2 = time()
timerec = end-start
timedp=end2-start2
print("Results for recursion - value: ", recval, "time:", timerec,"s")
print("Results for dynamic programming - value:", dpval, "time:", timedp,"s")
if(timerec<timedp):
    print("Recursion is faster by:", timedp - timerec, "s")
else:
    print("Dynamic programming is faster by:", timerec - timedp, "s")
