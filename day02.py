#ADVENT OF CODE 2021 - DAY 2

def input_to_list(filename):
    file = open(filename)
    data_list = file.readlines()
    file.close()
    for i in range(len(data_list)):
        data_list[i] = (data_list[i][0:-3], int(data_list[i][-2]))
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

def main():
    #PART 1
    commands = input_to_list(r'day02-input.txt')
    position = move_to(commands)
    print("horizontal:", position[0], " depth:", position[1], " factor:", (position[0]*position[1]))

    #PART 2
    print("part 2")

if __name__ == "__main__":
    main()