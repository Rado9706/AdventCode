class StringFind:
    vowels = "aeiou"
    dontContain = ["ab", "cd", "pq", "xy"]

    def __init__(self):
        self.vowelCounter = 0
        self.twiceSeen = False
        self.forbide = False
        self.prev_char = ""
        self.prev_prev_char = ""

    def startChecking(self, char: str) -> None:
        if self.forbide:
            return

        if char in StringFind.vowels:
            self.vowelCounter += 1

        if char == self.prev_char:
            self.twiceSeen = True

        if self.prev_prev_char + self.prev_char in StringFind.dontContain:
            self.forbide = True

        self.prev_prev_char = self.prev_char
        self.prev_char = char

    def checkResults(self) -> bool:
        return not self.forbide and self.vowelCounter >= 3 and self.twiceSeen


from time import time

start = time()
with open("/home/rado/personal/AdventCode/2015/day5/input.txt") as inputIO:
    data = inputIO.readlines()
    nice = 0
    for string in data:
        strFinder = StringFind()
        string = string.strip("\n") + " "
        for char in string:
            strFinder.startChecking(char)
        if strFinder.checkResults():
            nice += 1
    print(nice)
end = time()

print(end - start)
