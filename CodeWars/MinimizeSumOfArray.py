#Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .

def min_sum(arr):
    nums1 = sorted(arr)
    nums2 = sorted(arr, reverse = True)
    return sum([nums1[i] * nums2[i] for i in range(len(nums1)//2)])

print(min_sum([12,6,10,26,3,24]))