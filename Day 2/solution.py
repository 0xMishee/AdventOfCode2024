"""Checks what reports are safe and how many reports are safe with fault tolerance."""

def safe_report_count(row, min_val=1, max_val=3) -> int:
    """Counts the number of safe reports without fault tolerance."""
    return 1 if all(min_val <= row[i+1] - row[i] <= max_val for i in range(len(row) - 1)) \
             or all(min_val <= row[i] - row[i+1] <= max_val for i in range(len(row) - 1)) else 0

def safe_report_count_fault_tolerance(row) -> int:
    """Counts the number of safe reports with fault tolerance."""

    if safe_report_count(row):
        return 1

    safe: int = 0

    if safe_report_count(row):
        return 1

    for i in range(len(row)):
        fault_tolerated_report = row[:i] + row[i+1:]
        if safe_report_count(fault_tolerated_report):
            safe += 1
            break

    return safe

if __name__ == '__main__':
    safe_reports: int = 0
    safe_reports_fault_tolerance: int = 0

    with open('input.txt', "r", encoding="utf-8") as f:
        reports = f.readlines()

        for levels in reports:
            level_values = list(map(int, levels.split()))
            safe_reports += safe_report_count(level_values)
            safe_reports_fault_tolerance += safe_report_count_fault_tolerance(level_values)

    print(f"This is the safe amount of reports: {safe_reports}")
    print(f"This is the safe amount with one fault tolerance: {safe_reports_fault_tolerance}")
