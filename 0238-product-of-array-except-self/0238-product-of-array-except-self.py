class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Initialize answer array with 1s

        # First Pass: Calculate prefix products
        # answer[i] will store product of nums[0...i-1]
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # Second Pass: Calculate suffix products and combine
        # right_product will store product of nums[i+1...n-1]
        suffix_product = 1
        for i in range(n - 1, -1, -1):  # Iterate from right to left
            answer[i] *= suffix_product  # Multiply current prefix product by suffix product
            suffix_product *= nums[i]

        return answer
        