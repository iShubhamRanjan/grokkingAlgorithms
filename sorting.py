def simple_sort(nums):
  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      if nums[i] > nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
  return nums


def selection_sort(nums):
  for i in range(0, len(nums) - 1):
    smallest = i
    for j in range(i + 1, len(nums)):
      if nums[j] < nums[smallest]:
        smallest = j
    nums[i], nums[smallest] = nums[smallest], nums[i]
  return nums


def selection_sort_variation(nums):
  new_nums = []
  for i in range(0, len(nums)):
    smallest = find_smallest_helper(nums)
    new_nums.append(nums.pop(smallest))
  return new_nums


def find_smallest_helper(nums):
  smallest = nums[0]
  smallest_index = 0
  for i in range(len(nums)):
    if nums[i] < smallest:
      smallest, smallest_index = nums[i], i
  return smallest_index


nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
print(selection_sort(nums))
