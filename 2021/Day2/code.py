f = open("input.txt","r")
inputs = []
for line in f.readlines():
    inputs.append(line.strip().split(" "))

# print(inputs)
x = 0
y = 0
aim = 0

for command in inputs:
    if(command[0]=="forward"):
        x += int(command[1])
        y += aim*int(command[1])
    if(command[0]=="down"):
        aim += int(command[1])
    if(command[0]=="up"):
        aim -= int(command[1])

print(x*y)