
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
#There's a bug!
def mergeWithPointers(storeMergeList, firstMergeSize, listToMerge, secondMergeSize):
    currResultIndex = firstMergeSize - 1 #not sure how to interpret this?
    stillMerging = secondMergeSize - 1
    currStoringIndex = firstMergeSize + secondMergeSize - 1 #note sure how to interpret this?
    while stillMerging >= 0:
        storeMergeListHasGreaterValue = checkIfBigger(storeMergeList, listToMerge, currResultIndex, stillMerging, currStoringIndex)
        if storeMergeListHasGreaterValue:
            storeMergeList[currStoringIndex] = storeMergeList[currResultIndex]
            currResultIndex -= 1
        else:
            storeMergeList[currStoringIndex] = listToMerge[stillMerging]
            stillMerging -= 1
        currStoringIndex -= 1

def checkIfBigger(storeMergeList, listToMerge, currResultIndex, currentIndexToMerge, currStoringIndex):
    list1LastIndexIsBigger = storeMergeList[currStoringIndex] > listToMerge[currentIndexToMerge]
    storageIsAvailable = currResultIndex >= 0
    return list1LastIndexIsBigger and storageIsAvailable
            


## Testing here
# print(assertConstraints(nums1, m, nums2, n))
nums1 = [1,2,3,0,0,0]
nums2 = [1,2,3]
m = 3
n = 3
mergeWithSTL(nums1, m, nums2, n)
# mergeWithPointers(nums1, m, nums2, n)
print(nums1)