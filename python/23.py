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

print(Part1(graph))  # 1304

# Slight modification of https://en.wikipedia.org/wiki/Clique_problem#Finding_a_single_maximal_clique.
# We optimize by only considering neighbors of `key`, because non-neighbors of `key` can't
# be in its clique.
def MaximalCliqueFor(key, graph):
    clique = set([key])
    for neighbor in graph[key]:
        if all(neighbor in graph[elem] for elem in clique):
            clique.add(neighbor)
    return clique

def Part2(graph):
    maximum_clique = []
    for key in graph:
        maximal_clique = MaximalCliqueFor(key, graph)
        if len(maximal_clique) > len(maximum_clique):
            maximum_clique = [elem for elem in maximal_clique]
    return ','.join(sorted(maximum_clique))

print(Part2(graph))  # ao,es,fe,if,in,io,ky,qq,rd,rn,rv,vc,vl
