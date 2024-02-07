arr, x = [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0], 6

def binary_search(lo, hi, condition):
  if lo > hi:
    return -1
  
  mid = (hi + lo) // 2
  result = condition(mid)
  
  if result == 'found':
    return mid
  elif result == 'left':
    return binary_search(lo, mid - 1, condition)
  elif result == 'right':
    return binary_search(mid + 1, hi, condition)

def first_occurance():
  def condition(mid):
    if arr[mid] == x:
      if (mid - 1) >= 0 and arr[mid - 1] == x:
        return 'left'
      else:
        return 'found'
    elif arr[mid] > x:
      return 'right'  
    elif arr[mid] < x:
      return 'left'
      
  return binary_search(0, len(arr) - 1, condition)

def last_occurance():
  def condition(mid):
    if arr[mid] == x:
      if (mid + 1) <= (len(arr) - 1) and arr[mid + 1] == x:
        return 'right'
      else:
        return 'found'
    elif arr[mid] < x:
      return 'left'  
    elif arr[mid] > x:
      return 'right'
      
  return binary_search(0, len(arr) - 1, condition)

def first_and_last_occurance():
  print(f'first occurance: {first_occurance()}; last occurance: {last_occurance()}')

