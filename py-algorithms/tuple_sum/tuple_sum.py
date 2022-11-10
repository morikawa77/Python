# Algorithm to find the sum of the elements of a tuple

from itertools import combinations

tuple_size = 4

def tupleSum(nums, target):
    
    nums.sort()
    
    def valid(val):
        return sum(val) == target

    # combinations list with elementos who sum is target
    combinations_list = list(set(list(filter(valid, list(combinations(nums, tuple_size))))))

    # convert list of tuples to list of lists
    result = [list(i) for i in combinations_list]
          
    return result



print(tupleSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(tupleSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(tupleSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])