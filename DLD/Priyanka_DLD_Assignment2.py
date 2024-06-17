"""
@Author: Priyanka A
Date: 7 May 2024

Script overview:
    This code implements the Quine-McCluskey algorithm for minimizing boolean expressions.
    It allows users to input minterms manually or generate them from their uppercase first name's ASCII code.
    The algorithm reduces the expression to its simplest form and outputs the minimized SoP expression.

Functions:
    count_set_bits(number):
        Counts the number of set bits (1s) in a binary representation of a given number.

    create_combination(number):
        Creates a string representation of a number for further processing in combinations.

    generate_binary_representation(number, num_variables):
        Generates the binary representation of a number, padded to the specified number of variables.

    find_single_bit_difference(string1, string2):
        Finds the difference between two binary strings with exactly one bit difference and returns a string
        with '-' indicating the differing bit, or None if there is not exactly one bit difference.

    generate_expression(binary_string):
        Converts a binary string into a boolean expression with variables A, B, C, etc.

    get_num_variables():
        Prompts the user to enter the number of variables for their equation and validates the input.

    get_input():
        Prompts the user to enter minterms in a comma-separated format and validates the input.

    get_name():
        Prompts the user to enter their first name in uppercase and validates the input.

    generate_minterms_from_name(user_name):
        Generates a list of minterms from the ASCII values of the characters in the user's name.

    find_min_variables(input_list):
        Determines the minimum number of variables required to represent the given minterms.

    display_menu():
        Displays the main menu options for the user to choose between manual input and name-based minterm generation.

    main():
        Main function that orchestrates the user interaction and the Quine-McCluskey algorithm to minimize boolean expressions.
"""

import pandas as pd

def count_set_bits(number):
    """
    Count the number of set bits in a binary number.

    Args:
        number (int): The number to count set bits in.

    Returns:
        int: The count of set bits.
    """
    return bin(number).count('1')

def create_combination(number):
    """
    Create a string representation of a number.

    Args:
        number (int): The number to convert to string.

    Returns:
        str: The string representation of the number.
    """
    return str(number)

def generate_binary_representation(number, num_variables):
    """
    Generate the binary representation of a number, padded to the specified number of variables.

    Args:
        number (int): The number to convert to binary.
        num_variables (int): The number of variables (bits) to pad to.

    Returns:
        str: The padded binary string.
    """
    return bin(number)[2:].rjust(num_variables, '0')

def find_single_bit_difference(string1, string2):
    """
    Find the difference between two binary strings with exactly one bit difference.

    Args:
        string1 (str): The first binary string.
        string2 (str): The second binary string.

    Returns:
        str: A new string with '-' indicating the differing bit, or None if there is not exactly one bit difference.
    """
    difference_count = 0
    result = ''
    for bit1, bit2 in zip(string1, string2):
        if bit1 == bit2:
            result += bit1
        else:
            result += '-'
            difference_count += 1
    return result if difference_count == 1 else None

def generate_expression(binary_string):
    """
    Convert a binary string into a boolean expression with variables A, B, C, etc.

    Args:
        binary_string (str): The binary string to convert.

    Returns:
        str: The boolean expression.
    """
    expression = ''
    for i, bit in enumerate(binary_string):
        if bit == '1':
            expression += f'{chr(65 + i)}'
        elif bit == '0':
            expression += f'{chr(65 + i)}\''
    return expression

def get_num_variables():
    """
    Prompt the user to enter the number of variables for their equation and validate the input.

    Returns:
        int: The number of variables.
    """
    while True:
        num_variables = input("Enter the number of variables in your equation\nInput: ")
        if num_variables.isdigit() and int(num_variables) > 0:
            return int(num_variables)
        else:
            print("Invalid input! Exiting...")

def get_input():
    """
    Prompt the user to enter minterms in a comma-separated format and validate the input.

    Returns:
        list[int]: The list of minterms.
    """
    while True:
        user_input = input("Enter the minterms in comma-separated format\nInput: ")
        minterms = user_input.split(',')
        if all(term.isdigit() for term in minterms):
            return [int(term) for term in minterms]
        else:
            print("Invalid input! Exiting...")

def get_name():
    """
    Prompt the user to enter their first name in uppercase and validate the input.

    Returns:
        str: The user's first name in uppercase.
    """
    while True:
        user_name = input("Enter your first name in uppercase\nInput: ")
        if user_name.isupper():
            return user_name
        else:
            print("Invalid input! Exiting...")

def generate_minterms_from_name(user_name):
    """
    Generate a list of minterms from the ASCII values of the characters in the user's name.

    Args:
        user_name (str): The user's first name in uppercase.

    Returns:
        list[int]: The list of minterms generated from the ASCII values.
    """
    minterms = {ord(char) for char in user_name}
    return list(minterms)

def find_min_variables(input_list):
    """
    Determine the minimum number of variables required to represent the given minterms.

    Args:
        input_list (list[int]): The list of minterms.

    Returns:
        int: The minimum number of variables.
    """
    max_minterm = max(input_list)
    num_variables = 1
    while max_minterm >= (1 << num_variables):
        num_variables += 1
    return num_variables

