reports = list()

with open('input.txt') as f:
    l = f.readlines()
l = [el.replace('\n', '') for el in l]

levels = list()

for i in range(len(l)):
    temp = [int(n) for n in l[i].split(' ')]
    levels.append(temp)

def is_safe(level):
    inc = all(i < j and 1 <= (j - i) <= 3 for i, j in zip(level, level[1:]))
    dec = all(i > j and 1<= (i - j) <= 3 for i, j in zip(level, level[1:]))
    return inc or dec

safe = list()
unsafe = list()

for level in levels:
    if is_safe(level):
        safe.append(level)
    else:
        unsafe.append(level)

for report in unsafe:
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            safe.append(modified_report)
            break

print(len(safe))