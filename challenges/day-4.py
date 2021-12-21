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
        for board1 in boards_list:
            board_numbers = [val for sublist in board1 for val in sublist]
            if numbers_drawn[-1] in [val for sublist in board1 for val in sublist]:
                
                for board in [board1,list(zip(*reversed(board1)))]:
                    for line in board:
                        print('lineee', line)
                        if all([digit in numbers_drawn for digit in line]):
                            print('BINGO@ line ', line)
                            print('board', board_numbers, '\n numbers drawn', numbers_drawn)
                            sum_of_nums = sum(list(set([int(i) for i in board_numbers]).difference(set([int(i) for i in numbers_drawn]))))
                            return sum_of_nums * int(numbers_drawn[-1])

def losing_board(f):
    text_split = f.split('\n\n')
    drawing_list = text_split.pop(0).split(',')
    print('dddddd',drawing_list)
    #print('board', text_split)
    boards_list = [[j.split() for j in i.split('\n')] for i in text_split]
    print('booool', boards_list[2]) # this gives away numbers kept like str

    numbers_drawn = []
    while len(drawing_list) > 1:
        numbers_drawn.append(drawing_list.pop(0))
        for board1 in boards_list:
            board_numbers = [val for sublist in board1 for val in sublist]
            if numbers_drawn[-1] in [val for sublist in board1 for val in sublist]:
                
                for board in [board1,list(zip(*reversed(board1)))]:
                    for line in board:
                        print('lineee', line)
                        if all([digit in numbers_drawn for digit in line]):
                            print('BINGO@ line ', line)
                            print('board', board_numbers, '\n numbers drawn', numbers_drawn)
                            print('others', len(boards_list))
                            boards_list.remove(board1)
                            if len(boards_list) == 0:
                                sum_of_nums = sum(list(set([int(i) for i in board_numbers]).difference(set([int(i) for i in numbers_drawn]))))
                                return sum_of_nums*int(numbers_drawn[-1])


with open('..\\reference\day-4.txt') as f:
    iii = losing_board(f.read())
    print(iii)

