def solve_one(data: list) -> int:
    """
    Counts occurrences of the word "XMAS" in all directions in a grid created from input data.
    """

    word: str = "XMAS"
    word_count: int = 0

    # Create a grid from the input data
    grid: list = []
    for line in enumerate(data):
        grid.append(list(line[1].strip()))

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for line in range(rows):
        for index, c in enumerate(grid[line]):
            if c == "X":
                try:
                    # Horizontal check
                    if index + 3 < cols and grid[line][index:index + 4] == list(word):
                        word_count += 1

                    # Reverse Horizontal check
                    if index - 3 >= 0 and grid[line][index - 3:index + 1] == list(word[::-1]):
                        word_count += 1

                    # Vertical check
                    if line + 3 < rows and "".join([grid[line + i][index] for i in range(4)]) == word:
                        word_count += 1

                    # Reverse Vertical check
                    if line - 3 >= 0 and "".join([grid[line - i][index] for i in range(4)]) == word:
                        word_count += 1

                    # Diagonal (down-right)
                    if line + 3 < rows and index + 3 < cols and "".join([grid[line + i][index + i] for i in range(4)]) == word:
                        word_count += 1

                    # Diagonal (up-left)
                    if line - 3 >= 0 and index - 3 >= 0 and "".join([grid[line - i][index - i] for i in range(4)]) == word:
                        word_count += 1

                    # Diagonal (down-left)
                    if line + 3 < rows and index - 3 >= 0 and "".join([grid[line + i][index - i] for i in range(4)]) == word:
                        word_count += 1

                    # Diagonal (up-right)
                    if line - 3 >= 0 and index + 3 < cols and "".join([grid[line - i][index + i] for i in range(4)]) == word:
                        word_count += 1

                except IndexError:
                    # Out of bounds catch
                    pass

    return word_count


def solve_two(data: str) -> int:
    return 0


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    print(solve_one(data))
