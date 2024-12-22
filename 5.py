from collections import defaultdict

with open(0) as file:
    data = file.read()

def ParseRules(rules_str):
    graph = defaultdict(set)  # Adjacency list.
    lines = [line.strip() for line in rules_str.split('\n')]
    for line in lines:
        first, second = [int(n) for n in line.split('|')]
        graph[first].add(second)
    return graph

def ParseSequences(sequences_str):
    lines = [line.strip() for line in sequences_str.split('\n')]
    result = []
    for line in lines:
        if line == '':  # Account for trailing empty lines in the file.
            continue
        numbers = [int(n) for n in line.split(',')]
        result.append(numbers)
    return result

rules_str, sequences_str = data.split('\n\n')

# `rules[a]` tells us what numbers `a` must come before.
rules = ParseRules(rules_str)
sequences = ParseSequences(sequences_str)

def FindARootNode(graph):
    candidates = set(graph.keys())
    for value in graph.values():
        for number in value:
            if number in candidates:
                candidates.remove(number)
    assert(len(candidates) > 0)
    return list(candidates)[0]

# Returns True if `before` must come before `after` according to `rules`.
def MustComeBefore(after, before, rules):
    return after in rules[before]

# Returns True if `sequence` has at least one pair out of order.
def IsBadSequence(sequence, rules):
    n = len(sequence)
    return any(MustComeBefore(sequence[i], sequence[j], rules) for i in range(n) for j in range(i+1, n))

# Edits `sequence` to be valid and returns the middle element after doing so.
# But if `sequence` was already valid to begin with, returns 0.
def EditSequence(sequence, rules):
    n = len(sequence)
    was_bad = False
    for i in range(n):
        for j in range(i+1, n):
            if MustComeBefore(sequence[i], sequence[j], rules):
                was_bad = True
                sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence[n//2] if was_bad else 0

def Part1(sequences, rules):
    return sum(seq[len(seq)//2] for seq in sequences if not IsBadSequence(seq, rules))

# part 1
print(Part1(sequences, rules))

# part 2
print(sum(EditSequence(seq, rules) for seq in sequences))
