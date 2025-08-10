import sys
input = sys.stdin.readline

dmax = 1000
dmin = -1000
drange = dmax - dmin + 1
inf = (1 << 31) - 2

n = int(input())
events = []

for _ in range(n):
    time, lower_bound, upper_bound = map(int, input().split())
    events.append((time, lower_bound - dmin + 1, upper_bound - dmin))

events.sort(reverse=True)
tmax = events[0][0] if events else 0

dists = [[inf] * (drange + 2) for _ in range(2)]
dists[0][-dmin] = 0

for t in range(1, tmax + 1):
    curr = t & 1
    prev = (t - 1) & 1
    
    for i in range(1, drange + 1):
        dists[curr][i] = min(
            dists[prev][i - 1] + 1,
            dists[prev][i],
            dists[prev][i + 1] + 1
        )
        if dists[curr][i] > inf:
            dists[curr][i] = inf
    
    if events and t == events[-1][0]:
        event = events.pop()
        _, lower_bound, upper_bound = event
        for i in range(lower_bound, upper_bound):
            dists[curr][i] = inf

answer = inf
for dist in dists[tmax & 1]:
    answer = min(dist, answer)

print(-1 if answer == inf else answer)