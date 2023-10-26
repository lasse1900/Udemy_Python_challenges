def hamming_distance(s1, s2):
    # Check if the input strings have the same length
    if len(s1) != len(s2):
        raise ValueError("Input strings must have the same length")

    # Initialize a variable to keep track of the distance
    distance = 0

    # Compare each character of the strings
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1

    return distance

# Input strings
string1 = "10011"
string2 = "10100"

# Calculate the Hamming distance
distance = hamming_distance(string1, string2)

# Output the result
print(f"The Hamming distance between '{string1}' and '{string2}' is {distance}")
