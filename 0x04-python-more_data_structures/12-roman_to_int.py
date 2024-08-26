def roman_to_int(roman_string):
    decimal_roman = 0
    i = 0
    while i < len(roman_string):
        if roman_string[i] == "M":
            decimal_roman += 1000
        elif roman_string[i] == "C" and i + 1 < len(roman_string) and roman_string[i + 1] == "D":
            decimal_roman += 400
            i += 1
        elif roman_string[i] == "C" and i + 1 < len(roman_string) and roman_string[i + 1] == "M":
            decimal_roman += 900
            i += 1
        elif roman_string[i] == "C":
            decimal_roman += 100
        elif roman_string[i] == "D":
            decimal_roman += 500
        elif roman_string[i] == "X" and i + 1 < len(roman_string) and roman_string[i + 1] == "L":
            decimal_roman += 40
            i += 1
        elif roman_string[i] == "X" and i + 1 < len(roman_string) and roman_string[i + 1] == "C":
            decimal_roman += 90
            i += 1
        elif roman_string[i] == "X":
            decimal_roman += 10
        elif roman_string[i] == "L":
            decimal_roman += 50
        elif roman_string[i] == "I" and i + 1 < len(roman_string) and roman_string[i + 1] == "V":
            decimal_roman += 4
            i += 1
        elif roman_string[i] == "I" and i + 1 < len(roman_string) and roman_string[i + 1] == "X":
            decimal_roman += 9
            i += 1
        elif roman_string[i] == "I":
            decimal_roman += 1
        elif roman_string[i] == "V":
            decimal_roman += 5
        i += 1
    return decimal_roman


