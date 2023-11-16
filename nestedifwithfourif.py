university = input("Enter university name: ")
degree = input("Enter degree level (UG or PG): ")
stream = input("Enter course stream (Science or Arts): ")
course_name = input("Enter course name: ")

if university == "calicut":
    if degree == "UG":
        if stream == "Science":
            if course_name == "maths":
                print("Seats available")
            elif course_name == "cs":
                print("Admission completed")
            else:
                print("course not available")
        elif stream == "Arts":
            if course_name == "english":
                print("Seats available")
            elif course_name == "history":
                print("Admission completed")
            else:
                print("course not available")
            print("Course:", course_name)
        else:
            print("Invalid stream.")
    elif degree == "PG":
        if stream == "Science":
            if course_name == "maths":
                print("10 Seats available")
            elif course_name == "cs":
                print("Admission not started")
            else:
                print("course not available")

        elif stream == "Arts":
            if course_name == "english":
                print("Seats available")
            elif course_name == "history":
                print("Admission completed")
            else:
                print("course not available")
        else:
            print("Invalid stream.")
    else:
        print("Invalid degree level.")
elif university == "University2":
    pass
else:
    print("Invalid university.")

