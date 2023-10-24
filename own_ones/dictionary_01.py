# Create an English to Spanish dictionary
english_to_spanish = {
    "apple": "manzana",
    "banana": "plátano",
    "car": "coche",
    "cat": "gato",
    "dog": "perro",
}

# Look up translations
word = input("Enter a word in English: ")
if word in english_to_spanish:
    translation = english_to_spanish[word]
    print(f"The Spanish translation of {word} is {translation}.")
else:
    print(f"Sorry, we don't have a translation for {word} in our dictionary.")
