
n = int(input())
players = list(map(int, input().split()))

teams = 0

for i in range(n):
    if players[i] <= 2:
        teams += 1

print(teams // 3)