
def assertConstraints(nums1, m, nums2, n):
    assert len(nums1) == m+n, "length of nums1 should be m + n"
    assert len(nums2) == n, "length of nums2 should be n"
    assert 0 <= m <= 200 and 0 <= n <= 200, "length for m and n should be from 0 to 200"
    assert 1 <= m+n <= 200, "total merge length should be from 1 to 200"

#initialize variables to test
def merge(nums1, m, nums2, n):
    for j in range(n):
        nums1[m+j] = nums2[j]
    nums1.sort()


## Testing here
# print(assertConstraints(nums1, m, nums2, n))
nums1 = [1,2,3,0,0,0]
nums2 = [1,2,3]
m = 3
n = 3
merge(nums1, m, nums2, n)
print(nums1)