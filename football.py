

total_points = 0
total_wins = 0
for _ in range(30):
    score = int(input())
    total_points += score
    if score == 3:
        total_wins += 1

print(total_points, total_wins)





