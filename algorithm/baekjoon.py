def bag_num(sugar):
    digit = len(sugar)
    result = 0
    bag_num_list = [0, 3, 4, 3, 4, 3, 4, 5, 4, 5]
    if int(sugar[-2:]) < 10:
        bag_num_list = [0, -1, -1 ,1, -1, 1, 2, -1, 2, 3]
    elif int(sugar) < 20:
        bag_num_list[0] += 2
        return bag_num_list[int(sugar[-1])]
        
    units_digit = int(sugar[-1])
    for i in range(0, digit - 1):
        result += int(sugar[-i-2]) * 2 * 10 ** i
    if bag_num_list[units_digit] == -1:
        return -1
    result += bag_num_list[units_digit]
    return result

if __name__ == "__main__":
    sugar = input()
    print(bag_num(sugar))