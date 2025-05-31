from collections import defaultdict, deque
import heapq

def ancient_ordering(words):

    graph = defaultdict(set)
    in_degree = {chr(c): 0 for c in range(ord('a'), ord('z')+1)}
    used_chars = set()

    for word in words:
        for ch in word:
            used_chars.add(ch)

    n = len(words)
    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return "-1"
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break


    heap = []
    for ch in used_chars:
        if in_degree[ch] == 0:
            heapq.heappush(heap, ch)

    result = []
    while heap:
        ch = heapq.heappop(heap)
        result.append(ch)
        for nei in sorted(graph[ch]):
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                heapq.heappush(heap, nei)

    if len(result) != len(used_chars):
        return "-1"

    return ''.join(result)


n = int(input())
words = [input().strip() for _ in range(n)]
print(ancient_ordering(words))

