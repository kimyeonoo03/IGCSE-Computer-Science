number = int(input("Please enter the number of students."))
name_list = []
score_list = []
for x in range (0, number):
    name = input("Please enter the name of the student.")
    score = int(input("Please enter the score of the student."))
    name_list.append(name)
    score_list.append(score)

highest_score = 0
for y in range (0, number - 1):
    if highest_score < score_list[y]:
        highest_score = score_list[y]

if highest_score == score_list[y]:
    print (name_list[y],score_list[y])
