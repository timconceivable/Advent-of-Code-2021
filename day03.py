#ADVENT OF CODE 2021 - DAY 3

def input_to_list(filename):
    file = open(filename)
    data_list = file.read().splitlines()
    file.close()
    return data_list

def convert_to_decimal(binary):
    return int(binary, 2)

def find_gamma(data_list):
    data_len = len(data_list)
    binary_len = len(data_list[0])
    gamma_list = [0]*binary_len
    for binary in data_list:
        for i in range(binary_len):
            if binary[i] is "1":
                gamma_list[i] += 1
    gamma_binary = ""
    for n in gamma_list:
        bit = round(int(n)/data_len)
        gamma_binary = gamma_binary+str(bit)
    return gamma_binary

def find_epsilon(binary):
    new_binary = ""
    for i in binary:
        if i is "1":
            new_binary += "0"
        elif i is "0":
            new_binary += "1"
    return new_binary

def main():
    #PART 1
    x = "_"
    diagnostic = input_to_list(r'day03-input.txt')
    gamma = find_gamma(diagnostic)
    gamma_decimal = convert_to_decimal(gamma)
    epsilon = find_epsilon(gamma)
    epsilon_decimal = convert_to_decimal(epsilon)
    power = gamma_decimal*epsilon_decimal
    print("PART 1: \n   gamma rate: ", gamma, "  (", gamma_decimal, ")",
        "\n   epsilon rate: ", epsilon, "  (", epsilon_decimal, ")",
        "\n   power consumption: ", power, sep="")

    #PART 2

    print("PART 2: \n   gamma rate:", x, 
        "\n   epsilon:", x, 
        "\n   power consumption:", x, "\n")

if __name__ == "__main__":
    main()