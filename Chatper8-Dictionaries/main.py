def print_scores(gradebook):
    # loops through keys
    for student in gradebook:
        total_points = 0
        points_earned = 0
        # keys in the dictionary associated with the student key
        for assignment in gradebook[student]:
            print(f'{assignment} : {gradebook[student][assignment]}')
            # first item in the list associated with the assignment
            points_earned += gradebook[student][assignment][0]
            total_points += gradebook[student][assignment][1]

        print(f'{student} : {points_earned / total_points * 100:.2f}%')


gradebook = {}

gradebook['Eric'] = {}

gradebook['Eric']['Project 1'] = [95, 100]
gradebook['Eric']['Project 2'] = [98, 100]
gradebook['Eric']['Lab 1'] = [5, 10]


student = input("Enter a student to add to the gradebook")

if student not in gradebook:
    gradebook[student] = {}

    assignment = input(f"Enter an assignment to add for {student}")

    while assignment != "DONE":
        gradebook[student][assignment] = []
        points_earned = int(input("Enter the points earned "))
        total_points = int(input("Enter the total points possible"))
        gradebook[student][assignment].append(points_earned)
        gradebook[student][assignment].append(total_points)
        assignment = input(f"Enter an assignment to add for {student} or DONE")

print_scores(gradebook)