def count(items, i):
  if items is None or len(items) <= 0:
    return None
  elif len(items) == 1:
    return i + 1
  else:
    return count(items[1:], i + 1)
