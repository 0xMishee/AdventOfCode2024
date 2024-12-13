def solve_one(data: list[str]) -> int:
    """
    Calculate the number of unique steps taken by the guard.
    """
    steps: int = 0
    blockage: str = "#"
    guard_directions: dict[str, tuple[int, int]] = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
    directions: list[str] = list(guard_directions.keys())
    unique_steps: list[tuple[int, int]] = []

    grid: list[list[str]] = [list(line.strip()) for line in data]

    rows: int = len(grid)
    cols: int = len(grid[0]) if rows > 0 else 0

    def find_guard(grid: list[list[str]]) -> tuple[tuple[int, int] | None, str | None]:
        """
        Find the guard's initial position and direction.
        """
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] in guard_directions:
                    return (row, col), grid[row][col]
        return None, None

    guard_location: tuple[int, int] | None
    current_direction: str | None
    guard_location, current_direction = find_guard(grid)
    if guard_location is None or current_direction is None:
        return 0

    current_row: int
    current_col: int
    current_row, current_col = guard_location

    while True:
        if (current_row, current_col) not in unique_steps:
            unique_steps.append((current_row, current_col))

        move_row: int
        move_col: int
        move_row, move_col = guard_directions[current_direction]
        next_row: int = current_row + move_row
        next_col: int = current_col + move_col

        ## Replaced try/except IndexError with boundary checks for better reliability
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if grid[next_row][next_col] == blockage:
                # Cyclic rotation
                current_index: int = directions.index(current_direction)
                current_direction = directions[(current_index + 1) % 4]
            else:
                current_row = next_row
                current_col = next_col
        else:
            break

    steps = len(unique_steps)
    return steps



if __name__ == "__main__":
    with open("Day 6\\input.txt", "r", encoding="utf-8") as file:
        data: list[str] = file.readlines()

    print(solve_one(data))
