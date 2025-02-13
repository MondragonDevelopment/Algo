# Add elements in each array and multiply them by the depth of said array (starting at 1)

def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

nums = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(nums))
