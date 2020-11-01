# Given a string of words, return the length of the shortest word(s).

# Notes:

# The input string will never be empty and you do not need to validate for different data types.
# [execution time limit] 4 seconds (py3)

# [input] string input_str

# [output] integer

def csShortestWord(input_str):
    word = ''
    all_words = []
    
    input_str = input_str.lower() + ' '
    
    for i in range(0, len(input_str)):
        if(input_str[i] != ' '):
            word = word + input_str[i]
        else:
            all_words.append(word)
            word = ''
            
    small = all_words[0]
    
    for x in range(0, len(all_words)):
        if(len(small) > len(all_words[x])):
            small = all_words[x]
        
    return int(len(small))