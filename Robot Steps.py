# Kevin Ramos
# CSCI128 - Section E
# Python-TrackTheRobot
num_directions = int(input())
x = 0
y = 0
for direction in range(num_directions):
    directions = input().split()
    directions[1] = int(directions[1])
    if 'right' in directions:
        x += directions[1]
    elif 'left' in directions:
        x -= directions[1]
    elif 'up' in directions:
        y += directions[1]
    elif 'down' in directions:
        y -= directions[1]
print(f"({x}, {y})")
