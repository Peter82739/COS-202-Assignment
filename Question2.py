print("PERSONAL POCKET CGPA CALCULATOR")

while True:

    total_unit = 0
    total_point = 0

    n = int(input("\nEnter Number of Courses: "))

    for i in range(n):

        print("\nCourse", i + 1)

        unit = int(input("Course Unit: "))
        score = int(input("Course Score: "))

        match score:

            case s if 70 <= s <= 100:
                point = 5
                grade = "A"

            case s if 60 <= s <= 69:
                point = 4
                grade = "B"

            case s if 50 <= s <= 59:
                point = 3
                grade = "C"

            case s if 45 <= s <= 49:
                point = 2
                grade = "D"

            case s if 40 <= s <= 44:
                point = 1
                grade = "E"

            case s if 0 <= s <= 39:
                point = 0
                grade = "F"

            case _:
                print("Invalid Score")
                continue

        quality = unit * point

        total_unit += unit
        total_point += quality

        print("Grade =", grade)

    cgpa = total_point / total_unit

    print("\nTotal Units =", total_unit)
    print("Total Points =", total_point)
    print("CGPA =", round(cgpa, 2))

    again = input("\nCalculate Again? (Y/N): ").upper()

    match again:
        case "Y":
            continue
        case "N":
            print("Thank You")
            break
        case _:
            print("Invalid Input")
            break