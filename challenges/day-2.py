def get_location(direction_list):
    forwards = filter(lambda x: 'forward' in x, direction_list)
    ups = filter(lambda x: 'up' in x, direction_list)
    downs = filter(lambda x: 'down' in x, direction_list)
    dict_of_directions = {'up':0 , 'down':0, 'forward':0}
    for direction in direction_list:
        #print('dict_of_directions[direction.split()[0]] ',direction.split()[0], direction.split()[1] )
        dict_of_directions[direction.split()[0]] = int(dict_of_directions[direction.split()[0]]) + int(direction.split()[1])
    print(dict_of_directions)



with open('..\\reference\day-2.txt') as f:
    direction_list = f.readlines()
    get_location(direction_list)
