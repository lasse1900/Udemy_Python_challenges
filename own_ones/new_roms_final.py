def roman_to_short(roman):
    roman_numerals = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1
    }
    
    result = 0
    prev_value = 0

    for numeral in roman:
        value = roman_numerals[numeral]
        if prev_value < value:
            result -= prev_value
        else:
            result += prev_value
        prev_value = value

    result += prev_value

    # return result

    # Now, we convert the result back to the shorter Roman format
    short_roman = ""
    for r_symbol, r_value in sorted(roman_numerals.items(), key=lambda item: -item[1]):
        while result >= r_value:
            short_roman += r_symbol
            result -= r_value

    return short_roman

# Input a Roman numeral in longer format
roman_numeral = input("Enter a Roman numeral in longer format: ")

# Call the roman_to_short function to convert it to the shorter format
short_roman = roman_to_short(roman_numeral)

# Output the result
print(f"The Roman numeral in shorter format is: {short_roman}")
