from datetime import datetime

with open("inputs/day1_bigboy.txt", "r") as text:
    inp = text.read()

start = datetime.now()

first_list = []
second_list = []

left_repeats = {

}

numbers = inp.split("\n")
for pair in numbers:
    pair_l, pair_r = pair.split("   ")
    first_list.append(int(pair_l))
    second_list.append(int(pair_r))
    if(int(pair_r) not in left_repeats.keys()):
        left_repeats[int(pair_r)] = 1
    else:
        left_repeats[int(pair_r)] += 1

### Part-1

first_list.sort()
second_list.sort()

diff = 0
for index in range(len(first_list)):
    diff += abs(first_list[index] - second_list[index])

print(diff)

##### Part-2

sim_score = 0
for number in first_list:
    if(number in left_repeats.keys()):
        sim_score += number*left_repeats[number]

print(sim_score)

end = datetime.now()
print(end-start)