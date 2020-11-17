result = []

def flatten(seq):
    for i in seq:
        if isinstance(i, (list, tuple)):
            flatten(i)
        else:
            result.append(i)
    return result
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))