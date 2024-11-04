def two_highest_scores():
    number_of_students = input("Enter the number of students: ")

    highest_name = ""
    highest_score = 0
    
    second_highest_name = ""
    second_highest_score = 0

    for_a_in_range(number_of_students)
    name = input("Enter student's name: ")
    score = int(input("Enter student's score: "))
        
        if score > highest_score:
            second_highest_name = highest_name
            second_highest_score = highest_score
            
            highest_name = name
            highest_score = score
        elif score > second_highest_score:
            second_highest_name = name
            second_highest_score = score
    
    print("Top two students:")
    print(f"{highest_name}'s score is {highest_score}")
    print(f"{second_highest_name}'s score is {second_highest_score}")

two_highest_scores()