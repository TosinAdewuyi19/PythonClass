def get_largest_element(element):
    if not element:
        return None 
    
    largest = None
    for number in element:
        if largest is None or number > largest:
            largest = number
    return largest

element = {20,10,25,40}
print(get_largest_element(element))