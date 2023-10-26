# def StringChallenge(strParam):

#     return strParam

# print(StringChallenge(input()))

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
    
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    
    return roman_num

# Input a normal number
num = int(input("Enter a normal number: "))

# Call the int_to_roman function to convert it to Roman numerals
roman_numeral = int_to_roman(num)

# Output the result
print(f"The Roman numeral for {num} is {roman_numeral}")
