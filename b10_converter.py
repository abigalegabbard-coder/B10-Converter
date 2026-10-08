num = int(input("Enter a number to convert: "))
usernewbase = int(input("Enter a new base: "))

def convert_base10_to_newbase(num, newbase):
    """Converts a user input from base 10 to another chosen base"""
    new_num = []
    while num > 0:
        remainder = num%newbase
        print(f"{num}/{newbase} = {num//newbase} r {remainder}")
        num = num//newbase
        new_num.insert(0, str(remainder))
    return "".join(new_num)
print(convert_base10_to_newbase(num, usernewbase))