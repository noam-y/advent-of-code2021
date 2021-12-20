import re

def get_binary_values(binary_text):
    length_of_text = len(binary_text.split()[0])
    gamma_rate= ''
    epsilon_rate= ''
    for i in range(length_of_text):
        search_regex = r"\n[0-1]{"+ str(i) +r"}([0-1])"
        print(search_regex)
        binary_value_in_place_i = re.findall( search_regex,binary_text )
        print(binary_value_in_place_i, length_of_text)
        int_binary_value_in_place_i = list(map(int, binary_value_in_place_i))
        print(sum(int_binary_value_in_place_i) / length_of_text, 0)
        final_binary_digit = int(round(sum(int_binary_value_in_place_i) / len(int_binary_value_in_place_i), 0))
        gamma_rate = gamma_rate + str(final_binary_digit)
        epsilon_rate = epsilon_rate + str(abs(int(final_binary_digit)-1))
    gamma_rate = int(gamma_rate,2)
    epsilon_rate = int(epsilon_rate,2)
    print("gamma: {0}, epsilon: {1}, final:{2}".format(gamma_rate,epsilon_rate,int(gamma_rate)*int(epsilon_rate)))    


def get_binaryk_values(binary_text):
    options = binary_text.split()
    # while high_options < 1:
    #     higher_search_regex = r"\n" + joker_value_higher + r"([0-1])"
    #     next_bit = list(re.findall( higher_search_regex, binary_text ))
    #     high_count_each_value = {j:higher_value_in_place_i.count(str(j)) for j in [0,1]}
    #     joker_value_higher+= '1' if next_bit.count(1) >= next_bit.count(0) else joker_value_higher+= '0'
    #     print(joker_value_higher)
    #     joker_value_higher += str(max(high_count_each_value, key=count_each_value.get()))
    joker =''
    ljoker= ''
    lplace= 0
    place = 0
    laddjoker = ''
    while len(options) > 1 and len(joker) < len(options[0]):
        options = list(filter(lambda x: x.find(joker) == 0, options))
        print('highest',joker, 'options', options)
        if len(options) == 1:
            joker = options[0]
            break
        first_bit = [i[len(joker)] for i in options]
        counting_bits = {i:first_bit.count(i) for i in ['0','1']}
        addjoker = '1' if counting_bits['1'] >= counting_bits['0'] else '0'
        print('adding low',addjoker)
        joker = str(joker) + str(addjoker)

    
    options = binary_text.split()
    while len(options) > 1 and len(ljoker) < len(options[0]):
        options = list(filter(lambda x: x.find(ljoker) == 0, options))
        if len(options) == 1:
            ljoker = options[0]
            break
        print('lowest',ljoker, 'options', options)
        first_bit = [i[len(ljoker)] for i in options]
        counting_bits = {i:first_bit.count(i) for i in ['0','1']}
        print(counting_bits)
        laddjoker = '1' if counting_bits['0'] > counting_bits['1'] else '0'
        print('adding low',laddjoker)
        ljoker = str(ljoker) + str(laddjoker)

    #ans = int(joker,2)* int(ljoker,2)
    print('low:', ljoker, 'high', joker, 'multi:')
    co2 = int(ljoker,2)
    oxygen = int(joker,2)
    print(co2*oxygen)


with open('..\\reference\day-3.txt') as f:
    get_binaryk_values(f.read())


