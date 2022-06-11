f = open("input.txt","r")

inputs = list(map(lambda x: int(x),f.readline().strip().split(",")))
# print(inputs)

fishes = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}
for input in inputs:
    fishes[input] += 1

days = 80 #256 for problem-2
for day in range(days):
    temp = fishes[0]
    for i in range(8):
        fishes[i] = fishes[i+1]
    fishes[6] += temp
    fishes[8] = temp
    # print(fishes)

print(sum(fishes.values()))