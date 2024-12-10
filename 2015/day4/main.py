import hashlib

input = "iwrupvqb"


def get_md5_of_string(input_string):
    # check hash
    return hashlib.md5(input_string.encode()).hexdigest()


def findLowestmd5(input: str, leadingZeroLen: int) -> None:
    # Brute Force Try
    index = 0
    result = None

    leadingZeros = ""
    for i in range(leadingZeroLen):
        leadingZeros += "0"

    while True:
        print(index)
        result = get_md5_of_string(input + str(index))
        if result[:leadingZeroLen] == leadingZeros:
            print(f"index where leading {leadingZeroLen} zero is {index}")
            break
        index += 1


findLowestmd5(input, 6)
