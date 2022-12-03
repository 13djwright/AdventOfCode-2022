def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

def part1():
    with open('./input.txt', 'r') as f:
            total_score = 0
            for line in f:
                compartment_one = line[:len(line)//2]
                compartment_two = line[len(line)//2:]
                common_letter = ''.join(set(compartment_one).intersection(compartment_two))
                total_score += get_priority(common_letter)
            print("total: ", total_score)
    f.close()

def part2():
    with open('./input.txt', 'r') as f:
        line_count = 0
        total_score = 0
        arr = []
        for line in f:
            if (line_count == 3):
                print(arr)
                common_letter = ''.join(set(arr[0]).intersection(arr[1]).intersection(arr[2]))
                total_score += get_priority(common_letter)
                arr.clear()
                line_count = 0
            arr.append(line.rstrip())
            line_count += 1
        print(arr)
        common_letter = ''.join(set(arr[0]).intersection(arr[1]).intersection(arr[2]))
        total_score += get_priority(common_letter)
        print("total: ", total_score)
    f.close()

def main():
    part1()
    part2()

main()