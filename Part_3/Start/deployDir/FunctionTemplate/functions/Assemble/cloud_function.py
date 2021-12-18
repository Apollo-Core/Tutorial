def cloud_function(json_input):
    shifted_arr = json_input["shiftedCharArr"]
    result = "".join(shifted_arr)
    # return the result
    res = {
        "encodedString": result
    }
    return res