def display_menu():
    """
    Display the main menu options for the user to choose between manual input and name-based minterm generation.
    """
    print("\n" + "-"*38)
    print("--- Quine-McCluskey Implementation ---")
    print("-"*38 + "\n")
    print("1. Solve using normal QM technique")
    print("2. Generate minterms and apply QM from your first name's ASCII code\n")

def main():
    """
    Main function that orchestrates the user interaction and the Quine-McCluskey algorithm to minimize boolean expressions.
    """
    display_menu()
    variant = input("Input: ")

    if variant == '1':
        num_variables_known = input("Do you know the number of variables in your equation? (y/n): ").lower()
        if num_variables_known == 'y':
            num_variables = get_num_variables()
            input_list = get_input()
        elif num_variables_known == 'n':
            input_list = get_input()
            num_variables = find_min_variables(input_list)
            print(f"\nThe minimum number of variables based on your input is: {num_variables}")
            print(f"The equation contains {num_variables} variables named A to {chr(64 + num_variables)}\n")
        else:
            print("Invalid input! Exiting...")
            return

    elif variant == '2':
        user_name = get_name()
        minterms = generate_minterms_from_name(user_name)
        print(f"\nMinterms generated from the name's ASCII code: {minterms}")
        input_list = minterms
        num_variables = find_min_variables(input_list)
        print(f"\nThe minimum number of variables based on your name's ASCII code is: {num_variables}")
        print(f"The equation contains {num_variables} variables named A to {chr(64 + num_variables)}\n")
    else:
        print("Invalid input! Exiting...")
        return

    input_list.sort()
    df_original = pd.DataFrame(columns=['Group', 'Combination', 'Binary'])
    for num in input_list:
        df_original.loc[len(df_original.index)] = [count_set_bits(num), create_combination(num), generate_binary_representation(num, num_variables)]

    df_original = df_original.sort_values(by='Group').reset_index(drop=True)
    df_temp = pd.DataFrame(columns=['Group', 'Combination', 'Binary'])
    df_result = df_original.copy()

    while not df_original.empty:
        group_list = df_original['Group'].tolist()
        group_dict = {num: group_list.count(num) for num in group_list}
        unique_groups = list(group_dict.keys())

        for i in range(len(unique_groups) - 1):
            pointer1 = sum(group_dict[unique_groups[j]] for j in range(i))
            pointer2 = pointer1 + group_dict[unique_groups[i]]
            for j in range(group_dict[unique_groups[i]]):
                for k in range(group_dict[unique_groups[i + 1]]):
                    diff_string = find_single_bit_difference(df_original['Binary'].iloc[pointer1 + j], df_original['Binary'].iloc[pointer2 + k])
                    if diff_string:
                        df_temp.loc[len(df_temp.index)] = [df_original['Group'].iloc[pointer1 + j],
                                                          df_original['Combination'].iloc[pointer1 + j] + "," + df_original['Combination'].iloc[pointer2 + k],
                                                          diff_string]
                        df_result = df_result[df_result['Binary'] != df_original['Binary'].iloc[pointer1 + j]]
                        df_result = df_result[df_result['Binary'] != df_original['Binary'].iloc[pointer2 + k]]

        df_result = pd.concat([df_result, df_temp], axis=0)
        df_original = df_temp.copy()
        df_temp = df_temp.iloc[0:0]

    final_binary_list = list(set(df_result['Binary'].tolist()))
    temp_str = ','.join(df_result.loc[df_result['Binary'].isin(final_binary_list), 'Combination'].tolist())
    temp_list = temp_str.split(',')
    temp_dict = {num: temp_list.count(num) for num in temp_list}

    essential_list = []
    for binary_string in final_binary_list:
        minterm = df_result.loc[df_result['Binary'] == binary_string, 'Combination'].iloc[0]
        minterm_list = minterm.split(",")
        if any(temp_dict[comb] == 1 for comb in minterm_list):
            essential_list.append(binary_string)

    remaining_implicants = [implicant for implicant in final_binary_list if implicant not in essential_list]
    covered_minterms = set()
    for essential in essential_list:
        covered_minterms.update(df_result[df_result['Binary'] == essential]['Combination'].iloc[0].split(','))

    while remaining_implicants:
        max_covered = 0
        best_implicant = None
        for implicant in remaining_implicants:
            minterms = set(df_result[df_result['Binary'] == implicant]['Combination'].iloc[0].split(','))
            covered = len(minterms - covered_minterms)
            if covered > max_covered:
                max_covered = covered
                best_implicant = implicant

        if best_implicant is None:
            break

        essential_list.append(best_implicant)
        covered_minterms.update(df_result[df_result['Binary'] == best_implicant]['Combination'].iloc[0].split(','))
        remaining_implicants.remove(best_implicant)

    minimized_expression = ' + '.join(generate_expression(binary_string) for binary_string in essential_list)
    if not minimized_expression:
        print("\nThe expression results in a constant, either 0 or 1")
    else:
        print("\n" + "-"*30)
        print(f"\nThe minimized expression is:\n\n{minimized_expression}")
        print("\n" + "-"*30 + "\n")

if __name__ == "__main__":
    main()
