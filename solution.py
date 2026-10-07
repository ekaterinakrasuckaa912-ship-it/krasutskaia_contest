n = int(input())

events = {}

for _ in range(n):
    start, end, cost = map(int, input().split())

    events[start] = events.get(start, 0) + cost
    events[end] = events.get(end, 0) - cost

current_load = 0
max_load = -1
earliest_time = 0

for time in sorted(events):
    current_load += events[time]

    if current_load > max_load:
        max_load = current_load
        earliest_time = time

print(max_load, earliest_time)
