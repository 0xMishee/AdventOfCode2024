"""Module for calculating total distance and similarity score from input file."""


def total_distance() -> int:
    """Calculates the total distance between corresponding elements of two lists
    from "input.txt". Returns the sum of absolute differences between corresponding
    elements of the two sorted lists."""
    total_distance_number: int = 0

    left_list: list = []
    right_list: list = []

    with open("input.txt", "r", encoding="utf-8") as file:
        data: list = file.read().splitlines()
        for line in data:
            left_list.append(line.split()[0])
            right_list.append(line.split()[1])

    left_list.sort()
    right_list.sort()

    for index, left_value in enumerate(left_list):
        total_distance_number += abs(int(left_value) - int(right_list[index]))

    return total_distance_number


def similar_score() -> int:
    """Calculates the total similar score between corresponding elements of two lists from "input.txt"."""
    total_similar_score: int = 0

    left_list: list = []
    right_list: list = []

    with open("input.txt", "r", encoding="utf-8") as file:
        data: list = file.read().splitlines()
        for line in data:
            left_list.append(int(line.split()[0]))
            right_list.append(int(line.split()[1]))

    for _, left_value in enumerate(left_list):
        left_value_count = right_list.count(left_value)
        total_similar_score += left_value_count * left_value

    return total_similar_score


if __name__ == "__main__":
    print(f"This is the total distance score: {total_distance()}")
    print(f"This is the similar score: {similar_score()}")