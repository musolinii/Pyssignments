student_grades = [("Alice", 89.5), ("Bob", 92.3), ("Charlie", 78.9), ("David", 85.6)]


def grade_analyzer(grades,operation):
    
    if (operation == "average"):
        
        total = 0
        average = 0

        for grade in student_grades:
            total += grade[1]
            average = total / len(student_grades)
        print(average)

    elif (operation == "highest"):

        highest = -1
        name = ""

        for grade in student_grades:
            
            if (grade[1] > highest):
                highest = grade[1]
                name = grade[0]
            
        print(name,highest)

    
    elif (operation == "lowest"):

        lowest = 100
        name = ""
        
        for grade in student_grades:

            if (grade[1] < lowest):
                lowest = grade[1]
                name = grade[0]
        print(name,lowest)

    else :
        print("Enter correct input")


operation = input("Give appropriate operation:")
operation.lower()
grade_analyzer(student_grades,operation)