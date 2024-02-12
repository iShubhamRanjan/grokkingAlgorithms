graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def main():
  node = find_lowest_cost_node(costs)
  while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours:
      new_cost = cost + neighbours[n]
      if costs[n] > new_cost:
        costs[n] = new_cost
        parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


def find_lowest_cost_node(costs):
  lowest_cost = float('inf')
  lowest_cost_node = None
  for node in costs:
    if node not in processed and costs[node] < lowest_cost:
      lowest_cost = costs[node]
      lowest_cost_node = node
  return lowest_cost_node


main()
print('costs ->', costs)
print('parents ->', parents)
