from classroom import Student, Teacher

def main():
    s = Student("Alice", "Van", "Physics")
    s.print_name_subject()  # "Alice Van, Physics"

    t = Teacher("Bob", "Smith", "Python Programming")
    t.print_name_course()   # "Bob Smith teaches Python Programming"

if __name__ == "__main__":
    main()
