def dict.valie_search(request_value, dict_request):
    count = 0
    for i, j in dict_request.items():
        if request_value in j:
            return_request_value = True
            return_key_dict = i
            count += 1
    if count == 0:
        return_request_value = False
        return_key_dict = None
    return [return_request_value, return_key_dict]
