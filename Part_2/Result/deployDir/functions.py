
"""
Split function

Input: 
    original (string) - the string to split
Returns: 
    (list of chars) - list containing the chars of the given string
"""
def split(original):
   return list(original) 

"""
Shift function

Input:
    original_char (char) - the char from the original string
    offset (int) - the offset by which the character is shifted to the RIGHT (offset = 1 -> 'a' becomes 'b')
Output:
    (char) - the character created by applying the provided offset to the provided char
"""
def shift(original_char, offset):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    ALPHA = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = original_char
    if original_char in alpha or original_char in ALPHA:
        arr = alpha if original_char in alpha else ALPHA
        idx = arr.index(original_char)
        new_idx = (idx + offset) % 26
        result = arr[new_idx]    
    return result

"""
Assemble function

Input:
    shifted_arr (char list) - the list of the characters to assemble
Output:
    (string) - the string created by concatenating the characters
"""
def assemble(char_list):
    return "".join(char_list)

