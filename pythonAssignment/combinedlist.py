def combine_alternating(list1, list2):
    combined_list = []
    length = min(len(list1), len(list2))
    for count in range(length):
        combined_list.append(list1[count])
        combined_list.append(list2[count])
    combined_list.extend(list1[length:])
    combined_list.extend(list2[length:])
    return combined_list

