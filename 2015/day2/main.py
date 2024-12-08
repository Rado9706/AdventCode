from pathlib import Path
from typing import List

with open(
    str(Path("/home/rado/codes/AdventCode/2015/day2/input.txt")), "r"
) as input:
    data = input.readlines()
    area: int = 0
    ribbonTotal: int = 0
    for boxDimention in data:
        boxDimention = boxDimention.strip("\n")
        dimentionList: List[str] = boxDimention.split("x")
        #dimentionList = ["2","3","4"]
        areaminList: List[int] = []
        areaRow: int = 0
        ribbonRow: int = 1
        for i in range(len(dimentionList)):
            ribbonRow *= int(dimentionList[i])
            areaRow += 2 * int(dimentionList[i]) * int(dimentionList[(i + 1)%len(dimentionList)])
            areaminList.append(int(dimentionList[i]))
        areaminList.sort()   
        areaRow += areaminList[0] * areaminList[1]
        ribbonRow += 2 * (areaminList[0] + areaminList[1])
        area += areaRow
        ribbonTotal += ribbonRow
    print(area)
    print(ribbonTotal)
