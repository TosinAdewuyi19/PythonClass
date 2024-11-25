def remove_elements(original_list, to_remove):
    if isinstance(to_remove, list):
        return [item for item in original_list if item not in to_remove]
    else:
        return [item for item in original_list if item != to_remove]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
to_remove_single = 5
to_remove_list = [2, 4, 6]

print(remove_elements(numbers, to_remove_single))  
print(remove_elements(numbers, to_remove_list))    
