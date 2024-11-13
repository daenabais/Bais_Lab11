#initializing variables
student_grades= []
num_of_students= 5
passing_grade= 75
passing_count= 0
#starting the loop
for i in range(num_of_students):
    x=int(input(f"Enter grade for student {i+ 1} (between 40-100):"))
    if 40 <= x <=100:
       student_grades.append(x)
       if x >= passing_grade:
           passing_count += 1
    else:
        print("Invalid input, please enter grade between 40-100.")
        break

#calculating the grades
else:
    average_grade= sum(student_grades) / num_of_students
    percentage_of_passers= passing_count / num_of_students * 100

#displaying the output
    print("Grades:", student_grades)
    print("The number of students who has passing grades:", passing_count)
    print("The perecentage of the class who passed:", percentage_of_passers, "%")
    print("The average grade of the class",average_grade)

