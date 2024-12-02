#!/usr/local/bin/python3

# Checks that a report is safe
# Input: array of integers
def report_is_safe(report):
    prev = None
    threshold = 0
    for entry in report:
        if not prev:
            # First Iteration
            prev = entry
            continue

        if prev and threshold == 0:
            # Secont Iteration - Initialization of check condition
            if entry > prev:
                threshold = SAFETY_THRESHOLD
            elif entry < prev:
                threshold = -SAFETY_THRESHOLD
            else:
                return False
        
        delta = entry - prev

        if threshold < 0:
            if delta >= 0 or delta < threshold:
                return False
        elif threshold > 0:
            if delta <= 0 or delta > threshold:
                return False

        prev = entry
    
    return True

# ==== PART 1 ====

# Constants
SAFETY_THRESHOLD = 3 # Max amount of growth/degrowth in the sequence for it to be considered safe

safe_reports = 0

with open("./input", "r") as input:
    for line in input.readlines():
        report = [int(entry) for entry in line.split(" ")]
        safe_reports += 1 if report_is_safe(report) else 0

print(f"PART 1 - Solution: {safe_reports}")

# ==== PART 2 ====

DAMPENER_THRESHOLD = 1 # Amount of levels that may be ignored to make the problem pass
# TODO make this code work with dampening of more than 1 level
# TODO optimize it (it will be exponential)

safe_reports = 0

with open("./input", "r") as input:
    for line in input.readlines():
        report = [int(entry) for entry in line.split(" ")]

        if report_is_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                if report_is_safe(report[0:i] + report[i+1:len(report)]):
                    safe_reports += 1
                    # DEBUG - print(f"Report {report} made safe by removing {report[i]}")
                    break

print(f"PART 2 - Solution: {safe_reports}")