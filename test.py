l = [[0, 0, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]]

def get_neighbours_status(x, y, l):
    total = 0
    # Loop through all possible neighbors
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Skip the cell itself
            if i == 0 and j == 0:
                continue
            # Calculate neighbor's coordinates
            nx, ny = x + i, y + j
            # Check if neighbor is within bounds
            if 0 <= nx < len(l) and 0 <= ny < len(l[0]):
                if l[nx][ny] == 1:
                    total += 1
    return total

print(get_neighbours_status(0, 0, l))  # Example
