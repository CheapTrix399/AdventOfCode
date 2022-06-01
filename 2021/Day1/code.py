f = open("input.txt","r")
inputs = []
for line in f.readlines():
    inputs.append(line.strip())

# print(len(inputs))

#Code1
# counter = 0
# for i in range(1,len(inputs)):
#     if(int(inputs[i])>int(inputs[i-1])):
#         counter += 1
# print(counter)

#Code2
counter = 0
for i in range(1,len(inputs)-2):
    if((int(inputs[i])+int(inputs[i+1])+int(inputs[i+2]))>(int(inputs[i-1])+int(inputs[i])+int(inputs[i+1]))):
        counter += 1
print(counter)