from pathlib import Path
from typing import List

with open(
    str(Path("/home/rado/personal/AdventCode/2015/day2/input.txt")), "r"
) as input:
    data = input.readlines()
    for boxDimention in data:
        boxDimention = boxDimention.strip("\n")
        dimentionList: List[str] = boxDimention.split("x")
        pass
