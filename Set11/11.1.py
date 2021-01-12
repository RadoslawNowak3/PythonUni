import random
import math
def random_int(N):
    numbers = []
    for i in range(0, N):
        numbers.append(i)
    random.shuffle(numbers)
    return numbers

def almost_sorted_int(N):
    numbers = []
    for i in range(0, N):
        numbers.append(i)
    for i in range(1, N):
        j = random.randint(i - 1, i)
        numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

def almost_sorted_int_reversed(N):
    numbers = almost_sorted_int(N)
    numbers.reverse()
    return numbers

def gaussian_int(N):
    numbers = []
    for i in range(N):
        numbers.append(random.gauss(0, 1))
    return numbers

def repeating_int(N):
    numbers = []
    for i in range(N):
        numbers.append(random.randint(0, math.floor(math.sqrt(N))))
    random.shuffle(numbers)
    return numbers

print(random_int(50))
print(almost_sorted_int(50))
print(almost_sorted_int_reversed(50))
print(gaussian_int(50))
print(repeating_int(50))