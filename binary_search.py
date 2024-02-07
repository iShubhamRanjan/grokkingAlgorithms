tests = []
tests.append({'input': {'arr': [3,5,7,9,11,13,15,17,19], 'x': 11}, 'output': 4})
tests.append({'input': {'arr': [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0], 'x': 6}, 'output': 2})
arr, x = tests[0]['input']['arr'], tests[0]['input']['x']

def test_location(mid):
  if x == arr[mid]:
    if (mid - 1) >= 0 and arr[mid - 1] == x:
      return 'left'
    else:
      return 'found'
  elif x > arr[mid]:
    return 'left'
  elif x < arr[mid]:
    return 'right'

def binary_search(low, high):
  if low > high:
    return -1

  mid = (high + low) // 2
  result = test_location(mid)

  if result == 'found':
    return mid
  elif result == 'left':
    return binary_search(low, mid - 1)
  elif result == 'right':
    return binary_search(mid + 1, high)

def exec():
  result = binary_search(0, len(arr) - 1)
  print(x, f'found at index {result}' if result != -1 else 'not found')