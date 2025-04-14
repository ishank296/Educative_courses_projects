def reverse(array):
    if array == []:
        return
    elif len(array) == 1:
        return array
    else:
        return [array[len(array)-1]] + reverse(array[:len(array)-1])


if __name__ == "__main__":
    array = [3,54,7,3,2]
    print(reverse(array))