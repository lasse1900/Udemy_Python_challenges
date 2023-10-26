def ArrayChallenge(strArr):
    # Check if the input list contains exactly two strings
    if len(strArr) != 2:
        return "Input must contain exactly two strings."

    s1 = strArr[0]
    s2 = strArr[1]

    # Check if the strings have the same length
    if len(s1) != len(s2):
        return "Input strings must have the same length."

    # Initialize a variable to keep track of the distance
    distance = 0

    # Compare each character of the strings
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1

    return distance

# Input strings
input_strings = input().split()

# Call the ArrayChallenge function with the input
result = ArrayChallenge(input_strings)

# Output the result
print(result)
