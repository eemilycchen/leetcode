"""
Title: 88. Merge Sorted Array
Author: Emily Chen

HELP/REFERENCE ACKNOWLEDGEMENT
Persons: 
"""
def assertConstraints(nums1, m, nums2, n):
    assert len(nums1) == m+n, "length of nums1 should be m + n"
    assert len(nums2) == n, "length of nums2 should be n"
    assert 0 <= m <= 200 and 0 <= n <= 200, "length for m and n should be from 0 to 200"
    assert 1 <= m+n <= 200, "total merge length should be from 1 to 200"

#initialize variables to test
#sample solution
def mergeWithSTL(nums1, firstMergeSize, nums2, secondMergeSize):
    for nextIndex in range(secondMergeSize):
        nums1[firstMergeSize+nextIndex] = nums2[nextIndex]
    nums1.sort()

def merge(nums1, firstMergeSize, nums2, secondMergeSize):
    firstMergeIndex = firstMergeSize - 1
    secondMergeIndex = secondMergeSize - 1
    storageIndex = firstMergeSize + secondMergeSize - 1
    #why does secondMergeIndex define still merging? Is it because it tells us
    #all of the items from the second merge has been added to the storage?
    while secondMergeIndex >= 0:
        nums1IsBigger = nums1[firstMergeIndex] > nums2[secondMergeIndex]
        if firstMergeIndex >= 0 and nums1IsBigger:
            nums1[storageIndex] = nums1[firstMergeIndex]
            firstMergeIndex -= 1
        else:
            nums1[storageIndex] = nums2[secondMergeIndex]
            secondMergeIndex -= 1
        storageIndex -= 1
            


## Testing here
# print(assertConstraints(nums1, m, nums2, n))
nums1 = [0,0,0,0,2,2,7,0,0,0]
nums2 = [1,4,5]
m = 7
n = 3
# mergeWithSTL(nums1, m, nums2, n)
merge(nums1, m, nums2, n)
# merge(nums1, m, nums2, n)
print(nums1)