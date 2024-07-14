# Given an array of integers, write a function that returns a list of the 3 largest numbers

def findThreeLargest(array):
    ThreeLargest = [float("-inf"), float("-inf"), float("-inf")]
    for num in array:
        if num > ThreeLargest[-1]:
            ThreeLargest = updateThreeLargest(ThreeLargest, num)
    return ThreeLargest

def updateThreeLargest(array, num):
    for i in range(len(array)):
        if num > array[i]:
            temp = array[i]
            array[i] = num 
            num = temp
    return array



nums = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargest(nums))