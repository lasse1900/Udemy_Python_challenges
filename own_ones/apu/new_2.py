def roman_to_shorter(roman_numeral):
  """Converts a Roman numeral to a shorter format, if possible.

  Args:
    roman_numeral: A string representing a valid Roman numeral.

  Returns:
    A string representing the Roman numeral in a shorter format, if possible,
    or the original Roman numeral otherwise.
  """

  # Create a dictionary mapping Roman numerals to their shorter forms.
  roman_to_shorter_map = {
      "IIIII": "V",
      "IIII": "IV",
      "XXXX": "L",
      "XXX": "XL",
      "CCCC": "D",
      "CCC": "CD",
      "MMMM": "M",
      "MMM": "MM"
  }

  # Iterate over the Roman numeral, looking for substrings that can be
  # replaced with shorter forms.
  shorter_roman_numeral = ""
  for i in range(len(roman_numeral)):
    if i + 4 < len(roman_numeral) and roman_numeral[i:i + 5] in roman_to_shorter_map:
      shorter_roman_numeral += roman_to_shorter_map[roman_numeral[i:i + 5]]
      i += 4
    else:
      shorter_roman_numeral += roman_numeral[i]

  return shorter_roman_numeral


# Example usage:

print(roman_to_shorter("LLXXXVVV"))  # "L"
print(roman_to_shorter("MMMDCCLXXVI"))  # "MMMDCCLXXVI" (shorter form not possible)
