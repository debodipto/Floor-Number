class Solution(object):
    def maxProduct(self, nums):
        positive, negative = nums[0], nums[0]
        result = nums[0]
        for num in nums[1:]:
            positive, negative = max(num, positive * num, negative * num), min(num,
                                                                               positive * num, negative * num)
            result = max(result, positive)
        return result


if __name__ == "__main__":
    assert Solution().maxProduct([2, 3, -2, 4]) == 6
