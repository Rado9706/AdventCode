from pathlib import Path
from typing import List

with open(str(Path("input.txt")), "r") as input:
    data = input.readline()
    floar = 0
    FirstHitBase: List[int] = []
    for index, char in enumerate(data, start=1):
        if char == "(":
            floar += 1
        else:
            floar -= 1
        if floar == -1 and len(FirstHitBase) == 0:
            FirstHitBase.append(index)

    print(floar)
    print(FirstHitBase[0])
