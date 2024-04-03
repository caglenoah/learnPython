def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far

# def find_max(nums):
#     max_so_far = float("-inf")
#     for i in range(0, len(nums)):
#         if nums[i] > max_so_far:
#             max_so_far = nums[i]
#     return max_so_far