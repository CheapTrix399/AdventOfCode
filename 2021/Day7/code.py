f = open("input.txt","r")

inputs = list(map(lambda x: int(x),f.readline().strip().split(",")))

# print(inputs)
min_sum = None
for pivot in set(inputs):
    summ = 0
    for i in inputs:
        summ += abs(pivot-i)
    if(min_sum != None):
        if(min_sum>summ):
            min_sum = summ
    else:
        min_sum = summ

print(min_sum)