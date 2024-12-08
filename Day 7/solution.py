import functools
import itertools
import re


def solve_one(data: list) -> int:
    total_calibration: int = 0

    def calibration_permutations(calibration: list) -> list[str]:
        ## Function to generate all possible permutations of the calibration values.

        operators: list[str] = ["+", "*"]
        combinations = itertools.product(operators, repeat=len(calibration) - 1)

        cal_permutations: list[str] = []

        ## Builds the expression for each permutation. 
        for combination in combinations:
            expression: str = str(calibration[0])
            for number, operation in zip(calibration[1:], combination):
                expression += operation + str(number)
            cal_permutations.append(expression)

        return cal_permutations

    ## Function to calculate the calibration value.
    def calculate(calibration: str) -> int:

        ordered_calibrations: list[str] = calibration.split(" ")
        goal_sum: int = int(ordered_calibrations[0].split(":")[0])
    
        calculation_values: list[int] = ordered_calibrations[1:]
        calculation_values = [int(value) for value in calculation_values]


        ## Quick check for all addition or multiplication
        if goal_sum == sum(calculation_values):
            ##print("Sum Test OK: ", goal_sum, calculation_values)
            return goal_sum
        elif goal_sum == functools.reduce(lambda x, y: x * y, calculation_values):
            ##print("Multiplication Test OK: ", goal_sum, calculation_values)
            return goal_sum
        
        ## Generate all possible permutations of the calculation values.
        cal_permutations = calibration_permutations(calculation_values)

        addition_flag: bool = True
        mul_flag: bool = True

        ## I´m sorry for making this... I´m not proud of it.
        for cal in cal_permutations:
            cal_breakdown = re.findall(r'\d+|[+*]', cal)
            tmp_sum = int(cal_breakdown[0])
            
            for i in range(1, len(cal_breakdown), 2):  # Step by 2 to process operators and operands
                operator = cal_breakdown[i]
                operand = int(cal_breakdown[i + 1])
                
                if operator == "+":
                    if addition_flag:
                        tmp_sum += operand
                elif operator == "*":
                    if mul_flag:
                        tmp_sum *= operand

            if int(goal_sum) == tmp_sum:
                #print("Success: ", goal_sum, cal)
                return goal_sum
            else:
                #print("Failed: ", goal_sum, cal)
                continue
        return 0

    for calculation in data:
        total_calibration += calculate(calculation)

    return total_calibration

if __name__ == "__main__":
    with open("Day 7/input.txt") as file:
        data = file.readlines()

    data = [line.strip() for line in data]

    # Part 1
    print("Number of calibration results: ",solve_one(data))