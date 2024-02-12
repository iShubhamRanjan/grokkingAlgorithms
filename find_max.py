def max_in_list(arr, curr_max):
  if arr is None or len(arr) <= 0:
    return None

  curr_max = find_max(arr[0], curr_max)
  if len(arr) == 1:
    return curr_max
  else:
    return max_in_list(arr[1:], curr_max)


def find_max(n1, n2):
  return n1 if n1 > n2 else n2
