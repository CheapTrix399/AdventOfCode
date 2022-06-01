f = open("input.txt","r")
inputs = []
for line in f.readlines():
    inputs.append(line.strip())

inputs_copy = inputs.copy()
# print(inputs)
position = 0
while(len(inputs)>1):
    vals = []
    for row in range(len(inputs)):
        vals.append(inputs[row][position])
    # print(vals)
    newinputs = []
    if(vals.count("1")>=vals.count("0")):
        for row in inputs:
            if(row[position]=="1"):
                newinputs.append(row)
    else:
        for row in inputs:
            if(row[position]=="0"):
                newinputs.append(row)
    position += 1
    inputs = newinputs
    # print(inputs)
o2 = inputs[0]
inputs = inputs_copy

position = 0
while(len(inputs)>1):
    vals = []
    for row in range(len(inputs)):
        vals.append(inputs[row][position])
    # print(vals)
    newinputs = []
    if(vals.count("1")<vals.count("0")):
        for row in inputs:
            if(row[position]=="1"):
                newinputs.append(row)
    else:
        for row in inputs:
            if(row[position]=="0"):
                newinputs.append(row)
    position += 1
    inputs = newinputs
co2 = inputs[0]

print(int(o2,2)*int(co2,2))