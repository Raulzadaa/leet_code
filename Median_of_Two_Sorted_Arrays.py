class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        mergedArray = []

        for c in nums1:
            mergedArray.append(c)

        for c in nums2:
            mergedArray.append(c)

        size = len(mergedArray)
        mergedArray = sorted(mergedArray)

        if len(mergedArray) % 2 == 0:
            a = float(mergedArray[(size//2)])
            b = float(mergedArray[(size//2) - 1 ])

            median = (a+b)/2

        else:
            median = mergedArray[(size//2) ]

        return float(median) 