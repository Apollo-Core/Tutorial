def cloud_function(json_input):
    original = json_input["original"]    
    # Processing
    result = list(original) 
    # return the result
    res = {
        "charArr": result
    }
    return res
