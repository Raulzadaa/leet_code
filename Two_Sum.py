class Solution(object):
    def twoSum(self, nums, target):

        for c in range(len(nums)):

            for b in range(len(nums)):

                if nums[c] + nums[b] == target:

                    a = []
                    a.append(c)
                    a.append(b)
                    return list(a)

nums = [3,2,4]

target = 6

answer = Solution().twoSum(nums , target)

print(answer)