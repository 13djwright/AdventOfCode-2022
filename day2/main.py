
def won(a, b):
    if a == 1: #Rock
        return b == 3
    if a == 2: #Paper
        return b == 1
    if a == 3: #Scissors
        return b == 2

def get_score(a, b):
    if a == b: #draw
        return 3 + a
    if (won(a, b)):
        return 6 + a
    return a

def convert_to_name(l):
    upper_l = l.upper()
    if upper_l == "A" or upper_l == "X": #Rock
        return "Rock"
    if upper_l == "B" or upper_l == "Y": #Paper
        return "Paper"
    if upper_l == "C" or upper_l == "Z": #Scissors
        return "Scissors"

def convert_to_int(l):
    upper_l = l.upper()
    if upper_l == "A" or upper_l == "X": #Rock
        return 1
    if upper_l == "B" or upper_l == "Y": #Paper
        return 2
    if upper_l == "C" or upper_l == "Z": #Scissors
        return 3

def get_winning_choice(a):
    if a == 1: #Rock
        return 2
    if a == 2: #Paper
        return 3
    if a == 3: #Scissors
        return 1

def get_losing_choice(a):
    if a == 1: #Rock
        return 3
    if a == 2: #Paper
        return 1
    if a == 3: #Scissors
        return 2

# X = lose
# Y = draw
# Z = win
def determine_choice(o_choice_int, outcome):
    if outcome == "Y":
        return o_choice_int
    if outcome == "X": #lose
        return get_losing_choice(o_choice_int)
    if outcome == "Z":
        return get_winning_choice(o_choice_int)
        

def part1():
    with open('./input.txt', 'r') as f:
            total_score = 0
            for line in f:
                opponent_choice_int = convert_to_int(line[0])
                opponent_choice = convert_to_name(line[0])
                
                my_choice_int = convert_to_int(line[2])
                my_choice = convert_to_name(line[2])
                score = get_score(my_choice_int, opponent_choice_int)
                total_score += score
            print("My total score: ", total_score)
    f.close()

def part2():
    with open('./input.txt', 'r') as f:
            total_score = 0
            for line in f:
                opponent_choice_int = convert_to_int(line[0])
                expected_outcome = line[2]
                my_choice_int = determine_choice(opponent_choice_int, expected_outcome)                
                score = get_score(my_choice_int, opponent_choice_int)
                total_score += score
            print("My total score: ", total_score)
    f.close()

def main():
    part1()
    part2()

main()