def simple_sort(nums):
  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      if nums[i] > nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
  return nums


nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
print(simple_sort(nums))
