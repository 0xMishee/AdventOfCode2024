import re

def solve_one(row: str) -> int:
    """Solve part one."""
    mul_value: int = 0
    pattern: str = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, row)

    for match in matches:
        mul_value += int(match.group(1)) * int(match.group(2))

    return mul_value

def solve_two(row: str) -> int:
    """Solve part two. Must be one row or logic breaks 😂"""
    mul_value: int = 0
    flag: bool = True
    patterns: re.Pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

    for pattern in patterns.finditer(row):
        if pattern.group() == "do()":
            flag = True
        elif pattern.group() == "don't()":
            flag = False
        else:
            if flag:
                mul_value += int(pattern.group(1)) * int(pattern.group(2))

    return mul_value

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        rows = file.readlines()

    solve_one_sum: int = 0
    solve_two_sum: int = 0

    for row in rows:
        solve_one_sum += solve_one(row)
        solve_two_sum += solve_two(row)

    print(f"Solve 1 sum: {solve_one_sum}")
    print(f"Solve 2 sum: {solve_two_sum}")

