import pandas as pd
import re

def clean_input_string(input_string):
  cleaned_string = re.sub(r'[^0-9,]', '', input_string)
  cleaned_string = re.sub(r',{2,}', ',', cleaned_string)
  cleaned_string = cleaned_string.strip(',')
  return cleaned_string


def calculate_group(n):
  binary_representation = bin(n)[2:]
  group = sum(int(bit) for bit in binary_representation)
  return str(group)


def calculate_combo(n):
  return str(n)


def calculate_binary_representation(n, num_variables):
  binary_representation = bin(n)[2:]
  binary_representation = binary_representation.rjust(num_variables, '0')
  return binary_representation


def create_combined_string(s1, s2):
  count = 0
  combined_string = ''
  for i in range(len(s1)):
    if s1[i] == s2[i]:
      combined_string += s1[i]
    else:
      combined_string += '2'
      count += 1
  if count == 1:
    return combined_string
  else:
    return 0


def generate_expression(s):
  expression = ''
  for i in range(len(s)):
    if s[i] == '1':
      expression += chr(65 + i)  # Use uppercase letters starting from 'A'
    elif s[i] == '0':
      expression += chr(65 + i) + "'"  # Add "'" for complement
  return expression


if __name__ == "__main__":
  print('Please provide your input with SoP implicants in comma-separated format')
  input_list = input()
  input_list = clean_input_string(input_list)
  print("\nGiven input is:", input_list)
  print("\n")
  input_list = input_list.split(",")
  input_list = [eval(i) for i in input_list]

  input_list.sort()

  response = input("Do you know the number of variables for your equation?\nType y for 'yes' and n for 'no': ")
  print("\n")
  if response == "y":
    num_variables = int(input("What is the number of variables in your input: "))
  else:
    num_variables = 1
    while not (input_list[-1] <= ((2 ** num_variables) - 1)):
      num_variables += 1
    print("The least number of variables based on your input is:", num_variables)

  print("\nNumber of variables in the expression is:", num_variables, "from a0 to a" + str(num_variables - 1))

  df = pd.DataFrame(columns=['Group', 'Combo', 'BinaryRep'])

  for i in input_list:
    df.loc[len(df.index)] = [calculate_group(i), calculate_combo(i), calculate_binary_representation(i, num_variables)]

  df = df.sort_values(by='Group').reset_index(drop=True)

  df_new = pd.DataFrame(columns=['Group', 'Combo', 'BinaryRep'])
  df_combined = df.copy()

  while True:
    new_list = df['Group'].tolist()
    new_dict = {}
    for num in new_list:
      new_dict[num] = new_dict.get(num, 0) + 1
    group_list = list(new_dict.keys())

    for i in range(len(group_list) - 1):
      if i == 0:
        p1 = 0
        p2 = p1 + new_dict[group_list[i]]
      else:
        p1 = p2
        p2 = p1 + new_dict[group_list[i]]
      for j in range(new_dict[group_list[i]]):
        for k in range(new_dict[group_list[i + 1]]):
          if create_combined_string(df['BinaryRep'].iloc[p1 + j], df['BinaryRep'].iloc[p2 + k]) == 0:
            z = 0
          else:
            df_new.loc[len(df_new.index)] = [df['Group'].iloc[p1 + j], df['Combo'].iloc[p1 + j]
                             + "," + df['Combo'].iloc[p2 + k],
                             create_combined_string(df['BinaryRep'].iloc[p1 + j],
                                        df['BinaryRep'].iloc[p2 + k])]
            df_combined = df_combined.drop(df_combined[df_combined['BinaryRep'] == df['BinaryRep'].iloc[p1 + j]].index)
            df_combined = df_combined.drop(df_combined[df_combined['BinaryRep'] == df['BinaryRep'].iloc[p2 + k]].index)

    df_combined = pd.concat([df_combined, df_new], axis=0)
    df = df_new.copy()
    df_new = df_new[0:0]
    if len(df) == 0:
      break

  final_list = list(set(df_combined['BinaryRep'].tolist()))

  expression = ''
  for i in final_list:
    expression += str(generate_expression(i)) + '+ '

  expression = expression[:-3]
  print("The non-minimized expression is:", expression)

  combined_combinations = ','.join(df_combined.loc[df_combined['BinaryRep'].isin(final_list), 'Combo'].tolist())

  combination_list = combined_combinations.split(",")
  combination_dict = {}
  for num in combination_list:
    combination_dict[num] = combination_dict.get(num, 0) + 1

  minimized_list = []
  for i in final_list:
    combination = df_combined.loc[df_combined['BinaryRep'] == i, 'Combo'].iloc[0]
    combination_list = combination.split(",")
    for j in combination_list:
      if combination_dict[j] == 1:
        minimized_list.append(i)
        break

  minimized_expression = ''
  for i in minimized_list:
    minimized_expression += generate_expression(i) + ' + '

  minimized_expression = minimized_expression[:-3]  # Remove the last ' + '

  if len(minimized_expression) == 0:
    print("Your expression results in a constant, either 0 or 1")
  else:
    print("The minimized expression is:", minimized_expression)
