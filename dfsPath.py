import numpy as np
import matplotlib.pyplot as plt

#e.x: graph should be like this:
# graph = {'22': set(['32', '23']),
#          '32': set(['22', '42']),
#          '42': set(['32', '43']),
#          '43': set(['42','44','53']),
#          '44': set(['43', '34']),
#          '34': set(['44', '24']),
#         '24': set(['34', '23']),
#         '23': set(['22', '24']),
#         '53': set(['43'])
#         }
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def get_path(graph, node1, node2):
    st =list(dfs_paths(graph, node1, node2))
    final_path=st[0]
    for i in st:
        if len(i) <len(final_path):
            final_path=i

    print(final_path)
    return  final_path

#e.x to get the path bethween two nodes:
# get_path(graph,"53","22")