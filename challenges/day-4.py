import re

def winning_board(f):
    text_split = f.split('\n\n')
    drawing_list = text_split.pop(0).split(',')
    print('dddddd',drawing_list)
    #print('board', text_split)
    boards_list = [[j.split() for j in i.split('\n')] for i in text_split]
    print('booool', boards_list[2]) # this gives away numbers kept like str

    numbers_drawn = []
    while len(drawing_list) > 0:
        numbers_drawn.append(drawing_list.pop(0))
        for board in boards_list:
            board_numbers = [val for sublist in board for val in sublist]
            if numbers_drawn[-1] in [val for sublist in board for val in sublist]:
                for line in board:
                    print('lineee', line)
                    if all([digit in numbers_drawn for digit in line]):
                        print('BINGO@ line ', line)
                        print('board', board_numbers, '\n numbers drawn', numbers_drawn)
                        sum_of_nums = set([board_numbers]).difference(set(numbers_drawn))
                        return sum_of_nums

with open('..\\reference\day-4.txt') as f:
    iii = winning_board(f.read())
    print(iii)

