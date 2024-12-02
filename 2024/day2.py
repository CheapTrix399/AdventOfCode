# inp = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""
with(open("inputs/day2.txt","r") as file):
    inp = file.read()

reports = inp.split("\n")

def check_safety(levels):
    is_safe = True
    trend = None
    for index in range(len(levels)):
        levels[index] = int(levels[index])
        if(index==0):
            continue
        diff = levels[index] - levels[index-1]
        if((abs(diff)<1) or (abs(diff)>3)):
            is_safe = False
            break
        if(trend is None):
            if(diff>0):
                trend = "inc"
            elif(diff<0):
                trend = "dec"
            else:
                is_safe = False
                break
        else:
            if(trend == "inc"):
                if(diff<=0):
                    is_safe = False
                    break
            if(trend == "dec"):
                if(diff>=0):
                    is_safe = False
                    break
    return is_safe

safe_count = 0
for report in reports:
    levels = report.split(" ")
    is_safe = check_safety(levels)
    if(is_safe):
        safe_count += 1

print(safe_count)

## Part-2

safe_count = 0
for report in reports:
    levels = report.split(" ")
    is_safe = check_safety(levels)
    if(is_safe):
        safe_count += 1
    else:
        is_safe_again = False
        for index in range(len(levels)):
            copy_levels = levels.copy()
            copy_levels.pop(index)
            if(check_safety(copy_levels)):
                is_safe_again = True
                break
        if(is_safe_again):
            safe_count += 1

print(safe_count)