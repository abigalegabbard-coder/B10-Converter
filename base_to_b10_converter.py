num = input("Enter line of code to be converted to base 10: ")
base = int(input("Enter base to be converted into: "))

def convert_base_to_b10(num):
    """runs through the converting process"""
    numbers_to_add = []
    power_of = 0
    searching = 0
    while searching <= len(num) or power_of <= len(num):
        new_num = num[0]*base**power_of
        print(f"{num[searching]}*{base}**{power_of} = {new_num}")
        power_of+1
        searching+1
        numbers_to_add.append(new_num)
    return "".join(numbers_to_add)
convert_base_to_b10(num)