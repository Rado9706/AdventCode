class StringFind:
    vowels = "aeiou"
    dontContain = ["ab", "cd", "pq", "or" "xy"]

    def __init__(self):
        self.vowelCounter = 0
        self.slidingTwoChars = []
        self.charCount = {}
        self.twiceSeen = False
        self.forbide = False

    def vowelsCounter(self) -> None:
        if self.char in StringFind.vowels:
            self.vowelCounter += 1

    def twiceRow(self) -> None:
        self.charCount.setdefault(self.char, 0)
        self.charCount[self.char] += 1

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

    def checkResults(self) -> bool:
        for value in self.charCount.values():
            if value == 2:
                self.twiceSeen = True

        if self.vowelCounter >= 3 and self.twiceSeen is True and self.forbide is False:
            return True
        else:
            return False

    def startChecking(self, char: str) -> bool:
        self.char = char
        self.vowelsCounter()
        self.twiceRow()
        self.notContains()


with open("/home/rado/personal/AdventCode/2015/day5/input.txt") as inputIO:
    data = inputIO.readlines()
    nice = 0
    for string in data:
        strFinder = StringFind()
        string = string.strip("\n")
        for char in string:
            strFinder.startChecking(char)
        if strFinder.checkResults():
            nice += 1
    print(nice)
