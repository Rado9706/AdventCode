from pathlib import Path
from typing import List, Tuple, Set

class SantaMovement:
    def __init__(self):
        self.currX: int = 0
        self.currY: int = 0
        self.histUniqueAddress: Set[Tuple[int, int]] = set()

    def getCurrPosition(self) -> Tuple[int, int]:
        return (self.currX, self.currY)
    
    def addToUniqueHistory(self, address: Tuple[int, int]) -> None:
        self.histUniqueAddress.add(address)
    
    def MoveNorth(self) -> None:
        self.currX += 1
    
    def MoveSouth(self) -> None:
        self.currX -= 1
    
    def MoveWest(self) -> None:
        self.currY -= 1
    
    def MoveEast(self) -> None:
        self.currY += 1
    
    def MoveController(self, instruction: str) -> None:
        if instruction == "^":
            self.MoveNorth()
        elif instruction == "v":
            self.MoveSouth()
        elif instruction == "<":
            self.MoveWest()
        else:
            self.MoveEast()

with open("/home/rado/codes/AdventCode/2015/day3/input.txt") as inputIO:
    data = inputIO.read()

SantaPath = SantaMovement()
RoboSanta = SantaMovement()
      
for index, move in enumerate(data):
    if index % 2 == 0:
        SantaPath.MoveController(move)
        address = SantaPath.getCurrPosition()
        SantaPath.addToUniqueHistory(address)
    else:
        RoboSanta.MoveController(move)
        address = RoboSanta.getCurrPosition()
        RoboSanta.addToUniqueHistory(address)


SantaPath.histUniqueAddress.update(RoboSanta.histUniqueAddress)
print(len(SantaPath.histUniqueAddress)+1)