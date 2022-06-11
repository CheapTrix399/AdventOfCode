f = open("input.txt","r")
marked_nums = []
bingos = []
bingo = []
for line in f.readlines():
    temp = line.strip().split(",")
    if(len(temp)==1):
        if(temp[0]==""):
            if(bingo != []):
                bingos.append(bingo)
            bingo = []
        else:
            nums = line.strip().split()
            # print(nums)
            nums = list(map(lambda n: int(n),nums))
            bingo.append(nums)
    else:
        marked_nums = list(map(lambda n: int(n),temp))
bingos.append(bingo)

def bingo_wins(bingo,inputs):
    for row in range(len(bingo)):
        for col in range(len(bingo[0])):
            if(bingo[row][col] in inputs):
                bingo[row][col] = "x"
    bingo_wins = 0
    if((["x"]*len(bingo[0])) in bingo):
        bingo_wins = 1
    for col in range(len(bingo[0])):
        counter = 0
        for row in range(len(bingo)):
            if(bingo[row][col]=="x"):
                counter += 1
        if(counter == len(bingo)):
            bingo_wins = 1
    # print(bingo)
    if(bingo_wins == 1):
        sum = 0
        for row in range(len(bingo)):
            for col in range(len(bingo[0])):
                if(bingo[row][col] != "x"):
                    sum += bingo[row][col]
        return sum
    else:
        return None

inputs = []
final = None
for i in marked_nums:
    # print(bingos)
    inputs.append(i)
    # print(inputs)
    for bingo in bingos:
        result = bingo_wins(bingo,inputs)
        if(result != None):
            final = i*result
    if(final != None):
        print(final)
        break