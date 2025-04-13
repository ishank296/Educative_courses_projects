def average(array,index):
    if index ==len(array)-1:
        return array[index]
    if index == 0:
        return (array[index] + average(array,index+1))/len(array)
    else: return array[index] + average(array,index+1)


if __name__ == '__main__':
    testVariable = [10, 2, 3, 4, 8, 0]
    currentIndex = 0
    print(average(testVariable,0))