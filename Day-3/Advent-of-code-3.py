def order(thing):
    if thing.isupper():
        return ord(thing) - 38
    if thing.islower():
        return  ord(thing) - 96
    return 0
total = 0

with open("/home/nori/Random-code/Advent-of-code/Day-3/Rucksack.txt") as Rucksack:
    for line in Rucksack:
        line.replace ("\n","")
        n = len(line)
        compartment1 = line[:n//2]
        compartment2 = line[n//2:]
        items =[]
        for item in compartment1:
            for jitem in compartment2:
                if item == jitem and not item in items:
                    items.append(item)
                    break
        for item in items:
            total += order(item)

#print(items)
print(len(items))
print(total)