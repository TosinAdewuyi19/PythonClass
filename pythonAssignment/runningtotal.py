def running_total(list):
    totals = []
    current_total = 0
    for number in list:
        current_total += number
        totals.append(current_total)
    return totals

sample_list = [1, 2, 3, 4, 5]
print("Running total of the list is:", running_total(sample_list))
