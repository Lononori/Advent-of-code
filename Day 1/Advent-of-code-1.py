currentElf = 0
topElf = 0
secondElf =0
thirdElf =0
totalElf =0

with open('D:\Coding work\Calories.txt') as calories:
    for line in calories:
        item = line.strip()
        if item == '':
            if currentElf >= topElf:
                topElf = currentElf
            elif currentElf >= secondElf:
                secondElf = currentElf
            elif currentElf >= thirdElf:
                thirdElf = currentElf
            currentElf = 0
        elif item != '':
            currentElf += int(item)   
totalElf = topElf + secondElf + thirdElf
print(totalElf)
