"""
Title: 88. Merge Sorted Array
Question Link: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
Author: Emily Chen

HELP/REFERENCE ACKNOWLEDGEMENT
Persons: amanrathore48
Online sources: https://leetcode.com/problems/merge-sorted-array/discuss/3436053/Beats-100-oror-Best-\
    C%2B%2BJavaPython-and-JavaScript-Solution-oror-Two-Pointer-oror-STL

BUGS: None.
"""
def assertConstraints(nums1, m, nums2, n):
    assert len(nums1) == m+n, "length of nums1 should be m + n"
    assert len(nums2) == n, "length of nums2 should be n"
    assert 0 <= m <= 200 and 0 <= n <= 200, "length for m and n should be from 0 to 200"
    assert 1 <= m+n <= 200, "total merge length should be from 1 to 200"

#initialize variables to test
#sample solution
def mergeWithSTL(sortedList1, list1Size, sortedList2, list2Size):
    for nextIndex in range(list2Size):
        sortedList1[list1Size+nextIndex] = sortedList2[nextIndex]
    sortedList1.sort()

def merge(sortedList1, list1Size, sortedList2, list2Size):
    list1slot = list1Size - 1
    list2slot = list2Size - 1
    storageSlot = list1Size + list2Size - 1
    while list2slot >= 0:
        list1ElmIsBigger = sortedList1[list1slot] > sortedList2[list2slot]
        if list1slot >= 0 and list1ElmIsBigger:
            sortedList1[storageSlot] = sortedList1[list1slot]
            list1slot -= 1
        else:
            sortedList1[storageSlot] = sortedList2[list2slot]
            list2slot -= 1
        storageSlot -= 1
            


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