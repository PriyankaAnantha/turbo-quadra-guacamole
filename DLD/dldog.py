"""""
import pandas as pd

def count_set_bits(number):
    return str(bin(number).count('1'))

def create_combination(number):
    return str(number)

def generate_binary_representation(number, num_variables):
    binary_rep = bin(number)[2:]
    binary_rep = binary_rep.rjust(num_variables, '0')
    return binary_rep

def find_single_bit_difference(string1, string2):
    difference_count = 0
    result = ''
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            result += string1[i]
        else:
            result += '2'
            difference_count += 1
    return result if difference_count == 1 else 0

def generate_expression(binary_string):
    expression = ''
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            expression += f'{chr(65+i)} '
        elif binary_string[i] == '0':
            expression += f'{chr(65+i)}\' '
    return expression

def get_num_variables():
    num_variables = input("Enter the number of variables in your equation: ")
    while not num_variables.isdigit() or int(num_variables) <= 0:
        print("Invalid input! Please enter a positive integer.")
        num_variables = input("Enter the number of variables in your equation: ")
    return int(num_variables)

def get_input():
    print("Enter the minterms in comma-separated format:")
    user_input = input()
    while not all(term.isdigit() for term in user_input.split(',')):
        print("Invalid input! Please enter only integers separated by commas.")
        user_input = input("Enter the minterms in comma-separated format: ")
    return user_input

num_variables = get_num_variables()
input_list = [int(term) for term in get_input().split(',')]
input_list.sort()

df_original = pd.DataFrame(columns=['Group', 'Combination', 'Binary'])

for num in input_list:
    df_original.loc[len(df_original.index)] = [count_set_bits(num), create_combination(num), generate_binary_representation(num, num_variables)]

df_original = df_original.sort_values(by='Group').reset_index(drop=True)

df_temp = pd.DataFrame(columns=['Group', 'Combination', 'Binary'])
df_result = df_original.copy()

while True:
    group_list = df_original['Group'].tolist()
    group_dict = {}
    for num in group_list:
        group_dict[num] = group_dict.get(num, 0) + 1
    unique_groups = list(group_dict.keys())

    for i in range(len(unique_groups)-1):
        if i == 0:
            pointer1 = 0
            pointer2 = pointer1 + group_dict[unique_groups[i]]
        else:
            pointer1 = pointer2
            pointer2 = pointer1 + group_dict[unique_groups[i]]
        for j in range(group_dict[unique_groups[i]]):
            for k in range(group_dict[unique_groups[i+1]]):
                difference_string = find_single_bit_difference(df_original['Binary'].iloc[pointer1+j], df_original['Binary'].iloc[pointer2+k])
                if difference_string != 0:
                    df_temp.loc[len(df_temp.index)] = [df_original['Group'].iloc[pointer1+j],
                                                        df_original['Combination'].iloc[pointer1+j] + "," + df_original['Combination'].iloc[pointer2+k],
                                                        difference_string]
                    df_result = df_result.drop(df_result[df_result['Binary'] == df_original['Binary'].iloc[pointer1+j]].index)
                    df_result = df_result.drop(df_result[df_result['Binary'] == df_original['Binary'].iloc[pointer2+k]].index)

    df_result = pd.concat([df_result, df_temp], axis=0)
    df_original = df_temp
    df_temp = df_temp[0:0]
    if len(df_original) == 0:
        break

final_binary_list = df_result['Binary'].tolist()
final_binary_list = list(set(final_binary_list))

temp_str = ''
for binary_string in final_binary_list:
    temp_str += df_result.loc[df_result['Binary'] == binary_string, 'Combination'].iloc[0] + ','

temp_str = temp_str[:-1]
temp_list = temp_str.split(",")

temp_dict = {}
for num in temp_list:
    temp_dict[num] = temp_dict.get(num, 0) + 1

essential_list = []
for binary_string in final_binary_list:
    minterm = df_result.loc[df_result['Binary'] == binary_string, 'Combination'].iloc[0]
    minterm_list = minterm.split(",")
    for comb in minterm_list:
        if temp_dict[comb] == 1:
            essential_list.append(binary_string)
            break

Minimized_expression = ''
for binary_string in essential_list:
    Minimized_expression += generate_expression(binary_string) + '+ '
Minimized_expression = Minimized_expression[:-3]
if len(Minimized_expression) == 0:
    print("The expression results in a constant, either 0 or 1")
else:
    print("The minimized expression is:", Minimized_expression)

########################

import pandas as pd

def count_set_bits(number):
    return str(bin(number).count('1'))

def create_combination(number):
    return str(number)

def generate_binary_representation(number, num_variables):
    binary_rep = bin(number)[2:]
    binary_rep = binary_rep.rjust(num_variables, '0')
    return binary_rep

def find_single_bit_difference(string1, string2):
    difference_count = 0
    result = ''
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            result += string1[i]
        else:
            result += '2'
            difference_count += 1
    return result if difference_count == 1 else 0

def generate_expression(binary_string):
    expression = ''
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            expression += f'{chr(65+i)} '
        elif binary_string[i] == '0':
            expression += f'{chr(65+i)}\' '
    return expression

def get_num_variables():
    num_variables = input("Enter the number of variables in your equation: ")
    while not num_variables.isdigit() or int(num_variables) <= 0:
        print("Invalid input! Please enter a positive integer.")
        num_variables = input("Enter the number of variables in your equation: ")
    return int(num_variables)

def get_name():
    user_name = input("Enter your name in uppercase: ")
    while not user_name.isupper():
        print("Invalid input! Please enter your name in uppercase.")
        user_name = input("Enter your name in uppercase: ")
    return user_name

def generate_minterms_from_name(user_name):
    minterms = set()
    for char in user_name:
        ascii_code = ord(char)
        if ascii_code not in minterms:
            minterms.add(ascii_code)
    return minterms

def find_min_variables(input_list):
    max_minterm = max(input_list)
    num_variables = 1
    while not (max_minterm <= ((2**num_variables)-1)):
        num_variables += 1
    return num_variables

variant = input("Which variant do you want to solve?\nEnter '1' for normal QM technique or '2' to generate minterms from your name's ASCII code: ")

if variant == '1':
    num_variables_known = input("Do you know the number of variables in your equation? (y/n): ")
    if num_variables_known.lower() == 'y':
        num_variables = get_num_variables()
    else:
        input_list = [int(term) for term in input("Enter the minterms in comma-separated format: ").split(',')]
        num_variables = find_min_variables(input_list)
        print("The minimum number of variables based on your input is:", num_variables)
        print("The equation contains", num_variables, f"variables named A to {chr(64+num_variables)}")
        print()

elif variant == '2':
    user_name = get_name()
    minterms = generate_minterms_from_name(user_name)
    print("Minterms generated from the name's ASCII code:", minterms)
    input_list = list(minterms)
    num_variables = find_min_variables(input_list)
    print("The minimum number of variables based on your name's ASCII code is:", num_variables)
    print("The equation contains", num_variables, f"variables named A to {chr(64+num_variables)}")
    print()

else:
    print("Invalid input! Please enter either '1' or '2'.")

input_list.sort()

df_original = pd.DataFrame(columns=['Group', 'Combination', 'Binary'])

for num in input_list:
    df_original.loc[len(df_original.index)] = [count_set_bits(num), create_combination(num), generate_binary_representation(num, num_variables)]

df_original = df_original.sort_values(by='Group').reset_index(drop=True)

df_temp = pd.DataFrame(columns=['Group', 'Combination', 'Binary'])
df_result = df_original.copy()

while True:
    group_list = df_original['Group'].tolist()
    group_dict = {}
    for num in group_list:
        group_dict[num] = group_dict.get(num, 0) + 1
    unique_groups = list(group_dict.keys())

    for i in range(len(unique_groups)-1):
        if i == 0:
            pointer1 = 0
            pointer2 = pointer1 + group_dict[unique_groups[i]]
        else:
            pointer1 = pointer2
            pointer2 = pointer1 + group_dict[unique_groups[i]]
        for j in range(group_dict[unique_groups[i]]):
            for k in range(group_dict[unique_groups[i+1]]):
                difference_string = find_single_bit_difference(df_original['Binary'].iloc[pointer1+j], df_original['Binary'].iloc[pointer2+k])
                if difference_string != 0:
                    df_temp.loc[len(df_temp.index)] = [df_original['Group'].iloc[pointer1+j],
                                                        df_original['Combination'].iloc[pointer1+j] + "," + df_original['Combination'].iloc[pointer2+k],
                                                        difference_string]
                    df_result = df_result.drop(df_result[df_result['Binary'] == df_original['Binary'].iloc[pointer1+j]].index)
                    df_result = df_result.drop(df_result[df_result['Binary'] == df_original['Binary'].iloc[pointer2+k]].index)

    df_result = pd.concat([df_result, df_temp], axis=0)
    df_original = df_temp
    df_temp = df_temp[0:0]
    if len(df_original) == 0:
        break

final_binary_list = df_result['Binary'].tolist()
final_binary_list = list(set(final_binary_list))

temp_str = ''
for binary_string in final_binary_list:
    temp_str += df_result.loc[df_result['Binary'] == binary_string, 'Combination'].iloc[0] + ','

temp_str = temp_str[:-1]
temp_list = temp_str.split(",")

temp_dict = {}
for num in temp_list:
    temp_dict[num] = temp_dict.get(num, 0) + 1

essential_list = []
for binary_string in final_binary_list:
    minterm = df_result.loc[df_result['Binary'] == binary_string, 'Combination'].iloc[0]
    minterm_list = minterm.split(",")
    for comb in minterm_list:
        if temp_dict[comb] == 1:
            essential_list.append(binary_string)
            break

Minimized_expression = ''
for binary_string in essential_list:
    Minimized_expression += generate_expression(binary_string) + '+ '
Minimized_expression = Minimized_expression[:-3]
if len(Minimized_expression) == 0:
    print("The expression results in a constant, either 0 or 1")
else:
    print("The minimized expression is:", Minimized_expression)

"""

