
def count_increasing(list_of_nums):
    count_of_increase = 0
    for i in range(0,len(list_of_nums)-1):
        #print(i)
        if list_of_nums[i+1] - list_of_nums[i] > 0:
            count_of_increase += 1
    print('count of increase is:', count_of_increase)


def count_thirds_increasing(list_of_nums):
    count_of_increase = 0
    for i in range(0,len(list_of_nums)-3):
        #print(i)
        if list_of_nums[i+3] - list_of_nums[i] > 0:
            count_of_increase += 1
    print('countthirds of increase is:', count_of_increase)

with open('day-1.txt') as f:
    numberlist = list(map(lambda x: int(x), f.readlines()))
    count_thirds_increasing(numberlist)
    count_increasing(numberlist)



    