def locate_card(cards, query):
  position = 0
  while position < len(cards):
    if cards[position] == query:
      return position
    position += 1
  return -1


def test():
  tests = []
  tests.append({
      'input': {
          'cards': [13, 11, 10, 7, 4, 3, 1, 0],
          'query': 7
      },
      'output': 3
  })
  tests.append({
      'input': {
          'cards': [13, 11, 10, 7, 4, 3, 1, 0],
          'query': 1
      },
      'output': 6
  })
  tests.append({'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0})
  tests.append({
      'input': {
          'cards': [3, -1, -9, -127],
          'query': -127
      },
      'output': 3
  })
  tests.append({'input': {'cards': [6], 'query': 6}, 'output': 0})
  tests.append({
      'input': {
          'cards': [9, 7, 5, 2, -9],
          'query': 4
      },
      'output': -1
  })
  tests.append({'input': {'cards': [], 'query': 7}, 'output': -1})
  tests.append({
      'input': {
          'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
          'query': 3
      },
      'output': 7
  })
  tests.append({
      'input': {
          'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
          'query': 6
      },
      'output': 2
  })

  for test in tests:
    result = locate_card(**test['input'])
    print(test['input']['query'],
          f'found at position: {result}' if result != -1 else 'not found')
