f = open("input.txt","r")
inputs = []
for line in f.readlines():
    inputs.append(line.strip())

# print(inputs)

gamma = ""
epsilon = ""
for col in range(len(inputs[0])):
    vals = []
    for row in range(len(inputs)):
        vals.append(inputs[row][col])
    # print(vals)
    if(vals.count("1")>vals.count("0")):
        gamma+="1"
        epsilon+="0"
    else:
        gamma+="0"
        epsilon+="1"

gamma = int(gamma,2)
epsilon = int(epsilon,2)

print(gamma*epsilon)