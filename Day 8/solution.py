

def solve_one(input_data: list[str]) -> int:
    antinodes: set = set()
    frequencies: dict = {".":[]}
    antennas_locations: dict = {}

    grid: list[list[str]] = [list(line.strip()) for line in input_data]

    rows: int = len(grid)
    cols: int = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            if cell == ".":
                frequencies[cell].append((col, row))
            else:
                if cell not in antennas_locations:
                    antennas_locations[cell] = []
                    antennas_locations[cell].append((col, row))
                elif cell in antennas_locations:
                    antennas_locations[cell].append((col, row))


    for v in antennas_locations.values():
        for a in v:
            for b in v:
                if a == b:
                    continue
                dx: int = a[0] - b[0]
                dy: int = a[1] - b[1]
                nx: int = b[0] - dx
                ny: int = b[1] - dy
                antinodes.add((nx, ny))
    
    antinodes = {(x, y) for x, y in antinodes if 0 <= x < cols and 0 <= y < rows}

    return len(antinodes)

if __name__ == "__main__":


    with open("Day 8\\input.txt", "r", encoding="utf-8") as file:
        data = file.readlines()


    print("The amount of antinodes are: ", solve_one(data))