import pandas as pd

def count_set_bits(number):
    return str(bin(number).count('1'))

def create_combination(number):
    return str(number)

def generate_binary_representation(number, num_variables):
    binary_rep = bin(number)[2:]
    binary_rep = binary_rep.rjust(num_variables, '0')
    return binary_rep

def find_single_bit_difference(string1, string2):
    difference_count = 0
    result = ''
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            result += string1[i]
        else:
            result += '2'
            difference_count += 1
    return result if difference_count == 1 else 0

def generate_expression(binary_string):
    expression = ''
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            expression += f'{chr(65+i)} '
        elif binary_string[i] == '0':
            expression += f'{chr(65+i)}\' '
    return expression

def get_num_variables():
    num_variables = input("Enter the number of variables in your equation: ")
    while not num_variables.isdigit() or int(num_variables) <= 0:
        print("Invalid input! Please enter a positive integer.")
        num_variables = input("Enter the number of variables in your equation: ")
    return int(num_variables)

def get_name():
    user_name = input("Enter your name in uppercase without spaces, separated by commas: ")
    while not user_name.replace(",", "").isalpha() or " " in user_name:
        print("Invalid input! Please enter your name in uppercase without spaces.")
        user_name = input("Enter your name in uppercase without spaces, separated by commas: ")
    return user_name

