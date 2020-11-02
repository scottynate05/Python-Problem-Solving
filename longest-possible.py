# Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

# Examples:

# csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
# csLongestPossible("abc", "abc") -> "abc"
# [execution time limit] 4 seconds (py3)

# [input] string str_1

# [input] string str_2

# [output] string

def csLongestPossible(str_1, str_2):
    # result = []
    # if(len(str_1) < len(str_2)):
    #     for i in str_1:
    #         if(i in str_2):
    #             result.append(i)
    # else:
    #     for i in str_2:
    #         if(i in str_1):
    #             result.append(i)
    # return ''.join(dict.fromkeys(result))
    new_str = str_1 + str_2
    # return ''.join(OrderedDict.fromkeys(new_str))
    t = ''
    for i in new_str:
        if(i in t):
            pass
        else:
            t = t + i
    return ''.join(sorted(t))