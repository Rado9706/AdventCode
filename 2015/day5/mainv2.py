# also works but diffrent approch
from time import time


def checkBruteForce(string: str) -> bool:
    dontContain = ["ab", "cd", "pq", "xy"]
    twiceSeen = 0
    vowesCount = 0
    vowels = "aeiou"
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            twiceSeen += 1
        checkTwo = string[i] + string[i + 1]
        if any(checkTwo in substring for substring in dontContain):
            return False

        if string[i] in vowels:
            vowesCount += 1

    if string[-1] in vowels:
        vowesCount += 1
    if vowesCount >= 3 and twiceSeen > 0:
        return True
    else:
        return False


start = time()
with open("/home/rado/personal/AdventCode/2015/day5/input.txt") as inputIO:
    data = inputIO.readlines()
    nice = 0
    for word in data:
        word = word.strip("\n")
        if checkBruteForce(word):
            nice += 1

    print(nice)
end = time()

print(end - start)
