def input_info():
    name = input("Enter name: ").strip()
    roll_no = int(input("Enter Roll Number: ").strip())
    return (name, roll_no)

def print_info(name, roll_no):
    print("Name:", name)
    print("Roll Number:", roll_no)


inp_name, inp_roll = input_info()
print('\n') #makes output more readable
print_info(inp_name, inp_roll)
