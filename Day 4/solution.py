
def solve_one(data: list) -> int:

    matrix = create_matrix(data)

    word: str = "XMAS"
    word_count: int = 0


    

    return word_count

def solve_two(data: str) -> int:
    return 0

def create_matrix(data: list) -> list:
    matrix: list = []
    for line in data:
        matrix.append(list(line.strip()))

    return matrix

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

        print(solve_one(data))

