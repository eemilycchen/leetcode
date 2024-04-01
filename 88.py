
def assertConstraints(nums1, m, nums2, n):
    assert len(nums1) == m+n, "length of nums1 should be m + n"
    assert len(nums2) == n, "length of nums2 should be n"
    assert 0 <= m <= 200 and 0 <= n <= 200, "length for m and n should be from 0 to 200"
    assert 1 <= m+n <= 200, "total merge length should be from 1 to 200"

#initialize variables to test
#sample solution
def mergeWithSTL(storingList, storageSize, mergingList, listSize):
    for nextIndex in range(listSize):
        storingList[storageSize+nextIndex] = mergingList[nextIndex]
    storingList.sort()

"""
storingList = nums1
merginList = nums2
"""
def mergeWithPointers(storingList, storageSize, mergingList, listSize):
    indexUpdateFrom = storageSize - 1
    currentIndexToMerge = listSize - 1
    indexUpdateTo = storageSize + listSize - 1
    while currentIndexToMerge >= 0:
        nums1FirstIndexIsBigger = storingList[indexUpdateTo] > mergingList[currentIndexToMerge]
        storageIsAvailable = indexUpdateFrom >= 0
        if storageIsAvailable and nums1FirstIndexIsBigger:
            storingList[indexUpdateTo] = storingList[indexUpdateFrom]
            indexUpdateFrom -= 1
        else:
            storingList[indexUpdateTo] = mergingList[currentIndexToMerge]
            currentIndexToMerge -= 1
        indexUpdateTo -= 1
            


## Testing here
# print(assertConstraints(nums1, m, nums2, n))
nums1 = [1,2,3,0,0,0]
nums2 = [1,2,3]
m = 3
n = 3
mergeWithSTL(nums1, m, nums2, n)
print(nums1)