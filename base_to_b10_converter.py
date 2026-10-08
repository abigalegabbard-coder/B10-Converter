num = input("Enter number to be converted to base 10: ")
base = int(input(f"Enter base that {num} is in: "))

def convert_base_to_b10(num, base):
    """Converts a chosen base and numbers from that base to base 10"""
    total = 0
    power = 0
    for digit in reversed(num):
        value = int(digit)
        if value >= base:
            print(f"{value} is not a valid digit for base {base}.")
            return None
        new_num = value * (base ** power)
        print(f"{digit}*({base}**{power}) = {new_num}")
        total += new_num
        power+=1
    return total
answer = convert_base_to_b10(num, base)

if answer is not None:
    print(answer)