def generate_minterms_from_name(user_name):
    minterms = set()
    for char in user_name.replace(",", ""):
        ascii_code = ord(char)
        if ascii_code not in minterms:
            minterms.add(ascii_code)
    return minterms

def find_min_variables(input_list):
    max_minterm = max(input_list)
    num_variables = 1
    while not (max_minterm <= ((2**num_variables)-1)):
        num_variables += 1
    return num_variables

while True:
    variant = input("Which question do you want to solve?\n\n\tEnter:\n'1' for normal QM technique or '2' to generate minterms from your name's ASCII code or 'exit' to quit: ")

    if variant == 'exit':
        print("Exiting the program...")
        break

    if variant == '1':
        num_variables_known = input("Do you know the number of variables in your equation? (y/n): ")
        if num_variables_known.lower() == 'y':
            num_variables = get_num_variables()
        else:
            input_list = [int(term) for term in input("Enter the minterms in comma-separated format: ").split(',')]
            num_variables = find_min_variables(input_list)
            print("The minimum number of variables based on your input is:", num_variables)
            print("The equation contains", num_variables, f"variables named A to {chr(64+num_variables)}")
            print()

    elif variant == '2':
        user_name = get_name()
        minterms = generate_minterms_from_name(user_name)
        print("Minterms generated from the name's ASCII code:", minterms)
        input_list = list(minterms)
        num_variables = find_min_variables(input_list)
        print("The minimum number of variables based on your name's ASCII code is:", num_variables)
        print("The equation contains", num_variables, f"variables named A to {chr(64+num_variables)}")
        print()

    else:
        print("Invalid input! Please enter either '1', '2', or 'exit'.")

    input_list.sort()

    df_original = pd.DataFrame(columns=['Group', 'Combination', 'Binary'])

    for num in input_list:
        df_original.loc[len(df_original.index)] = [count_set_bits(num), create_combination(num), generate_binary_representation(num, num_variables)]

    df_original = df_original.sort_values(by='Group').reset_index(drop=True)

    df_temp = pd.DataFrame(columns=['Group', 'Combination', 'Binary'])
    df_result = df_original.copy()

    while True:
        group_list = df_original['Group'].tolist()
        group_dict = {}
        for num in group_list:
            group_dict[num] = group_dict.get(num, 0) + 1
        unique_groups = list(group_dict.keys())

        for i in range(len(unique_groups)-1):
            if i == 0:
                pointer1 = 0
                pointer2 = pointer1 + group_dict[unique_groups[i]]
            else:
                pointer1 = pointer2
                pointer2 = pointer1 + group_dict[unique_groups[i]]
            for j in range(group_dict[unique_groups[i]]):
                for k in range(group_dict[unique_groups[i+1]]):
                    difference_string = find_single_bit_difference(df_original['Binary'].iloc[pointer1+j], df_original['Binary'].iloc[pointer2+k])
                    if difference_string != 0:
                        df_temp.loc[len(df_temp.index)] = [df_original['Group'].iloc[pointer1+j],
                                                            df_original['Combination'].iloc[pointer1+j] + "," + df_original['Combination'].iloc[pointer2+k],
                                                            difference_string]
                        df_result = df_result.drop(df_result[df_result['Binary'] == df_original['Binary'].iloc[pointer1+j]].index)
                        df_result = df_result.drop(df_result[df_result['Binary'] == df_original['Binary'].iloc[pointer2+k]].index)

        df_result = pd.concat([df_result, df_temp], axis=0)
        df_original = df_temp
        df_temp = df_temp[0:0]
        if len(df_original) == 0:
            break

    final_binary_list = df_result['Binary'].tolist()
    final_binary_list = list(set(final_binary_list))

    temp_str = ''
    for binary_string in final_binary_list:
        temp_str += df_result.loc[df_result['Binary'] == binary_string, 'Combination'].iloc[0] + ','

    temp_str = temp_str[:-1]
    temp_list = temp_str.split(",")

    temp_dict = {}
    for num in temp_list:
        temp_dict[num] = temp_dict.get(num, 0) + 1

    essential_list = []
    for binary_string in final_binary_list:
        minterm = df_result.loc[df_result['Binary'] == binary_string, 'Combination'].iloc[0]
        minterm_list = minterm.split(",")
        for comb in minterm_list:
            if temp_dict[comb] == 1:
                essential_list.append(binary_string)
                break

    Minimized_expression = ''
    for binary_string in essential_list:
        Minimized_expression += generate_expression(binary_string) + '+ '
    Minimized_expression = Minimized_expression[:-3]
    if len(Minimized_expression) == 0:
        print("The expression results in a constant, either 0 or 1")
    else:
        print("The minimized expression is:", Minimized_expression)

































