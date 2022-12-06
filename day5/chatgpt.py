import re

stacks = [
    ["R", "G", "H", "Q", "S", "B", "T", "N"],
    ["H", "S", "F", "D", "P", "Z", "J"],
    ["Z", "H", "V"],
    ["M", "Z", "J", "F", "G", "H"],
    ["T", "Z", "C", "D", "L", "M", "S", "R", ],
    ["M", "T", "W", "V", "H", "Z", "J"],
    ["T", "F", "P", "L", "Z"],
    ["Q", "V", "W", "S"],
    ["W", "H", "L", "M", "T", "D", "N", "C", ],
]

# the rearrangement procedure
procedure = [
]

with open('./input.txt', 'r') as f:
    for line in f:
        if line.startswith("move"):
            moves = re.findall(r'\d+', line)
            num_to_move = int(moves[0])
            from_box = int(moves[1])
            to_box = int(moves[2])
            procedure.append(("move", num_to_move, from_box, to_box))
f.close()

# simulate the rearrangement procedure
for action, num_crates, from_stack, to_stack in procedure:
  # move the desired number of crates from the from_stack to the to_stack
#   for i in range(num_crates):
#     crate = stacks[from_stack - 1].pop()
#     stacks[to_stack - 1].append(crate)
    crates = stacks[from_stack - 1][-num_crates:]
    stacks[from_stack - 1] = stacks[from_stack - 1][:-num_crates]
    stacks[to_stack - 1].extend(crates)
    
# print the top crate on each stack after the procedure is complete
for i, stack in enumerate(stacks):
  print("Stack", i + 1, ":", stack[-1])