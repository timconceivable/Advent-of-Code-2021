#ADVENT OF CODE 2021 - DAY 1

def input_to_list(filename):
    file = open(filename)
    data_list = file.readlines()
    file.close()
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list

def increases(data_list):
    increase_num = 0
    for i in range(1, len(data_list)):
        if data_list[i] > data_list[i-1]:
            increase_num += 1
    return increase_num

def sums_of_threes(data_list):
    new_list = []
    for i in range(2, len(data_list)):
        new_list.append(data_list[i]+data_list[i-1]+data_list[i-2])
    return new_list

def main():
    #PART 1
    depths = input_to_list(r'day01-input.txt')
    total_increases = increases(depths)
    print("PART 1:", total_increases)
    
    #PART 2
    sums = sums_of_threes(depths)
    sum_increases = increases(sums)
    print("PART 2:", sum_increases, "\n")

if __name__ == "__main__":
    main()