import re
from array import *



class Stack:
    arr = []
    def __init__(self) -> None:
        pass
    
    def reverseStack(self) -> None:
        self.arr.reverse()

    def addItem(self, s: str):
        self.arr.append(s)
    
    def removeN(self, n: int) -> list:
        ret = self.arr[: len(self.arr) - n]
        return ret

T = [Stack() for i in range(9)]

def do_move(line: str):
    moves = re.findall(r'\d+', line)
    num_to_move = int(moves[0])
    from_box = int(moves[1])
    to_box = int(moves[2])
    #print("moving ", num_to_move, " from ", from_box, " to ", to_box)

def process_input(line: str):
    n = 4
    my_list = [line[idx:idx + n].rstrip() for idx in range(0, len(line), n)]
    for idx, i in enumerate(my_list):
        if i != '':
            T[idx].addItem(i)


with open('./input.txt', 'r') as f:
    for line in f:
        if line.startswith("move"):
            do_move(line)
        else:
            process_input(line)
    for i in T:
        print(i.arr)
f.close()