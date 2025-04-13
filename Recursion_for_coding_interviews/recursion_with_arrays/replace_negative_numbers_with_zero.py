def replace(array,index):
    if index == len(array):
        return
    if array[index] < 0:
        array[index] = 0
    replace(array,index+1)
    return


if __name__ == '__main__':
    array = [2, -3, 4, -1, -7, 8]
    print("Original Array --> " + str(array))
    replace(array,0)
    print("Modified Array --> " + str(array))