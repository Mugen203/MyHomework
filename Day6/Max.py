list = []

def Max(list):
    cur_max = list[0]

    for i in list:
        if i > cur_max:
            cur_max = i
    return cur_max

print(Max([23,5,133,34,65,89,123,432]))
