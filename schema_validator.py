def validate_response(obj):
    #to check input is dictionary
    if not isinstance(obj,dict):
        return False,"response must be in dictionary"
    
    #required input or keys
    required_keys=["id","name","email"]
    for key in required_keys:
        if key not in obj:
            return False,f"missing required key:{key}"
        
    #for validation of key
    if not isinstance(obj["id"],int):
        return False,"id must be in integer type"
    #for validation of name
    if not isinstance(obj["name"],str):
        return False,"name must be in string type"
    #for validation od email i.e check for "@"
    if not isinstance(obj["email"],str):
        return False,"email id must be in string"
    if not "@" in obj["email"]:
        return False,"email must contain '@"
    return True,"valid response"

#structure for valid response
if __name__=="__main__":
    valid_response={
        "id":1,
        "name":"tim",
        "email":"tim@gmail.com"
    }

    #to check missing email
    invalid_response_1={
        "id":2,
        "name":"rain"
    }
    #to check invalid email
    invalid_response_2 = {
        "id":3,
        "name":"pop",
        "email": "popexample.com"
    }
print("Valid test:", validate_response(valid_response))
print("inValid test1:", validate_response(invalid_response_1))
print("inValid test2:", validate_response(invalid_response_2))

    