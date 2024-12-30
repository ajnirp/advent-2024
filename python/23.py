from collections import defaultdict

with open(0) as file:
    lines = [line.strip() for line in file.readlines()]

graph = defaultdict(set)
for line in lines:
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

def Part1(graph):
    result = set()
    for a in graph:
        for b in graph[a]:
            for c in graph[b]:
                if c == a: continue
                if a in graph[c]:
                    if 't' in [a[0], b[0], c[0]]:
                        elem = [a, b, c]
                        elem.sort()
                        result.add(tuple(elem))
    return len(result)

print(Part1(graph))
