#!/usr/local/bin/python3

# ==== PART 1 ====

ordering = set()
to_print = []

# Input parsing
with open('./input', 'r') as input:
    mode = "ordering"
    for line in input.readlines():
        if mode == "ordering":
            if line == "\n":
                mode = "printing"
            else:
                ordering.add(tuple([int(N) for N in line.split("|")]))
        elif mode == "printing":
            to_print.append([int(N) for N in line.split(",")])

page_sum = 0

for print_order in to_print:
    last_i = len(print_order)-1
    for i in range(len(print_order)):
        if i == last_i:
            page_sum += print_order[len(print_order)//2]
        else:
            # Look for contradiction
            if (print_order[i+1], print_order[i]) in ordering:
                break

print(f"PART 1 - Solution: {page_sum}")

# ==== PART 2 ====

wrong_sum = 0

for print_order in to_print:
    incorrect = False
    i = 0
    while i < len(print_order)-1:
        # Look for contradiction
        if (print_order[i+1], print_order[i]) in ordering:
            incorrect = True
            # Reorder list from here and restart
            print_order[i], print_order[i+1] = print_order[i+1], print_order[i]
            i = 0
        else:
            i += 1
    
    if incorrect:
        wrong_sum += print_order[len(print_order)//2]


print(f"PART 2 - Solution: {wrong_sum}")
