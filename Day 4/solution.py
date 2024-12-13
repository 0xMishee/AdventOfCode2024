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
                    # Horizontal 
                    if index + 3 < cols and grid[line][index:index + 4] == list(word):
                        word_count += 1

                    # Reverse Horizontal 
                    if index - 3 >= 0 and grid[line][index - 3:index + 1] == list(word[::-1]):
                        word_count += 1

                    # Vertical 
                    if line + 3 < rows and "".join([grid[line + i][index] for i in range(4)]) == word:
                        word_count += 1

                    # Reverse Vertical 
                    if line - 3 >= 0 and "".join([grid[line - i][index] for i in range(4)]) == word:
                        word_count += 1

                    # Diagonal
                    if line + 3 < rows and index + 3 < cols and "".join([grid[line + i][index + i] for i in range(4)]) == word:
                        word_count += 1
                    if line - 3 >= 0 and index - 3 >= 0 and "".join([grid[line - i][index - i] for i in range(4)]) == word:
                        word_count += 1
                    if line + 3 < rows and index - 3 >= 0 and "".join([grid[line + i][index - i] for i in range(4)]) == word:
                        word_count += 1
                    if line - 3 >= 0 and index + 3 < cols and "".join([grid[line - i][index + i] for i in range(4)]) == word:
                        word_count += 1

                except IndexError:
                    # Out of bounds catch
                    pass

    return word_count


def solve_two(data: list) -> int:
    word: str = "MAS"
    word_count: int = 0

    # Create a grid from the input data
    grid: list = []
    for line in enumerate(data):
        grid.append(list(line[1].strip()))

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0


    for line in range(rows):
        for index, c in enumerate(grid[line]):
            if c == "M":
                try:
                    # Diagonal
                    if line + 2 < rows and index + 2 < cols and "".join([grid[line + i][index + i] for i in range(3)]) == word:
                        word_count += 1
                        #print("Diagonal", line, index)
                    if line - 2 >= 0 and index - 2 >= 0 and "".join([grid[line - i][index - i] for i in range(3)]) == word:
                        word_count += 1
                    if line + 2 < rows and index - 2 >= 0 and "".join([grid[line + i][index - i] for i in range(3)]) == word:
                        word_count += 1
                    if line - 2 >= 0 and index + 2 < cols and "".join([grid[line - i][index + i] for i in range(3)]) == word:
                        word_count += 1
                except IndexError:
                    # Out of bounds catch
                    pass




    return word_count


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    print(f"Number of XMAS Solve One:", solve_one(data))
    print(f"Number of Cross MAS:",solve_two(data))
