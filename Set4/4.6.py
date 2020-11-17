def sum_seq(sequence):
    sum = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            sum += sum_seq(i)
        else:
            sum += i
    return sum

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(sum_seq(seq))