# Given an array of integers, return indices of the two numbers such
# that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

def twoSum(nums, target):
    my_dict = {}
    if len(nums) >= 2:
        for index, current_value in enumerate(nums):
            if current_value < target and current_value not in my_dict.keys():
                my_dict.update({current_value: index})
            needed_element = target - current_value
            print(my_dict)
            if needed_element in my_dict and len(my_dict) > 1:
                return my_dict.get(needed_element), index
###################################################################
#        my_dict = {}
        if len(nums) >= 2:
            for index, current_value in enumerate(nums):
                needed_element = target - current_value

                if needed_element in my_dict:
                    return my_dict.get(needed_element), index
                else:
                    my_dict[current_value] = index


print(twoSum([3,2,4], 6))
