def balanced(string,startIndex,currentIndex):
    if currentIndex == len(string):
        return startIndex == 0
    if startIndex < 0:
        return False
    if string[currentIndex] == '(':
        return balanced(string,startIndex+1,currentIndex+1)
    if string[currentIndex] == ')':
        return balanced(string,startIndex-1,currentIndex+1)


if __name__ == "__main__":
    testVariable = ["(", "(", ")", ")", "(", ")"]
    print(balanced(testVariable,0,0))