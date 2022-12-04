class RangeCalc:
    def __init__(self, range_str: str) -> None:
         self.min = int(range_str.split('-')[0])
         self.max = int(range_str.split('-')[1])

    def __str__(self) -> str:
         return str(self.min) + "-" + str(self.max)

def containsRange(a: RangeCalc, b: RangeCalc) -> bool:
    return (a.min >= b.min and a.max <= b.max) or (b.min >= a.min and b.max <= a.max)

def hasOverlap(a: RangeCalc, b: RangeCalc) -> bool:
    return (a.min >= b.min and a.min <= b.max) or (a.max >= b.min and a.max <= b.max) or (b.min >= a.min and b.min <= a.max) or (b.max >= a.min and b.max <= a.max)

def part1():
    with open('./input.txt', 'r') as f:
            total_count = 0
            for line in f:
                ranges = line.split(',')
                first_range = RangeCalc(ranges[0])
                second_range = RangeCalc(ranges[1])
                if containsRange(first_range, second_range):
                    print(first_range, ",", second_range)
                    total_count += 1
            print("Total fully contained ranges: ", total_count)
    f.close()

def part2():
    with open('./input.txt', 'r') as f:
            total_count = 0
            for line in f:
                ranges = line.split(',')
                first_range = RangeCalc(ranges[0])
                second_range = RangeCalc(ranges[1])
                if hasOverlap(first_range, second_range):
                    print(first_range, ",", second_range)
                    total_count += 1
            print("Total fully contained ranges: ", total_count)
    f.close()

def main():
    part1()
    part2()

main()