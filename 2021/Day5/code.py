f = open("input.txt","r")
lines = []
max_x = -1
max_y = -1
for line in f.readlines():
    temp = line.split("->")
    temp[0] = list(map(lambda a: int(a),temp[0].split(",")))
    temp[1] = list(map(lambda a: int(a),temp[1].split(",")))
    if(temp[0][0]>max_x):
        max_x = temp[0][0]
    if(temp[0][1]>max_y):
        max_y = temp[0][1]
    if(temp[1][0]>max_x):
        max_x = temp[1][0]
    if(temp[1][1]>max_y):
        max_y = temp[1][1]
    lines.append(temp)

matrix = []
for x in range(max_y+1):
    temp = []
    for y in range(max_x+1):
        temp.append(0)
    matrix.append(temp)

for line in lines:
    if(line[0][0] == line[1][0]):
        x_min = min(line[0][1],line[1][1])
        x_max = max(line[0][1],line[1][1])
        for x in range(x_min,x_max+1):
            matrix[x][line[0][0]] += 1
            # if(matrix[x][line[0][0]] > answer):
            #     answer = matrix[x][line[0][0]]
    if(line[0][1] == line[1][1]):
        y_min = min(line[0][0],line[1][0])
        y_max = max(line[0][0],line[1][0])
        for y in range(y_min,y_max+1):
            matrix[line[0][1]][y] += 1
            # if(matrix[line[0][1]][y] > answer):
            #     answer = matrix[line[0][1]][y]

answer = 0
for row in matrix:
    for i in row:
        if(i>=2):
            answer += 1
print("Answer: ",answer)