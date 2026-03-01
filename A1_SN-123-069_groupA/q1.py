def grade(marks):
    if marks >= 80:
        return "A+", 4.00
    elif marks >= 75:
        return "A", 3.75
    elif marks >= 70:
        return "A-", 3.50
    elif marks >= 65:
        return "B+", 3.25
    elif marks >= 60:
        return "B", 3.00
    elif marks >= 55:
        return "B-", 2.75
    elif marks >= 50:
        return "C+", 2.50
    elif marks >= 45:
        return "C", 2.25
    elif marks >= 40:
        return "D", 2.00
    else:
        return "F", 0.00
    

with open("student_marks.txt") as file:
    print("Roll\tLetter Grade\tGrade Point")
    for line in file:
        data = line.strip().split()  
        if len(data)!= 5:
            print("Invalid data format")
            continue

        roll, first, second, attendance, final = map(int, data)
        total_marks = (first + second)/2 + attendance + final

        letter_grade, grade_point = grade(total_marks)
        print(f"{roll}\t{letter_grade}\t\t{grade_point:.2f}")
