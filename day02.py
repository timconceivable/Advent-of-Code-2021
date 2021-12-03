#ADVENT OF CODE 2021 - DAY 2

def input_to_list(filename):
    file = open(filename)
    data_list = file.read().splitlines()
    file.close()
    for i in range(len(data_list)):
        data_list[i] = (data_list[i][0:-2], int(data_list[i][-1]))
    return data_list

def move_to(data_list):
    x_pos = 0
    depth = 0
    for command in data_list:
        if "forward" in command:
            x_pos += command[1]
        if "down" in command:
            depth += command[1]
        if "up" in command:
            depth -= command[1]
    return x_pos, depth

def aim_to_move(data_list):
    x_pos = 0
    depth = 0
    aim = 0
    for command in data_list:
        if "forward" in command:
            x_pos += command[1]
            depth += aim*command[1]
        if "down" in command:
            aim += command[1]
        if "up" in command:
            aim -= command[1]
    return x_pos, depth

def main():
    #PART 1
    commands = input_to_list(r'day02-input.txt')
    position1 = move_to(commands)
    print("PART 1: \n   horizontal:", position1[0], 
        "\n   depth:", position1[1], 
        "\n   factor:", (position1[0]*position1[1]))

    #PART 2
    position2 = aim_to_move(commands)
    print("PART 2: \n   horizontal:", position2[0], 
        "\n   depth:", position2[1], 
        "\n   factor:", (position2[0]*position2[1]), "\n")

if __name__ == "__main__":
    main()