def quicksort(nums):
  if len(nums) < 2:
    return nums

  pivot = nums[0]
  left = [i for i in nums[1:] if i <= pivot]
  right = [i for i in nums[1:] if i > pivot]
  return quicksort(left) + [pivot] + quicksort(right)
