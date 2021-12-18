import json
from cloud_function import *


##################################################
########## Boilerplate wrapping code #############
##################################################

# IBM wrapper
def main(args):
    res = cloud_function(args)
    return res


def lambda_handler(event, context):
    # read in the args from the POST object
    json_input = json.loads(event["body"])
    res = cloud_function(json_input)
    return {"statusCode": 200, "body": json.dumps(res)}


##################################################
##################################################



# Docker wrapper
if __name__ == "__main__":
    # read the json
    json_input = json.loads(open("jsonInput.json").read())
    result = cloud_function(json_input)

    # write to std out
    print(json.dumps(result))