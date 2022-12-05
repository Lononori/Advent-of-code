def rpsYou(item):
    if 'X' in item:
        return 1
    elif 'Y' in item:
        return 2
    elif 'Z' in item:
        return 3
    else:
        return 0

def rpsLogic(num, item):
    if 'A' in item:
        match num :
            case 1 :
                return 3
            case 2 :
                return 4
            case 3 :
                return 8
    elif 'B' in item:
        match num :
            case 1 :
                return 1
            case 2 :
                return 5
            case 3 :
                return 3 + 6
    elif 'C' in item:
        match num :
            case 1 :
                return 2
            case 2 :
                return 3+3
            case 3 :
                return 1 + 6
    else:
        return 0
totalScore = 0
with open ("/home/nori/Random-code/Advent-of-code/Day-2/Rock-Paper-Scissors") as cheatSheet:
    for line in cheatSheet:
        line.strip()
        temp =0
        temp = rpsYou(line)
        temp = rpsLogic(temp,line)
        totalScore = totalScore + temp
        

    print(totalScore)


