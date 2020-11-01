# Given a string, return a new string with all the vowels removed.

# Examples:

# csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
# Notes:

# For this challenge, "y" is not considered a vowel.
# [execution time limit] 4 seconds (py3)

# [input] string input_str

# [output] string

def csRemoveTheVowels(input_str):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in input_str:
        if x in vowels:
            input_str = input_str.replace(x, '')
    return input_str