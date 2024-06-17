
main()
|
├── display_menu()
|   
├── get_num_variables() -> num_variables
|
├── get_input() -> input_list
|
├── get_name() -> user_name
|
├── generate_minterms_from_name(user_name) -> minterms
|
├── find_min_variables(input_list) -> num_variables
|
├── count_set_bits(number) -> set_bits_count
|
├── create_combination(number) -> combination_string
|
├── generate_binary_representation(number, num_variables) -> binary_string
|
├── find_single_bit_difference(string1, string2) -> diff_string or None
|
├── generate_expression(binary_string) -> expression
|
├── Process DataFrames (df_original, df_temp, df_result)
|   ├── Sort and group minterms by set bits
|   ├── Find prime implicants
|   └── Identify essential prime implicants
|
└── Print minimized expression


main():
    display_menu()
    variant = get user input

    if variant == '1':
        if user knows number of variables:
            num_variables = get_num_variables()
            input_list = get_input()
        else:
            input_list = get_input()
            num_variables = find_min_variables(input_list)
            print num_variables
    elif variant == '2':
        user_name = get_name()
        minterms = generate_minterms_from_name(user_name)
        input_list = minterms
        num_variables = find_min_variables(input_list)
        print num_variables
    else:
        exit

    input_list.sort()
    df_original = create DataFrame with minterms and their binary representations

    df_result = df_original.copy()
    df_temp = empty DataFrame

    while df_original is not empty:
        for each group in df_original:
            find pairs with single bit difference
            update df_temp and df_result accordingly
        
        update df_original with df_temp
        reset df_temp

    essential_list = find essential prime implicants from df_result
    remaining_implicants = find remaining prime implicants

    while remaining_implicants:
        find best implicant covering most uncovered minterms
        update essential_list and covered_minterms

    minimized_expression = generate expression from essential_list
    print minimized_expression
