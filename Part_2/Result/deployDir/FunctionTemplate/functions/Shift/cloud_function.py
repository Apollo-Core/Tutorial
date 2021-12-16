def cloud_function(json_input):
    original_char = json_input["char"]
    offset = json_input["offset"]
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    ALPHA = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = original_char
    if original_char in alpha or original_char in ALPHA:
        arr = alpha if original_char in alpha else ALPHA
        idx = arr.index(original_char)
        new_idx = (idx + offset) % 26
        result = arr[new_idx]    
    # return the result
    res = {
        "shiftedChar": result
    }
    return res
