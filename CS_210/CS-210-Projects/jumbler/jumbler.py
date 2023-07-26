"""jumbler:  List dictionary words that match an anagram.
2023-05-05 by John M.

Credits: 
John M. - 2023-05-05 - Initial implementation
Youtube - slight background reserach, haha.
"""

import os

# Change the current working directory to the folder containing the dictionary file
os.chdir(r"C:\Users\johnm\dev\UO CS Work\CS 210\CS-210-Projects\jumbler")

# Path to the dictionary file
DICT = "dict.txt"
# Open the dictionary file for reading
dict_file = open(DICT, "r")

# Initialize an empty list to store the words from the dictionary
word_list = []
# Read each line in the dictionary file
for line in dict_file:
    # Remove any trailing whitespace characters and append the word to the word_list
    word = line.rstrip()
    word_list.append(word)

def normalize(word: str) -> str:
    """Return word in lowercase, sorted."""
    # Convert the word to lowercase
    word = word.lower()
    # Sort the characters in the word and join them back into a string
    return ''.join(sorted(word))

def find_anagrams(input_word: str, word_list):
    # Normalize the input word
    input_word_normalized = normalize(input_word)
    # Initialize an empty list to store the anagrams
    anagrams = []

    # Iterate through each word in the word_list
    for word in word_list:
        # Check if the normalized forms of the current word and input_word match
        if normalize(word) == input_word_normalized:
            # If they match, add the word to the list of anagrams
            anagrams.append(word)

    # Return the list of anagrams
    return anagrams

# Get user input for the word to find anagrams
input_word = input("Enter a word to find its anagrams: ")
# Call the find_anagrams function to get the list of anagrams
anagrams = find_anagrams(input_word, word_list)

# Print the results
print("Anagrams of", input_word, "are:", anagrams[0:])

# Close the dictionary file
dict_file.close()





