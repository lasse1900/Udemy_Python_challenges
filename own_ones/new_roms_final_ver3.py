def roman_to_decimal(roman_numeral):
  # Create a dictionary mapping Roman numerals to their decimal values.
  roman_numeral_map = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
  }

  decimal_value = 0

  for i in range(len(roman_numeral)):
    # Get the current Roman numeral character.
    current_roman_numeral = roman_numeral[i]

    # Get the decimal value of the current Roman numeral character.
    current_decimal_value = roman_numeral_map[current_roman_numeral]

    # If the next Roman numeral character is greater than the current Roman
    # numeral character, then the current Roman numeral character is a
    # subtraction.
    next_roman_numeral = roman_numeral[i + 1] if i + 1 < len(roman_numeral) else None
    if next_roman_numeral and roman_numeral_map[next_roman_numeral] > current_decimal_value:
      decimal_value -= current_decimal_value
    else:
      decimal_value += current_decimal_value

  return decimal_value

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    
    roman_num = ''
    i = 0
    
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    
    return roman_num

# roman_numeral = "LLXXXVVV"
roman_numeral = input("Give a roman number: ")
decimal_number = roman_to_decimal(roman_numeral)

roman_numeral = int_to_roman(decimal_number)
print(roman_numeral)