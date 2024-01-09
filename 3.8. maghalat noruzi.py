

def distance(points):
    total_distance = max(points) - min(points)
    return total_distance


input_line = input()
input_points = [int(x) for x in input_line.split()]

min_distance = distance(input_points)
print(min_distance)

