def find_min(nums):
    min = float("inf")
    for number in nums:
        if number < min:
            min = number
    return min