class StringFind:
    vowels = "aeiou"
    dontContain = ["ab", "cd", "pq", "xy"]

    def __init__(self):
        self.vowelCounter = 0
        self.slidingTwoChars = []
        self.twiceSlide = []
        self.twiceSeen = False
        self.forbide = False

    def vowelsCounter(self) -> None:
        if self.char in StringFind.vowels:
            self.vowelCounter += 1

    def twiceRowOnly(self) -> None:
        if self.twiceSeen:
            return
        if len(self.twiceSlide) < 2:
            self.twiceSlide.append(self.char)
            return
        if self.twiceSlide[0] == self.twiceSlide[1]:
            self.twiceSeen = True
        else:
            self.twiceSlide = self.twiceSlide[1:]
            self.twiceSlide.append(self.char)

    def notContains(self) -> None:
        if self.forbide:
            return
        if len(self.slidingTwoChars) < 2:
            self.slidingTwoChars.append(self.char)
            return
        elif len(self.slidingTwoChars) == 2:
            checkTwo = self.slidingTwoChars[0] + self.slidingTwoChars[1]
            if any(checkTwo in substring for substring in StringFind.dontContain):
                self.forbide = True
            self.slidingTwoChars.append(self.char)
            self.slidingTwoChars = self.slidingTwoChars[1:]
            return
        else:
            raise AssertionError(
                "self.slidingTwoChars, should never be more than 2 valuees long"
            )

    def checkResults(self) -> bool:
        if self.forbide is True:
            return False
        if self.vowelCounter >= 3 and self.twiceSeen is True:
            return True
        else:
            return False

    def startChecking(self, char: str) -> bool:
        self.char = char
        self.vowelsCounter()
        self.twiceRowOnly()
        self.notContains()


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
