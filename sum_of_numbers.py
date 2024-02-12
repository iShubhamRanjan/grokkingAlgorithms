def sum_of_numbers(nums):
  if nums is None or len(nums) <= 0:
    return None

  if len(nums) == 1:
    return nums[0]

  return nums[0] + sum_of_numbers(nums[1:])
